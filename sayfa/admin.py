from ast import keyword
from django.contrib import admin 
from .models import Eskort, Image, Blog, KeyWord

from django.contrib.auth.decorators import login_required

class EskortInline(admin.TabularInline):
    model = Image
    extra = 3
class EskortAdmin(admin.ModelAdmin):
    list_display = ('name','tel','rank','active')
    def active(self,obj):
        return obj.status == 1
    active.boolean = True
    inlines = [EskortInline,]

admin.site.register(Eskort,EskortAdmin)

class BlogInline(admin.TabularInline):
    model = KeyWord
    extra = 3
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    inlines = [BlogInline,]
admin.site.register(Blog, BlogAdmin)

