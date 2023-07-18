from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from authorization.models import Profile


class Vet(models.Model):
    vet_name = models.CharField(max_length=255, null=False)
    registration_id = models.CharField(max_length=255, null=False)
    vet_certification = models.ImageField(upload_to='vet_certifications/', null=True, blank=True)
    vet_certification_url = models.URLField(blank=True, default='')
    verification_id = models.ImageField(upload_to='verification_ids/', null=True, blank=True)
    verification_id_url = models.URLField(blank=True, default='')
    vet_profile_creator = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='vets', null=True, blank=True)

    def __str__(self):
        return self.vet_name


@receiver(post_save, sender=Vet)
def update_image_urls(sender, instance, created, **kwargs):
    if created and instance.vet_certification:
        instance.vet_certification_url = f"{settings.MEDIA_URL}{instance.vet_certification}"
    if created and instance.verification_id:
        instance.verification_id_url = f"{settings.MEDIA_URL}{instance.verification_id}"
    Vet.objects.filter(id=instance.id).update(
        vet_certification_url=instance.vet_certification_url,
        verification_id_url=instance.verification_id_url
    )
