# Generated by Django 4.2.3 on 2023-07-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reported_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('alternate_phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email_id', models.EmailField(blank=True, max_length=254, null=True)),
                ('verification_id', models.ImageField(blank=True, null=True, upload_to='verification_ids/')),
                ('verification_id_url', models.URLField(blank=True, default='')),
            ],
        ),
    ]
