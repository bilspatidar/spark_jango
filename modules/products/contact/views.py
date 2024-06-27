from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.settings import api_settings
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ContactListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request, pk=None):
        if pk:
            contact = get_object_or_404(Contact, pk=pk)
            serializer = ContactSerializer(contact)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)
        else:
            name = request.data.get('name')
            contacts = Contact.objects.all()
            if name:
                contacts = contacts.filter(name__icontains=name)
            contacts = contacts.order_by('id')
            paginator = self.pagination_class()
            page = paginator.paginate_queryset(contacts, request)

            if page is not None:
                serializer = ContactSerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)

            serializer = ContactSerializer(contacts, many=True)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
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
        contact = get_object_or_404(Contact, pk=pk)
        serializer = ContactSerializer(contact, data=request.data, partial=True)
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
        contact = get_object_or_404(Contact, pk=pk)
        contact.delete()
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
