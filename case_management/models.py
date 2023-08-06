from django.db import models
from authorization.models import Profile

# Create your models here.
class Case(models.Model):
    TYPE_OF_CASE = [
            ('Vaccination', 'Vaccination'),
            ('Sterilization', 'Sterilization'),
            ('OPD', 'OPD'),
            ('IPD', 'IPD'),
        ]

    STATUS_OF_CASE = [
            ('Reported', 'Reported'),
            ('Admitted', 'Admitted'),
            ('Blood Test', 'Blood Test'),
            ('Operation', 'Operation'),
            ('Post Operation', 'Post Operation'),
            ('Released', 'Released'),
        ]

    MORTALITY_OF_CASE = [
            ('Healthy', 'Healthy'),
            ('Unhealthy', 'Unhealthy'),
            ('Fatal', 'Fatal'),
        ]
    type_of_case = models.CharField(max_length=255, choices=TYPE_OF_CASE, null=True)
    status_of_case = models.CharField(max_length=255, choices=STATUS_OF_CASE, null=True)
    mortality_of_case = models.CharField(max_length=255, choices=MORTALITY_OF_CASE, null=True)
    cause_of_failure = models.TextField(null=True, blank=True)
    case_id = models.AutoField(primary_key=True)
    date_when_created = models.DateTimeField(auto_now_add=True)
    date_when_last_updated = models.DateTimeField(auto_now=True)
    user_adding_this_case = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Case - ID: {self.case_id} - {self.type_of_case}"


class ReportingDetail(models.Model):
    case_linked = models.OneToOneField(Case, on_delete=models.CASCADE)
    reporterName = models.CharField(max_length=255, blank=True, null=True)
    reporterContact = models.CharField(max_length=255, blank=True, null=True)
    reporterAltContact = models.CharField(max_length=255, blank=True, null=True)
    reporterEmail = models.CharField(max_length=255, blank=True, null=True)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    pincode = models.CharField(max_length=255, blank=True, null=True)
    reportedDate = models.DateField(blank=True, null=True)
    reportedTime = models.TimeField(blank=True, null=True)
    pickupDate = models.DateField(blank=True, null=True)
    pickupTime = models.TimeField(blank=True, null=True)
    frontImage = models.ImageField(upload_to='sponsor_logos/front/', null=True, blank=True)
    backImage = models.ImageField(upload_to='sponsor_logos/back/', null=True, blank=True)
    consentFormImage = models.ImageField(upload_to='sponsor_logos/consent_form/', null=True, blank=True)

    def __str__(self):
        return self.reporterName


class AnimalDetail(models.Model):
    ANIMAL_SPECIES_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Other', 'Other'),
    ]
    ANIMAL_BREED_CHOICES = [
        ('Indie', 'Indie'),
        ('Pet', 'Pet'),
        ('Other', 'Other'),
    ]
    ANIMAL_AGE_CHOICES = [
        ('0-1', '0-1'),
        ('1-5', '1-5'),
        ('5-10', '5-10'),
        ('10+', '10+'),
    ]
    ANIMAL_TEMPERAMENT_CHOICES = [
        ('Friendly', 'Friendly'),
        ('Aggressive', 'Aggressive'),
        ('Scared', 'Scared'),
        ('Other', 'Other'),
    ]
    ANIMAL_GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    ANIMAL_PREGNANT_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Not Sure', 'Not Sure'),
    ]
    ANIMAL_CATCHABLE_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    case_linked = models.OneToOneField(Case, on_delete=models.CASCADE)
    animalSpecies = models.CharField(max_length=255, choices=ANIMAL_SPECIES_CHOICES, null=True, blank=True)
    animalBreed = models.CharField(max_length=255, choices=ANIMAL_BREED_CHOICES, null=True, blank=True)
    animalAge = models.CharField(max_length=255, choices=ANIMAL_AGE_CHOICES, null=True, blank=True)
    animalTemperament = models.CharField(max_length=255, choices=ANIMAL_TEMPERAMENT_CHOICES, null=True, blank=True)
    animalGender = models.CharField(max_length=255, choices=ANIMAL_GENDER_CHOICES, null=True, blank=True)
    animalPregnant = models.CharField(max_length=255, choices=ANIMAL_PREGNANT_CHOICES, null=True, blank=True)
    animalMarking = models.CharField(max_length=255, null=True, blank=True)
    animalColor = models.CharField(max_length=255, null=True, blank=True)
    animalCatchable = models.CharField(max_length=255, choices=ANIMAL_CATCHABLE_CHOICES, null=True, blank=True)
    animalWeight = models.CharField(max_length=255, null=True, blank=True)
    admissionReason = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.animalSpecies} - {self.animalAge}"

class AnimalPictures(models.Model):
    animal_linked = models.ForeignKey(AnimalDetail, on_delete=models.CASCADE, related_name="animalPictures")
    animalPictures = models.ImageField(upload_to='animal_images/', null=True, blank=True)
    animal_picture_upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.animal_linked.animalSpecies} - {self.animal_linked.animalAge}"
    

