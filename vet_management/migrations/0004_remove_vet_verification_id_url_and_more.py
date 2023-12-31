# Generated by Django 4.2.3 on 2023-07-23 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vet_management', '0003_vet_vet_profile_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vet',
            name='verification_id_url',
        ),
        migrations.RemoveField(
            model_name='vet',
            name='vet_certification_url',
        ),
        migrations.AlterField(
            model_name='vet',
            name='verification_id',
            field=models.ImageField(blank=True, null=True, upload_to='vet/verification_ids/'),
        ),
        migrations.AlterField(
            model_name='vet',
            name='vet_certification',
            field=models.ImageField(blank=True, null=True, upload_to='vet/vet_certifications/'),
        ),
    ]
