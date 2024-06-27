from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import AccountHead
from .serializers import AccountHeadSerializer
from rest_framework.settings import api_settings
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AccountHeadListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request, pk=None):
        if pk:
            account_head = get_object_or_404(AccountHead, pk=pk)
            serializer = AccountHeadSerializer(account_head)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)
        else:
            name = request.data.get('name')
            type = request.data.get('type')
            status = request.data.get('status')
            account_heads = AccountHead.objects.all()
            if name:
                account_heads = account_heads.filter(name__icontains=name)
            if type:
                account_heads = account_heads.filter(type=type)
            if status:
                account_heads = account_heads.filter(status=status)
            account_heads = account_heads.order_by('id')
            paginator = self.pagination_class()
            page = paginator.paginate_queryset(account_heads, request)

            if page is not None:
                serializer = AccountHeadSerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)
            
            serializer = AccountHeadSerializer(account_heads, many=True)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = AccountHeadSerializer(data=request.data)
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
        account_head = get_object_or_404(AccountHead, pk=pk)
        serializer = AccountHeadSerializer(account_head, data=request.data, partial=True)
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
        account_head = get_object_or_404(AccountHead, pk=pk)
        account_head.delete()
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
