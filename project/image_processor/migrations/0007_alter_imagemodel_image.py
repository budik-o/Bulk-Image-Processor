# Generated by Django 5.0.2 on 2024-03-12 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_processor', '0006_imagemodel_modificationmodel_delete_processedimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(upload_to='results/'),
        ),
    ]