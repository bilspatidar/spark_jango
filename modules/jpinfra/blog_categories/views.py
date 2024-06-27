from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import BlogCategory
from .serializers import BlogCategorySerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from django.utils import timezone

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BlogCategoryListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request, pk=None):
        if pk:
            blog_category = get_object_or_404(BlogCategory, pk=pk)
            serializer = BlogCategorySerializer(blog_category)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)
        else:
            name = request.data.get('name')
            status = request.data.get('status')
            blog_categories = BlogCategory.objects.all()
            
            if name:
                blog_categories = blog_categories.filter(name__icontains=name)
            if status:
                blog_categories = blog_categories.filter(status=status)

            blog_categories = blog_categories.order_by('id')
            paginator = self.pagination_class()
            page = paginator.paginate_queryset(blog_categories, request)

            if page is not None:
                serializer = BlogCategorySerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)
            
            serializer = BlogCategorySerializer(blog_categories, many=True)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = BlogCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({
                "status": "Failed",
                "data": "",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        blog_category = get_object_or_404(BlogCategory, pk=pk)
        serializer = BlogCategorySerializer(blog_category, data=request.data, partial=True)
        if serializer.is_valid():
            instance = serializer.save()
            instance.date = timezone.now()  # Optionally update date
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
        blog_category = get_object_or_404(BlogCategory, pk=pk)
        blog_category.delete()
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
