# Generated by Django 4.2.3 on 2024-02-25 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ngo_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='ngo_profile_creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ngos', to=settings.AUTH_USER_MODEL),
        ),
    ]