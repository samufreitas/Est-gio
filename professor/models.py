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
    descricao = models.CharField('Descrição', max_length=150)

    class Meta:
        verbose_name = 'Período'
        verbose_name_plural = 'Período'
        ordering = ['id']

    # Retorna o nome da categoria
    def __str__(self):
        return self.descricao


class PeriodoDisc(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)  # Atributo de chave estrageira
    periodo = models.ForeignKey(Periodo, on_delete=models.RESTRICT)  # Atributo de chave estrageira

    class Meta:
        verbose_name = 'Periodo_Disciplina'
        verbose_name_plural = 'Periodos_Disciplinas'
        ordering = ['id']

    # Retorna o nome da categoria
    def __str__(self):
        return f'{self.disciplina.nome} do {self.periodo.descricao}'




class Trabalho(models.Model):
    titulo = models.CharField('Titulo', max_length=60)
    autor = models.CharField('Autor', max_length=60)
    orientador = models.CharField('Orientador', max_length=60)
    data = models.DateField()
    banca = models.CharField('Banca', max_length=150)
    resumo = models.TextField('Resumo', blank=False, null=True)  # blank= não obrigatorio/null=aceita valor nulo
    palavras_ch = models.CharField('Palavras chaves', max_length=60)
    arquivo = models.FileField('Arquivo', upload_to="media/Trabalhos/")

    class Meta:
        verbose_name = 'Trabalho'
        verbose_name_plural = 'Trabalhos'
        ordering = ['id']

    # Retorna o nome da categoria
    def __str__(self):
        return self.titulo
