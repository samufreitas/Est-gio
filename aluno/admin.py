from django.contrib import admin
from .models import Plano
# Register your models here.

class PlanoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'resumo', 'objetivo', 'obj_especifico', 'motivacao', 'status', 'user']

admin.site.register(Plano, PlanoAdmin)