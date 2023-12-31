# Generated by Django 4.2.3 on 2023-07-16 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_management', '0005_alter_postoperationdetail_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='mortality_of_case',
            field=models.CharField(choices=[('Healthy', 'Healthy'), ('Unhealthy', 'Unhealthy'), ('Fatal', 'Fatal')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='status_of_case',
            field=models.CharField(choices=[('Reported', 'Reported'), ('Admitted', 'Admitted'), ('Blood Test', 'Blood Test'), ('Operation', 'Operation'), ('Post Operation', 'Post Operation'), ('Released', 'Released')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='type_of_case',
            field=models.CharField(choices=[('Vaccination', 'Vaccination'), ('Sterilization', 'Sterilization'), ('OPD', 'OPD'), ('IPD', 'IPD')], max_length=255, null=True),
        ),
    ]
