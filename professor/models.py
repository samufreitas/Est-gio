from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Disciplina(models.Model):
    nome = models.CharField('Nome', max_length=60)
    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
        ordering = ['id']

    # Retorna o nome da categoria
    def __str__(self):
        return self.nome


class Periodo(models.Model):
    descricao = models.CharField('Descrição', max_length=150, unique=True)

    class Meta:
        verbose_name = 'Período'
        verbose_name_plural = 'Período'
        ordering = ['id']

    # Retorna o nome da categoria
    def __str__(self):
        return self.descricao


class PeriodoDisc(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = 'Periodo_Disciplina'
        verbose_name_plural = 'Periodos_Disciplinas'
        ordering = ['id']

    # Retorna o nome da categoria
    def __str__(self):
        return f'{self.disciplina.nome} {self.periodo.descricao}'




