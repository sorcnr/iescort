# Generated by Django 4.0.4 on 2022-05-11 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayfa', '0003_blogimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='eskort',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield'),
        ),
    ]