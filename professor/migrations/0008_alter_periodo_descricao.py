# Generated by Django 4.2.3 on 2023-08-08 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0007_alter_periodo_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='descricao',
            field=models.CharField(max_length=150, unique=True, verbose_name='Descrição'),
        ),
    ]
