# Generated by Django 4.2.3 on 2023-08-23 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0016_plano_arquivo_trabalho_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabalho',
            name='prof3',
            field=models.CharField(max_length=60, null=True, verbose_name='Professor3'),
        ),
    ]
