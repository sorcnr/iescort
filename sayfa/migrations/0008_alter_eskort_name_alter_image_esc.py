# Generated by Django 4.0.4 on 2022-05-04 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sayfa', '0007_remove_eskort_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eskort',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='esc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='sayfa.eskort'),
        ),
    ]