from django.contrib import admin
from .models import Eskort

class EskortAdmin(admin.ModelAdmin):
    pass

admin.site.register(Eskort,EskortAdmin)
