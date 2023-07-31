# Generated by Django 4.2.3 on 2023-07-29 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_management', '0024_remove_animaldetail_animalpictures_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animaldetail',
            name='animalPictures',
            field=models.FileField(blank=True, null=True, upload_to='animal_images/'),
        ),
        migrations.AddField(
            model_name='animaldetail',
            name='animalPictures02',
            field=models.ImageField(blank=True, null=True, upload_to='animal_images/'),
        ),
        migrations.AddField(
            model_name='animaldetail',
            name='animalPictures03',
            field=models.ImageField(blank=True, null=True, upload_to='animal_images/'),
        ),
        migrations.AddField(
            model_name='animaldetail',
            name='animalPictures04',
            field=models.ImageField(blank=True, null=True, upload_to='animal_images/'),
        ),
        migrations.AddField(
            model_name='animaldetail',
            name='animalPictures05',
            field=models.ImageField(blank=True, null=True, upload_to='animal_images/'),
        ),
        migrations.DeleteModel(
            name='AnimalPictures',
        ),
    ]
