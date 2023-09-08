from django import forms
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
import re
from .models import Plano, Trabalho
from professor.models import PeriodoDisc


class PlanoForm(forms.ModelForm):
    user_orientador = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='Orientador'),
        label='Orientador',
        empty_label='Selecione seu orientador',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    periodo = forms.ModelChoiceField(
        queryset=PeriodoDisc.objects.all(),
        label='periodo',
        empty_label='Selecione seu periodo',
    )
    def __init__(self, *args, **kwargs):
        super(PlanoForm, self).__init__(*args, **kwargs)
        self.fields['user_orientador'].label_from_instance = self.get_user_full_name

    def get_user_full_name(self, user):
        return user.get_full_name()

    class Meta:
        model = Plano
        fields = ['tema', 'resumo', 'objetivo', 'obj_especifico', 'motivacao', 'user_orientador', 'periodo']

    def clean(self):
        cleaned_data = super().clean()
        tema = cleaned_data.get("tema")
        resumo = cleaned_data.get("resumo")
        objetivo = cleaned_data.get("objetivo")
        obj_especifico = cleaned_data.get("obj_especifico")
        motivacao = cleaned_data.get("motivacao")
        user_orientador = cleaned_data.get("user_orientador")
        periodo = cleaned_data.get("periodo")

        if not tema:
            raise ValidationError("Campo obrigatório.")
        if re.match(r'^[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', tema):
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
        empty_label='Selecione seu orientador',
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    periodo = forms.ModelChoiceField(
        queryset=PeriodoDisc.objects.all(),
        label='periodo',
        empty_label='Selecione seu periodo',
    )
    def __init__(self, *args, **kwargs):
        super(TrabalhoForm, self).__init__(*args, **kwargs)
        self.fields['orientador'].label_from_instance = self.get_user_full_name
        self.fields['prof3'].required = False

    def get_user_full_name(self, user):
        return user.get_full_name()

    class Meta:
        model = Trabalho
        fields = ['titulo', 'orientador', 'prof1', 'prof2', 'prof3', 'data', 'resumo', 'palavras_ch', 'periodo', 'arquivo']

    def clean(self):
        cleaned_data = super().clean()
        titulo = cleaned_data.get("titulo")
        orientador = cleaned_data.get("orientador")
        prof1 = cleaned_data.get("prof1")
        prof2 = cleaned_data.get("prof2")
        data = cleaned_data.get("data")
        resumo = cleaned_data.get("resumo")
        palavras_ch = cleaned_data.get("palavras_ch")
        periodo = cleaned_data.get("periodo")
        arquivo = cleaned_data.get("arquivo")

        if not titulo:
            raise ValidationError("Campo titulo é obrigatório.")
        if re.match(r'^[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', titulo):
            raise ValidationError('O título não pode conter apenas números ou caracteres especiais.')

        if not resumo:
            raise ValidationError("Campo resumo é obrigatório.")
        if re.match(r'^[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', resumo):
            raise ValidationError('O resumo não pode conter apenas números ou caracteres especiais.')

        if not orientador:
            raise ValidationError("Campo orientador é obrigatório.")

        if not prof1:
            raise ValidationError("Campo professor 1 é obrigatório.")
        if re.match(r'^[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', prof1):
            raise ValidationError('O campo professor 1 não pode conter apenas números ou caracteres especiais.')

        if not prof2:
            raise ValidationError("Campo professor 2 é obrigatório.")
        if re.match(r'^[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', prof2):
            raise ValidationError('O campo professor 2 não pode conter apenas números ou caracteres especiais.')

        if not data:
            raise ValidationError("Campo data é obrigatório.")

        if not palavras_ch:
            raise ValidationError("Campo palavras chaves é obrigatório.")
        if re.match(r'^[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', palavras_ch):
            raise ValidationError('O campo das palavras chaves não pode conter apenas números ou caracteres especiais.')

        if not periodo:
            raise ValidationError("Campo período é obrigatório.")

        if not arquivo:
            raise ValidationError("Campo arquivo é obrigatório.")
        if not arquivo.name.endswith('.pdf'):
            raise ValidationError('Apenas arquivos PDF são permitidos.')
