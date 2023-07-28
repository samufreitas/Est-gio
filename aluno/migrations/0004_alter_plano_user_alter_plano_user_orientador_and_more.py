# Generated by Django 4.2.3 on 2023-07-28 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('professor', '0004_delete_plano'),
        ('aluno', '0003_plano_user_orientador_alter_plano_user_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plano',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='plano',
            name='user_orientador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Orientador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='plano',
            name='user_periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professor.periododisc'),
        ),
    ]
