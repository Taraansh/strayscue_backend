# Generated by Django 4.2.3 on 2023-08-11 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0012_alter_profile_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_active',
            field=models.CharField(choices=[('Active', 'Active'), ('Not Active', 'Not Active')], max_length=15),
        ),
    ]
