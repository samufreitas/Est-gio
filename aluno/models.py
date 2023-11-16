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
    tema = models.CharField('Tema', max_length=150)
    resumo = models.TextField('Resumo', blank=False, null=True)
    objetivo = models.TextField('Objetivo', blank=False, null=True)
    obj_especifico = models.TextField('Objetivo especifico', blank=False, null=True)
    motivacao = models.TextField('Motivação', blank=False, null=True)
    status = models.CharField('Status', max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_aluno')
    user_orientador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orientados')
    periodo = models.ForeignKey(PeriodoDisc, on_delete=models.CASCADE)
    arquivo = models.FileField(upload_to='plano_pdf')

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'
        ordering = ['id']

    # Retorna apenas o nome do Plano
    def __str__(self):
        return self.tema

class Trabalho(models.Model):
    titulo = models.CharField('Titulo', max_length=60)
    orientador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Orientador')
    prof1 = models.CharField('Professor1', max_length=60)
    prof2 = models.CharField('Professor2', max_length=60)
    prof3 = models.CharField('Professor3', max_length=60, blank=False, null=True)
    data = models.DateField()
    resumo = models.TextField('Resumo')  # blank= não obrigatorio/null=aceita valor nulo
    palavras_ch = models.CharField('Palavras chaves', max_length=60)
    periodo = models.ForeignKey(PeriodoDisc, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='Autor')
    arquivo = models.FileField('Arquivo', upload_to="Trabalhos/")
    status = models.CharField('Status', max_length=150)
    class Meta:
        verbose_name = 'Trabalho'
        verbose_name_plural = 'Trabalhos'
        ordering = ['id']

    # Retorna o nome da categoria
    def __str__(self):
        return self.titulo


