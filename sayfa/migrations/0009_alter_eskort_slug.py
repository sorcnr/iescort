# Generated by Django 4.0.4 on 2022-05-11 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayfa', '0008_alter_eskort_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eskort',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
