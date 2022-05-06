from django.contrib import admin 
from .models import Eskort, Image

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


