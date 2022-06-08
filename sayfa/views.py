from atexit import register
from cgitb import text


from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Eskort,Blog

#keyword dictionary for query slugs
keyDict = {
    "buca-escort" : "Buca Escort",
    "izmir-buca-escort" : "İzmir Buca Escort",
    "buca-escort-bayanlar" : "Buca Escort Bayanlar",
    "buca-escort-bayan" : "Buca Escort Bayan",
    "bornova-escort" : "Bornova Escort",
    "izmir-bornova-escort" : "İzmir Bornova Escort",
    "alsancak-escort" : "Alsancak Escort",
    "izmir-alsancak-escort" : "İzmir Alsancak Escort",
    "izmir-escort" : "İzmir Escort",
    "izmir-escort-bayanlar" : "İzmir Escort Bayanlar",
    "izmir-escort-bayan" : "İzmir Escort Bayan", 
}



# Create your views here.
def index_view(request, *args, **kwargs):
    escg = Eskort.objects.filter(rank=1).all()
    escs = Eskort.objects.filter(rank=2).all()
    escb = Eskort.objects.filter(rank=3).all()
    
    blogs = Blog.objects.all()
    
    context = {'blogs': blogs, 'escg': escg,
               'escs': escs, 'escb': escb, 'request': request}
    return render(request,'index.html',context)

def blog_view(request, *args, **kwargs):
    blog = Blog.objects.filter(slug=kwargs.get('slug')).first()
    keywords = blog.keywords.all()
    context = {'blog':blog, 'keywords':keywords}
    
    return render(request,'blog.html',context)

def blog_keyword_view(request, *args, **kwargs):
    blogs = Blog.objects.filter(
        keywords__key=keyDict[kwargs.get('slug')]).all()
    context = {'blogs': blogs, }
    return render(request, 'blog.html', context)

def escort_view(request, *args, **kwargs):
    esc = Eskort.objects.filter(slug=kwargs.get('slug')).first()
    images = esc.images.all()
    
    text = esc.text.rstrip('\"')
    escAll = Eskort.objects.all().order_by('rank')[:4]
    return render(request,'escort.html',{'e':esc,'escAll':escAll, 'images': images, 'text': text})