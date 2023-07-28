from django.db import models
from django.contrib.auth.models import User
from professor.models import PeriodoDisc


# Create your models here.
"""class UserPeriodo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    periodo_disc = models.ForeignKey(PeriodoDisc, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User periodo'
        verbose_name_plural = 'Users e periodos'
        ordering = ['id']

    # Retorna apenas o nome do Plano
    def __str__(self):
        return self.periodo_disc"""


class Plano(models.Model):
    titulo = models.CharField('Titulo', max_length=150)
    resumo = models.TextField('Resumo', blank=False, null=True)
    objetivo = models.TextField('Objetivo', blank=False, null=True)
    obj_especifico = models.TextField('Objetivo especifico', blank=False, null=True)
    motivacao = models.TextField('Motivação', blank=False, null=True)
    status = models.CharField('Status', max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planos')
    user_orientador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='planos_orientados')
    periodo = models.ForeignKey(PeriodoDisc, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'
        ordering = ['id']

    # Retorna apenas o nome do Plano
    def __str__(self):
        return self.titulo

