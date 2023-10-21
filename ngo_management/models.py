from django.db import models
from authorization.models import Profile

class Ngo(models.Model):
    id = models.AutoField(primary_key=True)
    ngo_name = models.CharField(max_length=255, null=False)
    darpan_id = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    mission_statement = models.CharField(max_length=255, null=True, blank=True)
    helpline_number = models.CharField(max_length=255, null=True, blank=True)
    alternate_helpline_number = models.CharField(max_length=255, null=True, blank=True)
    facebook_page = models.CharField(max_length=255, null=True, blank=True)
    linkedin_page = models.CharField(max_length=255, null=True, blank=True)
    instagram_page = models.CharField(max_length=255, null=True, blank=True)
    twitter_page = models.CharField(max_length=255, null=True, blank=True)
    ngo_email = models.CharField(max_length=255, null=True, blank=True)
    ngo_website = models.CharField(max_length=255, null=True, blank=True)
    ngo_address = models.CharField(max_length=255, null=True, blank=True, default='')
    offline_cases = models.IntegerField(null=True, blank=True, default=0)
    ngo_logo = models.ImageField(upload_to='ngo/', null=True, blank=True)
    ngo_profile_creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ngos', null=True, blank=True)

    def __str__(self):
        return f"{self.ngo_name} - {self.darpan_id}"