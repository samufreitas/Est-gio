from django.contrib import admin
from .models import Periodo, Disciplina, PeriodoDisc, Plano, Trabalho
# Register your models here.
class Periododmin(admin.ModelAdmin):
    list_display = ['descricao',]

class PeriodoDiscdmin(admin.ModelAdmin):
    list_display = ['disciplina', 'periodo']

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome',]

class PlanoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'resumo', 'objetivo', 'obj_especifico', 'motivacao', 'status', 'user']

class TrabalhoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'orientador', 'data', 'banca', 'resumo', 'palavras_ch', 'arquivo']


admin.site.register(Periodo, Periododmin) # Chama a classe CategoryAdmin para exibir seus atributos
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(PeriodoDisc, PeriodoDiscdmin)
admin.site.register(Plano, PlanoAdmin)
admin.site.register(Trabalho, TrabalhoAdmin)