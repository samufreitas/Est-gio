from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PlanoForm, TrabalhoForm
from .models import Plano, Trabalho
from django.core.paginator import Paginator


# Create your views here.
def add_plano(request):
    template_name = 'planos_form.html'
    context = {}
    if request.method == 'POST':
        form = PlanoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.status = 'Em andamento'
            f.save()
            messages.success(request, 'Plano salvo com sucesso!')
            return redirect('aluno:list_plano')
    else:
        form = PlanoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_plano(request):
    template_name = 'list_planos.html'
    # filter pega o usuário que está logado
    consulta = Plano.objects.all()#filter(user=request.user)
    paginator = Paginator(consulta, 2)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    planos = paginator.get_page(page_number)
    context = {
        'planos': planos
    }
    return render(request, template_name, context)

def add_trabalho(request):
    template_name = 'trabalho_form.html'
    context = {}
    if request.method == 'POST':
        form = TrabalhoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, 'Trabalho salvo com sucesso!')
            return redirect('aluno:list_trabalho')
        else:
           print('erro')
    else:
        form = TrabalhoForm() # No caso do usuário querer apenas visualizar e não submeter nada
    context['form'] = form # form contém os dados de todos os campos do formulário preenchido pelo usuário
    return render(request, template_name, context)

def list_trabalho(request):
    template_name = 'list_trabalho.html'
    # filter pega o usuário que está logado
    trabalhos = Trabalho.objects.all()
    context = {
        'trabalhos': trabalhos
    }
    return render(request, template_name, context)