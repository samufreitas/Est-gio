# Generated by Django 4.2.3 on 2023-08-08 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('professor', '0005_delete_trabalho'),
        ('aluno', '0007_trabalho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trabalho',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='trabalho',
            name='banca',
        ),
        migrations.AddField(
            model_name='trabalho',
            name='periodo',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.RESTRICT, to='professor.periododisc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trabalho',
            name='prof1',
            field=models.CharField(blank=True, max_length=60, verbose_name='Professor1'),
        ),
        migrations.AddField(
            model_name='trabalho',
            name='prof2',
            field=models.CharField(blank=True, max_length=60, verbose_name='Professor2'),
        ),
        migrations.AddField(
            model_name='trabalho',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='Autor', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trabalho',
            name='arquivo',
            field=models.FileField(upload_to='Trabalhos/', verbose_name='Arquivo'),
        ),
    ]
