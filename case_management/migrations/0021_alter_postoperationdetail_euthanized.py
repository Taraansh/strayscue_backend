# Generated by Django 4.2.3 on 2023-07-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_management', '0020_alter_reportingdetail_landmark_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postoperationdetail',
            name='euthanized',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], null=True),
        ),
    ]
