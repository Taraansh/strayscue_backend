from rest_framework import serializers
from ngo_management.models import Ngo

class NgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ngo
        fields = '__all__'
