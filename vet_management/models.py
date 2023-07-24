from django.db import models
from authorization.models import Profile


class Vet(models.Model):
    vet_name = models.CharField(max_length=255, null=False)
    registration_id = models.CharField(max_length=255, null=False)
    vet_certification = models.ImageField(upload_to='vet/vet_certifications/', null=True, blank=True)
    verification_id = models.ImageField(upload_to='vet/verification_ids/', null=True, blank=True)
    vet_profile_creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='vets', null=True, blank=True)

    def __str__(self):
        return self.vet_name
