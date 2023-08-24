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

    def clean(self):
        cleaned_data = super().clean()
        disciplina = cleaned_data.get("disciplina")
        periodo = cleaned_data.get("periodo")

        if not disciplina:
            raise ValidationError("Campo obrigatório.")
        if not periodo:
            raise ValidationError("Campo obrigatório.")

        semestre = PeriodoDisc.objects.filter(disciplina=disciplina, periodo=periodo).exclude(
            pk=self.instance.pk)
        if semestre.exists():
            raise ValidationError("Já existe esse período!")
