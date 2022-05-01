from random import choices
from django.db import models
import json

from django.urls import reverse

# Create your models here.
class Eskort(models.Model):
    class Rank(models.IntegerChoices):
        GOLD = 1
        SILVER = 2
        BRONZE = 3
    class Status(models.IntegerChoices):
        ACIK = 1
        KAPALI = 0
    
    name = models.TextField()
    tel = models.CharField(max_length=20)
    text = models.TextField()
    imgs = models.CharField(max_length=100)
    rank = models.IntegerField(choices= Rank.choices)
    status = models.IntegerField(choices=Status.choices,default=0)
    img1 = models.ImageField( null=True, upload_to ='esc-img/')
    img2 = models.ImageField( null=True, upload_to ='esc-img/')
    img3 = models.ImageField( null=True, upload_to ='esc-img/')

    

    def get_absolute_url(self):
        return reverse("escort_view",kwargs={"id":self.id})
    
    
        
    