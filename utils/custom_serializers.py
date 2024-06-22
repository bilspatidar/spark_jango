from rest_framework import serializers
from django.utils import timezone

class CustomFieldsSerializer(serializers.Serializer):
    date_created = serializers.SerializerMethodField()
    date_updated = serializers.SerializerMethodField()

    def get_date_created(self, obj):
        return self.format_datetime(obj.date_created)

    def get_date_updated(self, obj):
        return self.format_datetime(obj.date_updated)

    def format_datetime(self, dt):
        if not dt:
            return ""
        dt = timezone.localtime(dt, timezone=timezone.get_current_timezone())
        return dt.strftime("%d/%b/%Y %H:%M:%S")