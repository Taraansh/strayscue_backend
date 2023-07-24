from django.db import models
from authorization.models import Profile


class Reporter(models.Model):
    reported_name = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    alternate_phone_number = models.CharField(max_length=20, null=True, blank=True)
    email_id = models.EmailField(null=True, blank=True)
    verification_id = models.ImageField(upload_to='reporter_ids/', null=True, blank=True)
    reporter_profile_creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reporters', null=True, blank=True)

    def __str__(self):
        return self.reported_name
    