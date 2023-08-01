from case_management.models import Case, ReportingDetail, AnimalDetail, MedicalDetail, OperationDetail, PostOperationDetail
from rest_framework import serializers

class ReportingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportingDetail
        fields = "__all__"

class AnimalDetailSerializer(serializers.ModelSerializer):
    # animalPictures = serializers.ListField(child=serializers.ImageField(), required=False)
    class Meta:
        model = AnimalDetail
        fields = "__all__"

    # def validate_animalPictures(self, value):
    #     # Here, you can implement any custom validation for the images if needed.
    #     # For now, we'll simply return the value as it is.
    #     return value

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
    reportingdetail= ReportingDetailSerializer(read_only=True)
    animaldetail = AnimalDetailSerializer(read_only=True)
    medicaldetail = MedicalDetailSerializer(read_only=True)
    operationdetail = OperationDetailSerializer(read_only=True)
    postoperationdetail = PostOperationDetailSerializer(read_only=True)
    user_name = serializers.SerializerMethodField()
    # superuser = serializers.SerializerMethodField()

    class Meta:
        model = Case
        # fields = "__all__"
        fields = ('type_of_case', 'status_of_case', 'mortality_of_case', 'cause_of_failure', 'case_id', 'user_adding_this_case', 'user_name', "date_when_created", "date_when_last_updated", 'reportingdetail', 'animaldetail', 'medicaldetail', 'operationdetail', 'postoperationdetail')

    def get_user_name(self, obj):
        return f"{obj.user_adding_this_case}"
    
    # def get_superuser(self, obj):
    #     return f"{obj.user_adding_this_case}"