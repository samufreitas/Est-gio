from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PeriodoForm, PeriodoDiscForm
from aluno.models import Plano, Trabalho
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q

# Create your views here.
def is_professor(user):
    return user.groups.filter(name='Professor').exists()

@login_required(login_url='/contas/login/')
@user_passes_test(is_professor)
def pag_professor(request):
    return render(request, 'pag_inicio_pro.html')

@login_required(login_url='/contas/login/')
@user_passes_test(is_professor)
def add_periodo(request):
    template_name = 'periodo_form.html'
    context = {}
    if request.method == 'POST':
        form = PeriodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Período salvo com sucesso!')
    else:
        form = PeriodoForm()
    context['form'] = form # form contém os dados de todos os campos do formulário preenchido pelo usuário
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
@user_passes_test(is_professor)
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
    else:
        form = PeriodoDiscForm()
    context['form'] = form # form contém os dados de todos os campos do formulário preenchido pelo usuário
    return render(request, template_name, context)

"""@login_required(login_url='/contas/login/')
@user_passes_test(is_professor)"""
def list_plano_pro(request, status2=None):
    template_name = 'list_planos_pro.html'
    query = request.GET.get('query')
    status = request.GET.get('status')
    consulta = Plano.objects.all().exclude(status='Enviado')
    if query:
        consulta = consulta.filter(
            Q(user_orientador__last_name__icontains=query) |
            Q(user_orientador__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(periodo__periodo__descricao__icontains=query) |
            Q(periodo__disciplina__nome__icontains=query))
    if status:
        consulta = consulta.filter(status=status)
    if status2:
        consulta = consulta.filter(status=status2)
    paginator = Paginator(consulta, 6)

    page_number = request.GET.get("page")
    planos = paginator.get_page(page_number)
    context = {
        'planos': planos,
        'filtro_status': status2,
        'status': status,
        'query': query,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
@user_passes_test(is_professor)
def aprovar_plano(request, plano_id):
    try:
        plano = Plano.objects.get(id=plano_id)
        if plano.status != "Versão aprovada":
            plano.status = 'Versão aprovada'
            plano.save()
            messages.success(request, "Plano aprovado com sucesso!")
        else:
            messages.error(request, "Esse plano já foi corrigido!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('professor:list_plano_pro')


@login_required(login_url='/contas/login/')
@user_passes_test(is_professor)
def cancelar_plano_pro(request, plano_id):
    try:
        plano = Plano.objects.get(id=plano_id)
        if plano.status == "Versão aprovada":
            plano.status = 'Revisado'
            plano.save()
            messages.success(request, "Ação realizada com sucesso!")
        else:
            messages.error(request, "Essa ação ja foi realizada!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('professor:list_plano_pro')

"""@login_required(login_url='/contas/login/')
@user_passes_test(is_professor)"""
def list_trabalho_pro(request, status2=None):
    template_name = 'list_trabalho_pro.html'
    query = request.GET.get('query')
    status = request.GET.get('status')
    consulta = Trabalho.objects.all().exclude(status='Enviado')
    if query:
        consulta = consulta.filter(
            Q(orientador__last_name__icontains=query) |
            Q(orientador__first_name__icontains=query) |
            Q(user__last_name__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(periodo__periodo__descricao__icontains=query) |
            Q(periodo__disciplina__nome__icontains=query))
    if status:
        consulta = consulta.filter(status=status)
    if status2:
        consulta = consulta.filter(status=status2)
    paginator = Paginator(consulta, 6)

    page_number = request.GET.get("page")
    trabalhos = paginator.get_page(page_number)
    context = {
        'trabalhos': trabalhos,
        'filtro_status': status2,
        'status': status,
        'query': query,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
@user_passes_test(is_professor)
def aprovar_trabalho(request, trabalho_id):
    try:
        trabalho = Trabalho.objects.get(id=trabalho_id)
        if trabalho.status != "Versão aprovada":
            trabalho.status = 'Versão aprovada'
            trabalho.save()
            messages.success(request, "Ação realizada com sucesso!")
        else:
            messages.error(request, "Esse trabalho já foi aprovado!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('professor:list_trabalho_pro')

@login_required(login_url='/contas/login/')
@user_passes_test(is_professor)
def cancelar_trab_pro(request, trabalho_id):
    try:
        trabalho = Trabalho.objects.get(id=trabalho_id)
        if trabalho.status == "Versão aprovada":
            trabalho.status = 'Revisado'
            trabalho.save()
            messages.success(request, "Ação realizada com sucesso!")
        else:
            messages.error(request, "Essa ação ja foi realizada!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('professor:list_trabalho_pro')

