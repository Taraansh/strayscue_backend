# Generated by Django 4.2.3 on 2023-08-03 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case_management', '0027_remove_animaldetail_animalpictures_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalPictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animalPictures', models.ImageField(blank=True, null=True, upload_to='animal_images/')),
                ('animal_linked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animalPictures', to='case_management.animaldetail')),
            ],
        ),
    ]
