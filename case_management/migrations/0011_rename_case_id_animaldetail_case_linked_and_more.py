# Generated by Django 4.2.3 on 2023-07-17 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case_management', '0010_remove_animaldetail_animalpicturesurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animaldetail',
            old_name='case_id',
            new_name='case_linked',
        ),
        migrations.RenameField(
            model_name='medicaldetail',
            old_name='case_id',
            new_name='case_linked',
        ),
        migrations.RenameField(
            model_name='operationdetail',
            old_name='case_id',
            new_name='case_linked',
        ),
        migrations.RenameField(
            model_name='postoperationdetail',
            old_name='case_id',
            new_name='case_linked',
        ),
        migrations.RemoveField(
            model_name='medicaldetail',
            name='bloodReportImageURL',
        ),
        migrations.RemoveField(
            model_name='medicaldetail',
            name='feedingRecordImageURL',
        ),
        migrations.RemoveField(
            model_name='operationdetail',
            name='medicalPrescriptionImageURL',
        ),
        migrations.RemoveField(
            model_name='operationdetail',
            name='organImageURL',
        ),
        migrations.RemoveField(
            model_name='operationdetail',
            name='treatmentRecordImageURL',
        ),
        migrations.RemoveField(
            model_name='postoperationdetail',
            name='popPicturesURL',
        ),
        migrations.RemoveField(
            model_name='postoperationdetail',
            name='releasePicturesURL',
        ),
    ]