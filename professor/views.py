from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PeriodoForm, PeriodoDiscForm
from aluno.models import Plano, Trabalho
from django.core.paginator import Paginator
# Create your views here.

def pag_professor(request):
    return render(request, 'professor/base_professor.html')
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


def list_plano_pro(request):
    template_name = 'list_planos_pro.html'
    consulta = Plano.objects.all()
    paginator = Paginator(consulta, 10)

    page_number = request.GET.get("page")
    planos = paginator.get_page(page_number)
    context = {
        'planos': planos
    }
    return render(request, template_name, context)

def aprovar_plano(request, plano_id):
    try:
        plano = Plano.objects.get(id=plano_id)
        if plano.status != "Aprovado":
            plano.status = 'Aprovado'
            plano.save()
            messages.success(request, "Plano corrigido com sucesso!")
        else:
            messages.error(request, "Esse plano já foi corrigido!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('professor:list_plano_pro')


def cancelar_plano_pro(request, plano_id):
    try:
        plano = Plano.objects.get(id=plano_id)
        if plano.status != "Aprovado":
            plano.status = 'Corrigido'
            plano.save()
            messages.success(request, "Ação realizada com sucesso!")
        else:
            messages.error(request, "Essa ação ja foi realizada!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('professor:list_plano_pro')


def list_trabalho_pro(request):
    template_name = 'list_trabalho_pro.html'
    consulta = Trabalho.objects.all()
    paginator = Paginator(consulta, 3)

    page_number = request.GET.get("page")
    trabalhos = paginator.get_page(page_number)
    context = {
        'trabalhos': trabalhos
    }
    return render(request, template_name, context)

def aprovar_trabalho(request, trabalho_id):
    try:
        trabalho = Trabalho.objects.get(id=trabalho_id)
        if trabalho.status != "Aprovado":
            trabalho.status = 'Aprovado'
            trabalho.save()
            messages.success(request, "Ação realizada com sucesso!")
        else:
            messages.error(request, "Esse trabalho já foi aprovado!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('professor:list_trabalho_pro')

def cancelar_trab_pro(request, trabalho_id):
    try:
        trabalho = Trabalho.objects.get(id=trabalho_id)
        if trabalho.status == "Aprovado":
            trabalho.status = 'Corrigido'
            trabalho.save()
            messages.success(request, "Trabalho cancelado com sucesso!")
        else:
            messages.error(request, "Essa ação ja foi realizada!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('professor:list_trabalho_pro')

