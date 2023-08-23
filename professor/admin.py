from django.contrib import admin
from .models import Periodo, Disciplina, PeriodoDisc
# Register your models here.
class Periododmin(admin.ModelAdmin):
    list_display = ['descricao',]

class PeriodoDiscdmin(admin.ModelAdmin):
    list_display = ['disciplina', 'periodo']

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome',]






admin.site.register(Periodo, Periododmin) # Chama a classe CategoryAdmin para exibir seus atributos
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(PeriodoDisc, PeriodoDiscdmin)
