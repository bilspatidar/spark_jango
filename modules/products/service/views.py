from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Service
from .serializers import ServiceSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ServiceCustomView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request, pk=None):
        if pk:
            service = get_object_or_404(Service, pk=pk)
            serializer = ServiceSerializer(service)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)
        else:
            category = request.data.get('category')
            subcategory = request.data.get('subcategory')
            name = request.data.get('name')

            services = Service.objects.all()
            if category:
                services = services.filter(category__id=category)
            if subcategory:
                services = services.filter(subcategory__id=subcategory)
            if name:
                services = services.filter(name__icontains=name)

            paginator = self.pagination_class()
            result_page = paginator.paginate_queryset(services, request)
            serializer = ServiceSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
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
        service = get_object_or_404(Service, pk=pk)
        serializer = ServiceSerializer(service, data=request.data, partial=True)
        if serializer.is_valid():
            instance = serializer.save()
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
        service = get_object_or_404(Service, pk=pk)
        service.delete()
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
