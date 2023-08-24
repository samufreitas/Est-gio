from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User

from .forms import UserForm
# Create your views here.

def add_user(request):
    template_name = 'add_user.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
            form.save_m2m()
            messages.success(request, 'Usuário salvo com sucesso!')
    form = UserForm()
    context['form'] = form
    return render(request, template_name, context)


def user_new_password(request):
    template_name = 'user_new_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Senha alterada com sucesso!")
            update_session_auth_hash(request, form.user)
            if form.user.groups.filter(name='Aluno').exists():
                return redirect('aluno:list_plano')
            elif form.user.groups.filter(name='Professor').exists():
                return redirect('professor:pag_professor')
            elif form.user.groups.filter(name='Orientador').exists():
                return redirect('orientador:pag_orientador')
        else:
            messages.error(request, "Não foi possível trocar sua senha!")
    form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)



def user_login(request):
    template_name = 'user_login.html'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user.last_login is None:
            if user is not None:
                login(request, user)
                return redirect('accounts:user_new_password')
        if user is not None:
            login(request, user)
            if user.groups.filter(name='Aluno').exists():
                return redirect('aluno:add_plano')
            elif user.groups.filter(name='Professor').exists():
                return redirect('professor:pag_professor')
            elif user.groups.filter(name='Orientador').exists():
                return redirect('orientador:pag_orientador')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    return render(request, template_name, {})

# accounts/views.py
