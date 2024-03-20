from django.contrib import admin
from .models import Utilisateur

class liste(admin.ModelAdmin):
    list_display=('username','last_name')
    
admin.site.register(Utilisateur,liste)
