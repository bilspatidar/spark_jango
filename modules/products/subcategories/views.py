from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import SubCategory
from .serializers import SubCategorySerializer
from rest_framework.settings import api_settings
from rest_framework.pagination import PageNumberPagination
from django.template.loader import render_to_string
from emails.utils import send_subcategory_creation_email 
# from .utils import send_subcategory_creation_email

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class SubCategoryCustomView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request, pk=None):
        if pk:
            subcategory = get_object_or_404(SubCategory, pk=pk)
            serializer = SubCategorySerializer(subcategory)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)
        else:
            category = request.data.get('category')
            name = request.data.get('name')

            subcategories = SubCategory.objects.all()
            if category:
                subcategories = subcategories.filter(category=category)
            if name:
                subcategories = subcategories.filter(name__icontains=name)
            
            subcategories = subcategories.order_by('id') 
            
            paginator = self.pagination_class()
            page = paginator.paginate_queryset(subcategories, request)
            if page is not None:
                serializer = SubCategorySerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)

            serializer = SubCategorySerializer(subcategories, many=True)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save(user_created=request.user)
            send_subcategory_creation_email(instance)
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
        subcategory = get_object_or_404(SubCategory, pk=pk)
        serializer = SubCategorySerializer(subcategory, data=request.data, partial=True)
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
        subcategory = get_object_or_404(SubCategory, pk=pk)
        subcategory.delete()
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
