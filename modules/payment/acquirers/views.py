from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Acquirer  # Update import to Acquirer model
from .serializers import AcquirerSerializer  # Update import to AcquirerSerializer
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AcquirerListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request, pk=None):
        if pk:
            acquirer = get_object_or_404(Acquirer, pk=pk)
            serializer = AcquirerSerializer(acquirer)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)
        else:
            name = request.query_params.get('name')  # Use query_params instead of data for GET requests

            acquirers = Acquirer.objects.all()
            if name:
                acquirers = acquirers.filter(name__icontains=name)
            
            acquirers = acquirers.order_by('id')
            
            paginator = self.pagination_class()
            page = paginator.paginate_queryset(acquirers, request)
            if page is not None:
                serializer = AcquirerSerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)

            serializer = AcquirerSerializer(acquirers, many=True)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = AcquirerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_created=request.user)
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
        acquirer = get_object_or_404(Acquirer, pk=pk)
        serializer = AcquirerSerializer(acquirer, data=request.data, partial=True)
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
        acquirer = get_object_or_404(Acquirer, pk=pk)
        acquirer.delete()
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
