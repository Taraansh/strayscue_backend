# Generated by Django 4.2.3 on 2023-07-17 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case_management', '0008_rename_id_of_case_reportingdetail_case_linked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reportingdetail',
            name='backImageURL',
        ),
        migrations.RemoveField(
            model_name='reportingdetail',
            name='consentFormImageURL',
        ),
        migrations.RemoveField(
            model_name='reportingdetail',
            name='frontImageURL',
        ),
    ]