# Generated by Django 4.2.3 on 2023-07-14 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter_management', '0003_reporter_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reporter',
            old_name='user',
            new_name='reporter_profile_creator',
        ),
    ]
