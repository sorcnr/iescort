from atexit import register
from cgitb import text
import string
from typing import List
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Eskort
import random
from faker import Faker
from faker.providers import ssn, phone_number,person


# Create your views here.
def index_view(request, *args, **kwargs):
    esc = Eskort.objects.all().order_by('rank')
    for es in esc:
        print(es.name)
        
    return render(request,'index.html',{'esc':esc})
def escort_view(request, id):
    esc = Eskort.objects.filter(id=id)
    escAll = Eskort.objects.all().order_by('rank')[:2]
    return render(request,'escort.html',{'esc':esc,'escAll':escAll})