# Generated by Django 4.2.3 on 2023-07-18 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0003_rename_user_name_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_contact',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
