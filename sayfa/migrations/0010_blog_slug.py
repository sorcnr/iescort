# Generated by Django 4.0.4 on 2022-05-13 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayfa', '0009_alter_eskort_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Slug'),
        ),
    ]
