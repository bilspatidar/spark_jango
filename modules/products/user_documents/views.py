from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import UserDocument
from .serializers import UserDocumentSerializer
from rest_framework.settings import api_settings
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class UserDocumentCustomView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request, pk=None):
        if pk:
            userdocuments = get_object_or_404(UserDocument, pk=pk)
            serializer = UserDocumentSerializer(userdocuments)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)
        else:
            verified_by = request.data.get('verified_by')
            document_id = request.data.get('document_id')

            userdocuments = UserDocument.objects.all()
            if verified_by:
                userdocuments = userdocuments.filter(verified_by=verified_by)
            if document_id:
                userdocuments = userdocuments.filter(document_id__icontains=document_id)
            
            userdocuments = userdocuments.order_by('id') 
            
            paginator = self.pagination_class()
            page = paginator.paginate_queryset(userdocuments, request)
            if page is not None:
                serializer = UserDocumentSerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)

            serializer = UserDocumentSerializer(userdocuments, many=True)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = UserDocumentSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save(user_created=request.user)
            userdocument = instance 
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
        userdocuments = get_object_or_404(UserDocument, pk=pk)
        serializer = UserDocumentSerializer(userdocuments, data=request.data, partial=True)
        if serializer.is_valid():
            instance = serializer.save(user_updated=request.user)
            instance.date_updated = timezone.now()
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
        userdocuments = get_object_or_404(UserDocument, pk=pk)
        userdocuments.delete()
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
