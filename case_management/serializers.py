from case_management.models import Case, ReportingDetail, AnimalDetail, MedicalDetail, OperationDetail, PostOperationDetail
from rest_framework import serializers

class ReportingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportingDetail
        fields = "__all__"

class AnimalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalDetail
        fields = "__all__"

class MedicalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalDetail
        fields = "__all__"

class OperationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationDetail
        fields = "__all__"

class PostOperationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostOperationDetail
        fields = "__all__"

class CaseSerializer(serializers.ModelSerializer):
    reportingdetail_set = ReportingDetailSerializer(many=True, read_only=True)
    animaldetail_set = AnimalDetailSerializer(many=True, read_only=True)
    medicaldetail_set = MedicalDetailSerializer(many=True, read_only=True)
    operationdetail_set = OperationDetailSerializer(many=True, read_only=True)
    postoperationdetail_set = PostOperationDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Case
        fields = "__all__"