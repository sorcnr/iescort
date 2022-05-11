from ast import keyword
from django.contrib import admin 
from .models import BlogImage, Eskort, Image, Blog, KeyWord
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe


class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f'<a href="{image_url}" target="_blank">'
                f'<img src="{image_url}" alt="{file_name}" width="150" height="150" '
                f'style="object-fit: cover;"/> </a>')

        output.append(super(AdminFileWidget, self).render(
            name, value, attrs, renderer))
        return mark_safe(u''.join(output))

class EskortInline(admin.TabularInline):
    model = Image
    extra = 3
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }
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
class BlogImageInline(admin.TabularInline):
    model = BlogImage
    formfield_overrides = {models.ImageField: {'widget': AdminImageWidget}}

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    inlines = [BlogInline,BlogImageInline,]
admin.site.register(Blog, BlogAdmin)

