from django.contrib import admin
from .models import Plano, Trabalho
# Register your models here.

class PlanoAdmin(admin.ModelAdmin):
    list_display = ['tema', 'resumo', 'objetivo', 'obj_especifico', 'motivacao', 'status', 'user']

admin.site.register(Plano, PlanoAdmin)

class TrabalhoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'user', 'orientador', 'data', 'resumo', 'palavras_ch', 'periodo', ]

admin.site.register(Trabalho, TrabalhoAdmin)