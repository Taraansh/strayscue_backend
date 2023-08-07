# Generated by Django 4.2.3 on 2023-08-06 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case_management', '0030_remove_medicaldetail_feedingrecordimage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operationdetail',
            name='organImage',
        ),
        migrations.RemoveField(
            model_name='operationdetail',
            name='treatmentRecordImage',
        ),
        migrations.RemoveField(
            model_name='postoperationdetail',
            name='popPictures',
        ),
        migrations.RemoveField(
            model_name='postoperationdetail',
            name='releasePictures',
        ),
        migrations.CreateModel(
            name='TreatmentRecordImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatmentRecordImage', models.ImageField(blank=True, null=True, upload_to='operational_detail/treatment_record/')),
                ('treatment_record_image_upload_date', models.DateField(auto_now_add=True)),
                ('operation_linked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treatmentRecordImage', to='case_management.operationdetail')),
            ],
        ),
        migrations.CreateModel(
            name='ReleasePictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('releasePictures', models.ImageField(blank=True, null=True, upload_to='post_operation_detail/release_picture/')),
                ('release_pictures_upload_date', models.DateField(auto_now_add=True)),
                ('post_operation_linked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releasePictures', to='case_management.postoperationdetail')),
            ],
        ),
        migrations.CreateModel(
            name='PopPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popPictures', models.ImageField(blank=True, null=True, upload_to='post_operation_detail/picture/')),
                ('pop_pictures_upload_date', models.DateField(auto_now_add=True)),
                ('post_operation_linked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='popPictures', to='case_management.postoperationdetail')),
            ],
        ),
        migrations.CreateModel(
            name='OrganImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organImage', models.ImageField(blank=True, null=True, upload_to='operational_detail/organ_image/')),
                ('organ_image_upload_date', models.DateField(auto_now_add=True)),
                ('operation_linked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organImage', to='case_management.operationdetail')),
            ],
        ),
    ]