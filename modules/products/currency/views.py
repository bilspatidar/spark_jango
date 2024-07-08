from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Currency
from django.utils import timezone
from .serializers import CurrencySerializer
from rest_framework.settings import api_settings
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CurrencyListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request, pk=None):
        if pk:
            currency = get_object_or_404(Currency, pk=pk)
            serializer = CurrencySerializer(currency)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)
        else:
            name = request.data.get('name')
            currencies = Currency.objects.all()
            if name:
                currencies = currencies.filter(name__icontains=name)
            currencies = currencies.order_by('id')
            paginator = self.pagination_class()
            page = paginator.paginate_queryset(currencies, request)

            if page is not None:
                serializer = CurrencySerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)

            serializer = CurrencySerializer(currencies, many=True)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CurrencySerializer(data=request.data)
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
        currency = get_object_or_404(Currency, pk=pk)
        serializer = CurrencySerializer(currency, data=request.data, partial=True)
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
        currency = get_object_or_404(Currency, pk=pk)
        currency.delete()
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
