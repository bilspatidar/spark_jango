from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import FormField
from .serializers import FormFieldSerializer
from rest_framework.settings import api_settings


class FormFieldListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:
            formfield = get_object_or_404(FormField, pk=pk)
            serializer = FormFieldSerializer(formfield)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)
        else:
            formfields = FormField.objects.all()
            serializer = FormFieldSerializer(formfields, many=True)
            return Response({
                "status": "Success",
                "data": serializer.data,
                "errors": ""
            }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwarges):
        serializer = FormFieldSerializer(data=request.data)
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
        formfield = get_object_or_404(FormField, pk=pk)
        serializer = FormFieldSerializer(formfield, data=request.data, partial=True)
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
        formfield = get_object_or_404(FormField, pk=pk)
        formfield.delete()
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
