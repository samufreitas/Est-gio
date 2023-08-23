from django import forms
from django.contrib.auth.models import User, Group

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email' ,'groups', 'password']


    def __str__(self):
        return f'{self.cleaned_data["first_name"]} {self.cleaned_data["last_name"]}'