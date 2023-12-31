# Generated by Django 4.2.3 on 2023-07-14 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sponsor_management', '0002_alter_sponsor_sponsor_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='sponsor_profile_creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sponsors', to=settings.AUTH_USER_MODEL),
        ),
    ]
