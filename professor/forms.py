from django import forms
from django.contrib.auth.models import User, Group
from .models import Periodo, PeriodoDisc
from django.core.exceptions import ValidationError
import re

class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ['descricao', ]

    def clean(self):
        cleaned_data = super().clean()
        descricao = cleaned_data.get("descricao")

        if not descricao:
            raise ValidationError("Campo obrigatório.")
        if re.match(r'^[a-z A-Z!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', descricao):
            raise forms.ValidationError('A descrição não pode conter apenas letras ou caracteres especial!')
        if Periodo.objects.filter(descricao__iexact=descricao).exists():
            raise forms.ValidationError('Já existe um período com essa mesma descrição!')
class PeriodoDiscForm(forms.ModelForm):
    class Meta:
        model = PeriodoDisc
        fields = ['disciplina', 'periodo']


