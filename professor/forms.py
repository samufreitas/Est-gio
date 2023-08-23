from django import forms
from django.contrib.auth.models import User, Group
from .models import Periodo, PeriodoDisc


class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ['descricao', ]

class PeriodoDiscForm(forms.ModelForm):
    class Meta:
        model = PeriodoDisc
        fields = ['disciplina', 'periodo']


