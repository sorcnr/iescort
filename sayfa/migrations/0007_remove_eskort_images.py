# Generated by Django 4.0.4 on 2022-05-03 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sayfa', '0006_remove_eskort_imgs_eskort_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eskort',
            name='images',
        ),
    ]