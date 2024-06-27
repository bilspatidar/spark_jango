from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Document
from .serializers import DocumentSerializer
from rest_framework.settings import api_settings
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class DocumentCustomView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request, pk=None):
        if pk:
            document = get_object_or_404(Document, pk=pk)
            serializer = DocumentSerializer(document)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)
        else:
            name = request.data.get('name')

            documents = Document.objects.all()

            if name:
                documents = documents.filter(name__icontains=name)
            
            documents = documents.order_by('id') 
            
            paginator = self.pagination_class()
            page = paginator.paginate_queryset(documents, request)
            if page is not None:
                serializer = DocumentSerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)

            serializer = DocumentSerializer(documents, many=True)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        serializer = DocumentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  # user_created and user_updated will be set automatically
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""    
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "status": "Failed",
                "data": "",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        serializer = DocumentSerializer(document, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            instance = serializer.save(user_updated=request.user)
            instance.updated = timezone.now()  # Update the 'updated' field explicitly
            instance.save()
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)
        return Response({
            "status": "Failed",
            "data": "",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        document.delete()
        return Response({
            "status": "Success",
            "data": "",
            "errors": ""
        }, status=status.HTTP_204_NO_CONTENT)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}