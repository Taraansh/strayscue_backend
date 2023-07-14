from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Sponsor(models.Model):
    SPONSOR_CHOICES = [
        ('vaccination', 'Vaccination'),
        ('sterilization', 'Sterilization'),
        ('OPD', 'OPD'),
        ('IPD', 'IPD'),
        ('adoption', 'Adoption'),
        ('post_op_care', 'Post Op Care'),
        ('other', 'Other'),
    ]

    sponsor_name = models.CharField(max_length=255, null=False)
    animal_fit_for_surgery = models.CharField(max_length=255, choices=SPONSOR_CHOICES, null=True)
    sponsor_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    sponsor_logo = models.ImageField(upload_to='sponsor_logos/', null=True, blank=True)
    sponsor_logo_url = models.URLField(blank=True, default='')

    def __str__(self):
        return self.sponsor_name


@receiver(post_save, sender=Sponsor)
def update_image_url(sender, instance, created, **kwargs):
    if created and instance.sponsor_logo:
        instance.sponsor_logo_url = f"{settings.MEDIA_URL}{instance.sponsor_logo}"
        instance.save()
