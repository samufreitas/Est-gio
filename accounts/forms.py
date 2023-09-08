from django import forms
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import re
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'groups', 'password']
    def __str__(self):
        return f'{self.cleaned_data["first_name"]} {self.cleaned_data["last_name"]}'
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        groups = cleaned_data.get("groups")
        password = cleaned_data.get("password")

        if not first_name:
            raise ValidationError("Campo nome é obrigatório.")
        if re.match(r'^[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', first_name):
            raise forms.ValidationError('A nome não pode conter apenas números ou caracteres especial!')
        if not last_name:
            raise ValidationError("Campo sobrenome é obrigatório.")
        if re.match(r'^[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', last_name):
            raise forms.ValidationError('A sobrenome não pode conter apenas números ou caracteres especial!')
        if not username:
            raise ValidationError("Campo matrícula é obrigatório.")
        if re.match(r'^[a-z A-Z!@#$%^&*()_+{}\[\]:;<>,.?~\\/\\\'"\\-]*$', username):
            raise forms.ValidationError('A matrícula não pode conter apenas letras ou caracteres especial!')
        if len(username) < 10:
            raise ValidationError("A sua matrícula deve conter no mínimo 10 números")

        if not email:
            raise ValidationError("Campo obrigatório.")
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Insira um endereço de email válido.")
        if not password:
            raise ValidationError("Campo senha é obrigatório.")
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Alguém está usando essa matrícula! Se não for você procure a Coordenação do Curso o quanto antes!")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Alguém já está cadastrado com esse Emial! Se não for você em um cadastro anterior, procure a Coordenação do Curso o quanto antes!")