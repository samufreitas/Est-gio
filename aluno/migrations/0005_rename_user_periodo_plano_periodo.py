# Generated by Django 4.2.3 on 2023-07-28 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0004_alter_plano_user_alter_plano_user_orientador_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plano',
            old_name='user_periodo',
            new_name='periodo',
        ),
    ]
