# Generated by Django 4.2.3 on 2023-08-28 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ngo_management', '0004_alter_ngo_id'),
        ('case_management', '0033_remove_operationdetail_medicalprescriptionimage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='ngo_linked_with_this_case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ngo_management.ngo'),
        ),
    ]