from django.shortcuts import render
from django.contrib import messages
from .forms import PeriodoForm, PeriodoDiscForm
# Create your views here.

def add_periodo(request):
    template_name = 'periodo_form.html'
    context = {}
    if request.method == 'POST':
        form = PeriodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Período salvo com sucesso!')
        else:
           print('Erro')
    form = PeriodoForm() # No caso do usuário querer apenas visualizar e não submeter nada
    context['form'] = form # form contém os dados de todos os campos do formulário preenchido pelo usuário
    return render(request, template_name, context)

def add_periodo_disc(request):
    template_name = 'periodo_disc_form.html'
    context = {}
    if request.method == 'POST':
        form = PeriodoDiscForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Período salvo com sucesso!')
        else:
           print('Erro')
    form = PeriodoDiscForm() # No caso do usuário querer apenas visualizar e não submeter nada
    context['form'] = form # form contém os dados de todos os campos do formulário preenchido pelo usuário
    return render(request, template_name, context)
