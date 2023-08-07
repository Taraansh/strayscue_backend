from django.contrib import admin
from case_management.models import Case, ReportingDetail, AnimalDetail, MedicalDetail, OperationDetail, PostOperationDetail, AnimalPictures, FeedingRecordImage, BloodReportImage, TreatmentRecordImage, OrganImage, PopPictures, ReleasePictures

# Register your models here.
admin.site.register(Case)

admin.site.register(ReportingDetail)

admin.site.register(AnimalDetail)
admin.site.register(AnimalPictures)

admin.site.register(MedicalDetail)
admin.site.register(FeedingRecordImage)
admin.site.register(BloodReportImage)

admin.site.register(OperationDetail)
admin.site.register(TreatmentRecordImage)
admin.site.register(OrganImage)

admin.site.register(PostOperationDetail)
admin.site.register(PopPictures)
admin.site.register(ReleasePictures)
