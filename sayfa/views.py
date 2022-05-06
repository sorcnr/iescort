from atexit import register
from cgitb import text


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Eskort



# Create your views here.
def index_view(request, *args, **kwargs):
    escg = Eskort.objects.filter(rank=1).all()
    escs = Eskort.objects.filter(rank=2).all()
    escb = Eskort.objects.filter(rank=3).all()
        
    return render(request,'index.html',{'escg':escg,'escs':escs,'escb':escb})
def escort_view(request, id):
    esc = Eskort.objects.filter(id=id).first()
    images = esc.images.all()
    
    text = esc.text.rstrip('\"')
    escAll = Eskort.objects.all().order_by('rank')[:4]
    return render(request,'escort.html',{'e':esc,'escAll':escAll, 'images': images, 'text': text})