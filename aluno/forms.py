from django import forms
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
import re
from .models import Plano, Trabalho


class PlanoForm(forms.ModelForm):
    user_orientador = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='Orientador'),
        label='Orientador',
        empty_label='Selecione um orientador',
        to_field_name='first_name'  # Use 'username' ou outro campo único do modelo User
    )

    class Meta:
        model = Plano
        fields = ['titulo', 'resumo', 'objetivo', 'obj_especifico', 'motivacao', 'user_orientador', 'periodo']

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get("titulo")
        resumo = cleaned_data.get("resumo")
        objetivo = cleaned_data.get("objetivo")
        obj_especifico = cleaned_data.get("obj_especifico")
        motivacao = cleaned_data.get("motivacao")
        user_orientador = cleaned_data.get("user_orientador")
        periodo = cleaned_data.get("periodo")

        if not titulo:
            raise ValidationError("Campo obrigatório.")
        if re.match(r'^[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', titulo):
            raise ValidationError('O título não pode conter apenas números ou caracteres especiais.')

        if not resumo:
            raise ValidationError("Campo obrigatório.")
        if re.match(r'^[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', resumo):
            raise ValidationError('O resumo não pode conter apenas números ou caracteres especiais.')

        if not objetivo:
            raise ValidationError("Campo obrigatório.")
        if re.match(r'^[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', objetivo):
            raise ValidationError('O objetivo não pode conter apenas números ou caracteres especiais.')

        if not obj_especifico:
            raise ValidationError("Campo obrigatório.")
        if re.match(r'^[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', obj_especifico):
            raise ValidationError('O objetivo específico não pode conter apenas números ou caracteres especiais.')

        if not motivacao:
            raise ValidationError("Campo obrigatório.")
        if re.match(r'^[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', motivacao):
            raise ValidationError('A motivação não pode conter apenas números ou caracteres especiais.')

        if not user_orientador:
            raise ValidationError("Campo obrigatório.")

        if not periodo:
            raise ValidationError("Campo obrigatório.")




class TrabalhoForm(forms.ModelForm):
    orientador = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='Orientador'),
        label='Orientador',
        empty_label='Selecione um orientador',
        to_field_name='first_name'  # Use 'username' ou outro campo único do modelo User
    )
    class Meta:
        model = Trabalho
        fields = ['titulo', 'orientador', 'prof1', 'prof2', 'prof3', 'data', 'resumo', 'palavras_ch', 'periodo', 'arquivo']



