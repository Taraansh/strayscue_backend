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
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_name', models.CharField(max_length=255)),
                ('animal_fit_for_surgery', models.CharField(choices=[('Vaccination', 'Vaccination'), ('Sterilization', 'Sterilization'), ('OPD', 'OPD'), ('IPD', 'IPD'), ('Adoption', 'Adoption'), ('Post Op Care', 'Post Op Care'), ('Other', 'Other')], max_length=255, null=True)),
                ('sponsor_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('sponsor_logo', models.ImageField(blank=True, null=True, upload_to='sponsor_logos/')),
                ('sponsor_profile_creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sponsors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
