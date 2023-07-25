# Generated by Django 4.2.3 on 2023-07-25 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_management', '0018_alter_reportingdetail_landmark_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportingdetail',
            name='landmark',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reportingdetail',
            name='location',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reportingdetail',
            name='pincode',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reportingdetail',
            name='reporterContact',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reportingdetail',
            name='reporterName',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
