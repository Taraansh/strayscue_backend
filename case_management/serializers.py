from case_management.models import Case, ReportingDetail, AnimalDetail, MedicalDetail, OperationDetail, PostOperationDetail, AnimalPictures, FeedingRecordImage, TreatmentRecordImage, MedicalPrescriptionImage, OrganImage, PopPictures, ReleasePictures, BloodReportImage
from rest_framework import serializers

# Reporting Detail Serializer
class ReportingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportingDetail
        fields = "__all__"

# Animal Detail Serializer
    # Animal Pictures Serializer
class AnimalPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalPictures
        # fields = "__all__"
        fields = ["id", "animal_linked", "animalPictures", "animal_picture_upload_date"]

class AnimalDetailSerializer(serializers.ModelSerializer):
    animalPictures = AnimalPicturesSerializer(many = True)
    class Meta:
        model = AnimalDetail
        # fields = "__all__"
        fields = ["id", "case_linked", "animalSpecies", "animalBreed", "animalAge", "animalTemperament", "animalGender", "animalPregnant", "animalMarking", "animalColor", "animalCatchable", "animalWeight", "admissionReason", "animalPictures"]


# Medical Detail Serializer
    # Blood Report Image Serializer
class BloodReportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodReportImage
        # fields = "__all__"
        fields = ["id", "medical_linked", "bloodReportImage", "blood_report_date"]

    # Feeding Record Image Serializer
class FeedingRecordImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedingRecordImage
        # fields = "__all__"
        fields = ["id", "medical_linked", "feedingRecordImage", "feeding_record_image_upload_date"]

class MedicalDetailSerializer(serializers.ModelSerializer):
    feedingRecordImage = FeedingRecordImageSerializer(many=True)
    bloodReportImage = BloodReportImageSerializer(many=True)
    class Meta:
        model = MedicalDetail
        # fields = "__all__"
        fields = ["id", "case_linked", "medicalHistory", "vaccinationStatus", "dewormed", "fitForSurgery", "otherDetails", "admissionDate", "bloodReportImage", "feedingRecordImage"]

# Operation Detail Serializer
    # Treatment Record Image Serializer
class TreatmentRecordImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentRecordImage
        # fields = "__all__"
        fields = ["id", "operation_linked", "treatmentRecordImage", "treatment_record_image_upload_date"]

    # Organ Image Serializer
class OrganImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganImage
        # fields = "__all__"
        fields = ["id", "operation_linked", "organImage", "organ_image_upload_date"]

    # Medical Prescription Image Serializer
class MedicalPrescriptionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalPrescriptionImage
        # fields = "__all__"
        fields = ["id", "operation_linked", "medicalPrescriptionImage", "medical_prescription_image_upload_date"]

class OperationDetailSerializer(serializers.ModelSerializer):
    medicalPrescriptionImage = MedicalPrescriptionImageSerializer(many=True)
    treatmentRecordImage = TreatmentRecordImageSerializer(many=True)
    organImage = OrganImageSerializer(many=True)
    class Meta:
        model = OperationDetail
        # fields = "__all__"
        fields = ["id", "case_linked", "vetName", "operationDate", "operationStartTime", "operationEndTime", "operationOutcome", "medicalPrescriptionImage", "treatmentRecordImage", "organImage"]

# Post Operation Detail Serializer
    # Post Operation Pictures Serializer
class PopPicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopPictures
        # fields = "__all__"
        fields = ["id", "post_operation_linked", "popPictures", "pop_pictures_upload_date"]

    # Release Pictures Serializer
class ReleasePicturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleasePictures
        # fields = "__all__"
        fields = ["id", "post_operation_linked", "releasePictures", "release_pictures_upload_date"]

class PostOperationDetailSerializer(serializers.ModelSerializer):
    popPictures = PopPicturesSerializer(many=True)
    releasePictures = ReleasePicturesSerializer(many=True)
    class Meta:
        model = PostOperationDetail
        fields = ["id", "case_linked", "popComment", "popFacility", "popExpectedDays", "popStartDate", "popEndDate", "releaseDate", "euthanized", "comments", "popPictures", "releasePictures"]

# Case Serializer
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