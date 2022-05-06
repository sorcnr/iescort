from atexit import register
from cgitb import text


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Eskort



# Create your views here.
def index_view(request, *args, **kwargs):
    esc = Eskort.objects.all().order_by('rank')
    for es in esc:
        print(dir(es.images))
        
    return render(request,'index.html',{'esc':esc})
def escort_view(request, id):
    esc = Eskort.objects.filter(id=id).first()
    images = esc.images.all()
    
    
    escAll = Eskort.objects.all().order_by('rank')[:2]
    return render(request,'escort.html',{'e':esc,'escAll':escAll, 'images': images})