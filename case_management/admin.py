from django.contrib import admin
from case_management.models import Case, ReportingDetail, AnimalDetail, MedicalDetail, OperationDetail, PostOperationDetail

# Register your models here.
admin.site.register(Case)
admin.site.register(ReportingDetail)
admin.site.register(AnimalDetail)
admin.site.register(MedicalDetail)
admin.site.register(OperationDetail)
admin.site.register(PostOperationDetail)