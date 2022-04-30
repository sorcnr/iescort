from django.db import models

class Eskort(models.Model):
    id = models.AutoField(primary_key=True)
    isim = models.TextField()
    tel = models.CharField( max_length=20)
    aciklama = models.TextField()