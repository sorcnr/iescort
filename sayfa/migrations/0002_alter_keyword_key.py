# Generated by Django 4.0.4 on 2022-05-09 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sayfa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyword',
            name='key',
            field=models.CharField(choices=[('Buca Escort', 'Buca Escort'), ('İzmir Buca Escort', 'Izmir Buca Escort'), ('Buca Escort Bayanlar', 'Buca Escort Bayanlar'), ('Buca Escort Bayan', 'Buca Escort Bayan'), ('Bornova Escort', 'Bornova Escort'), ('İzmir Bornova Escort', 'Izmir Bornova Escort'), ('Alsancak Escort', 'Alsancak Escort'), ('İzmir Alsancak Escort', 'Izmir Alsancak Escort'), ('İzmir Escort', 'Izmir Escort'), ('İzmir Escort Bayanlar', 'Izmir Escort Bayanlar'), ('İzmir Escort Bayan', 'Izmir Escort Bayan')], max_length=50, verbose_name='Keyword'),
        ),
    ]
