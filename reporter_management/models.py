from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from authorization.models import Profile


class Reporter(models.Model):
    reported_name = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=20, null=False)
    alternate_phone_number = models.CharField(max_length=20, null=True, blank=True)
    email_id = models.EmailField(null=True, blank=True)
    verification_id = models.ImageField(upload_to='reporter_ids/', null=True, blank=True)
    verification_id_url = models.URLField(blank=True, default='')
    reporter_profile_creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reporters', null=True, blank=True)

    def __str__(self):
        return self.reported_name


@receiver(post_save, sender=Reporter)
def update_image_url(sender, instance, created, **kwargs):
    if created and instance.verification_id:
        instance.verification_id_url = f"{settings.MEDIA_URL}{instance.verification_id}"
        instance.save()
