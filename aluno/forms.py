from django import forms
from django.contrib.auth.models import User, Group
from .models import Plano


class PlanoForm(forms.ModelForm):
    user_orientador = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='Orientador'),
                                             label='Orientador')

    class Meta:
        model = Plano
        fields = ['titulo', 'resumo', 'objetivo', 'obj_especifico', 'motivacao', 'periodo', 'user_orientador']


