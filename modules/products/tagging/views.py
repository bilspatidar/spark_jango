from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Tagging
from .serializers import TaggingSerializer
from rest_framework.settings import api_settings
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class TaggingCustomViewList(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request, pk=None):
        if pk:
            tagging = get_object_or_404(Tagging, pk=pk)
            serializer = TaggingSerializer(tagging)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)
        else:
            booking_id = request.data.get('booking_id')
            taggings = Tagging.objects.all()
            if booking_id:
                taggings = taggings.filter(booking_id__icontains=booking_id)
                taggings = taggings.order_by('id') 
            
            paginator = self.pagination_class()
            page = paginator.paginate_queryset(taggings, request)
            if page is not None:
                serializer = TaggingSerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)
            serializer = TaggingSerializer(taggings, many=True)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwarges):
        serializer = TaggingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_created=request.user)
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
        tagging = get_object_or_404(Tagging, pk=pk)
        serializer = TaggingSerializer(tagging, data=request.data, partial=True)
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
        tagging = get_object_or_404(Tagging, pk=pk)
        tagging.delete()
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