class MedicalDetail(models.Model):
    MEDICAL_STATUS_CHOICES = (
        ('Already Done', 'Already Done'),
        ('To be done in NGO', 'To be done in NGO'),
        ('Not Done', 'Not Done'),
        ('Unsure', 'Unsure'),
    )

    FIT_FOR_SURGERY_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Unsure', 'Unsure'),
    )

    case_linked = models.OneToOneField(Case, on_delete=models.CASCADE)
    medicalHistory = models.CharField(max_length=255, null=True, blank=True)
    vaccinationStatus = models.CharField(max_length=20, choices=MEDICAL_STATUS_CHOICES, null=True, blank=True)
    dewormed = models.CharField(max_length=20, choices=MEDICAL_STATUS_CHOICES, null=True, blank=True)
    fitForSurgery = models.CharField(max_length=10, choices=FIT_FOR_SURGERY_CHOICES, null=True, blank=True)
    otherDetails = models.CharField(max_length=255, null=True, blank=True)
    admissionDate = models.DateField(null=True, blank=True)
    bloodReportImage = models.ImageField(upload_to='medical_detail/blood_repoort/', null=True, blank=True)

    def __str__(self):
        return f"{self.vaccinationStatus} - {self.case_linked}"
    
class FeedingRecordImage(models.Model):
    medical_linked = models.ForeignKey(MedicalDetail, on_delete=models.CASCADE, related_name="feedingRecordImage")
    feedingRecordImage = models.ImageField(upload_to='medical_detail/feeding_record/', null=True, blank=True)
    feeding_record_image_upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.medical_linked.medicalHistory}"


class OperationDetail(models.Model):
    VET_OUTCOMES = [
        ('Success', 'Success'),
        ('Failure', 'Failure'),
        ('Complicated', 'Complicated'),
    ]
    
    case_linked = models.OneToOneField(Case, on_delete=models.CASCADE)
    vetName = models.CharField(max_length=255, null=True, blank=True)
    operationDate = models.DateField(null=True, blank=True)
    operationStartTime = models.TimeField(null=True, blank=True)
    operationEndTime = models.TimeField(null=True, blank=True)
    operationOutcome = models.CharField(max_length=20, choices=VET_OUTCOMES, null=True, blank=True)
    medicalPrescriptionImage = models.ImageField(upload_to='operational_detail/prescription/', null=True, blank=True)

    def __str__(self):
        return f"OperationDetail - Case ID: {self.case_linked}"

class TreatmentRecordImage(models.Model):
    operation_linked = models.ForeignKey(OperationDetail, on_delete=models.CASCADE, related_name="treatmentRecordImage")
    treatmentRecordImage = models.ImageField(upload_to='operational_detail/treatment_record/', null=True, blank=True)
    treatment_record_image_upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.operation_linked.vetName}"

class OrganImage(models.Model):
    operation_linked = models.ForeignKey(OperationDetail, on_delete=models.CASCADE, related_name="organImage")
    organImage = models.ImageField(upload_to='operational_detail/organ_image/', null=True, blank=True)
    organ_image_upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.operation_linked.vetName}"
    

class PostOperationDetail(models.Model):
    POP_FACILITY_CHOICES = [
        ('In Shelter', 'In Shelter'),
        ('Not in shelter', 'Not in shelter'),
        ('On Street', 'On Street'),
        ('Other', 'Other'),
    ]

    POP_EUTHANIZED_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    case_linked = models.OneToOneField(Case, on_delete=models.CASCADE)
    popComment = models.TextField(null=True, blank=True)
    popFacility = models.CharField(max_length=20, choices=POP_FACILITY_CHOICES, null=True, blank=True)
    popExpectedDays = models.CharField(max_length=255, null=True, blank=True)
    popStartDate = models.DateField(null=True, blank=True)
    popEndDate = models.DateField(null=True, blank=True)
    releaseDate = models.DateField(null=True, blank=True)
    euthanized = models.CharField(max_length=10, choices=POP_EUTHANIZED_CHOICES, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"PostOperationDetail - ID: {self.case_linked}"
    
class PopPictures(models.Model):
    post_operation_linked = models.ForeignKey(PostOperationDetail, on_delete=models.CASCADE, related_name="popPictures")
    popPictures = models.ImageField(upload_to='post_operation_detail/picture/', null=True, blank=True)
    pop_pictures_upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.post_operation_linked.popFacility}"
    
class ReleasePictures(models.Model):
    post_operation_linked = models.ForeignKey(PostOperationDetail, on_delete=models.CASCADE, related_name="releasePictures")
    releasePictures = models.ImageField(upload_to='post_operation_detail/release_picture/', null=True, blank=True)
    release_pictures_upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.post_operation_linked.popFacility}"