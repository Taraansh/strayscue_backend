# Generated by Django 4.2.3 on 2024-02-25 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ngo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ngo_name', models.CharField(max_length=255)),
                ('darpan_id', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('mission_statement', models.CharField(blank=True, max_length=255, null=True)),
                ('helpline_number', models.CharField(blank=True, max_length=255, null=True)),
                ('alternate_helpline_number', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_page', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_page', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_page', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_page', models.CharField(blank=True, max_length=255, null=True)),
                ('ngo_email', models.CharField(blank=True, max_length=255, null=True)),
                ('ngo_website', models.CharField(blank=True, max_length=255, null=True)),
                ('ngo_address', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('offline_cases', models.IntegerField(blank=True, default=0, null=True)),
                ('ngo_logo', models.ImageField(blank=True, null=True, upload_to='ngo/')),
                ('ngo_profile_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ngos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
