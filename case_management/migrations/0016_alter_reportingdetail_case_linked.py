# Generated by Django 4.2.3 on 2023-07-20 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case_management', '0015_alter_reportingdetail_case_linked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportingdetail',
            name='case_linked',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='case_management.case'),
        ),
    ]