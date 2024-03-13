# Generated by Django 5.0.2 on 2024-03-09 17:00

import image_processor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_processor', '0002_alter_processedimage_modified_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processedimage',
            name='modified_image',
            field=models.ImageField(blank=True, null=True, upload_to='results/'),
        ),
        migrations.AlterField(
            model_name='processedimage',
            name='original_image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
