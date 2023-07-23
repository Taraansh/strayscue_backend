from django.db import models
from authorization.models import Profile


class Sponsor(models.Model):
    SPONSOR_CHOICES = [
        ('Vaccination', 'Vaccination'),
        ('Sterilization', 'Sterilization'),
        ('OPD', 'OPD'),
        ('IPD', 'IPD'),
        ('Adoption', 'Adoption'),
        ('Post Op Care', 'Post Op Care'),
        ('Other', 'Other'),
    ]

    sponsor_name = models.CharField(max_length=255, null=False)
    animal_fit_for_surgery = models.CharField(max_length=255, choices=SPONSOR_CHOICES, null=True)
    sponsor_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    sponsor_logo = models.ImageField(upload_to='sponsor_logos/', null=True, blank=True)
    sponsor_profile_creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sponsors', null=True, blank=True)


    def __str__(self):
        return self.sponsor_name
