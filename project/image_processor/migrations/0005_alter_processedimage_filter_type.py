# Generated by Django 5.0.2 on 2024-03-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_processor', '0004_alter_processedimage_filter_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processedimage',
            name='filter_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]