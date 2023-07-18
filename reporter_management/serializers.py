from rest_framework import serializers
from reporter_management.models import Reporter

class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = "__all__"
