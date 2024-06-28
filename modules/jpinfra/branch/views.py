from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Branch
from .serializers import BranchSerializer
from rest_framework.settings import api_settings
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BranchListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request, pk=None):
        if pk:
            branch = get_object_or_404(Branch, pk=pk)
            serializer = BranchSerializer(branch)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)
        else:
            branch_phone = request.data.get('branch_phone')
            name = request.data.get('name')
            
            branches = Branch.objects.all()

            if branch_phone:
                branches = branches.filter(branch_phone=branch_phone)
            if name:
                branches = branches.filter(name=name)
                
            branches = branches.order_by('id')
            paginator = self.pagination_class()
            page = paginator.paginate_queryset(branches, request)

            if page is not None:
                serializer = BranchSerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)
            
            serializer = BranchSerializer(branches, many=True)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = BranchSerializer(data=request.data)
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
        branch = get_object_or_404(Branch, pk=pk)
        serializer = BranchSerializer(branch, data=request.data, partial=True)
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
        branch = get_object_or_404(Branch, pk=pk)
        branch.delete()
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
