from django.shortcuts import render, redirect
from django.contrib import messages
from aluno.models import Plano, Trabalho
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
# Create your views here.
def is_orientador(user):
    return user.groups.filter(name='Orientador').exists()

@login_required(login_url='/contas/login/')
@user_passes_test(is_orientador)
def pag_orientador(request):
    return render(request, 'orientador/base_orientador.html')


@login_required(login_url='/contas/login/')
@user_passes_test(is_orientador)
def list_plano_ori(request, status1=None):
    template_name = 'list_planos_ori.html'
    query = request.GET.get('query')
    status = request.GET.get('status')
    consulta = Plano.objects.filter(user_orientador=request.user).exclude(status='Versão aprovada')
    if query:
        consulta = consulta.filter(Q(tema__icontains=query) | Q(user__last_name__icontains=query) | Q(user__first_name__icontains=query))
    if status:
        consulta = consulta.filter(status=status)
    if status1:
        consulta = consulta.filter(status=status1)
    paginator = Paginator(consulta, 6)

    page_number = request.GET.get("page")
    planos = paginator.get_page(page_number)
    context = {
        'planos': planos,
        'filtro_status': status1,
        'status': status,
        'query': query,
    }
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
@user_passes_test(is_orientador)
def corrigi_plano_ori(request, plano_id):
    try:
        plano = Plano.objects.get(id=plano_id)
        if plano.status != "Revisado":
            plano.status = 'Revisado'
            plano.save()
            messages.success(request, "Plano revisado com sucesso!")
        else:
            messages.error(request, "Esse plano já foi revisado!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('orientador:list_plano_ori')

@login_required(login_url='/contas/login/')
@user_passes_test(is_orientador)
def cancelar_plano_ori(request, plano_id):
    try:
        plano = Plano.objects.get(id=plano_id)
        if plano.status == "Revisado":
            plano.status = 'Enviado'
            plano.save()
            messages.success(request, "Ação realizada com sucesso!")
        else:
            messages.error(request, "Essa ação ja foi realizada!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('orientador:list_plano_ori')

@login_required(login_url='/contas/login/')
@user_passes_test(is_orientador)
def list_trabalho_ori(request, status1=None):
    template_name = 'list_trabalho_ori.html'
    query = request.GET.get('query')
    status = request.GET.get('status')
    consulta = Trabalho.objects.filter(orientador=request.user).exclude(status='Versão aprovada')
    if query:
        consulta = consulta.filter(Q(titulo__icontains=query) | Q(user__last_name__icontains=query) | Q(user__first_name__icontains=query))
    if status:
        consulta = consulta.filter(status=status)
    if status1:
        consulta = consulta.filter(status=status1)
    paginator = Paginator(consulta, 6)

    page_number = request.GET.get("page")
    trabalhos = paginator.get_page(page_number)
    context = {
        'trabalhos': trabalhos,
        'filtro_status': status1,
        'status': status,
        'query': query,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
@user_passes_test(is_orientador)
def corrigi_trabalho_ori(request, trabalho_id):
    try:
        trabalho = Trabalho.objects.get(id=trabalho_id)
        if trabalho.status != "Revisado":
            trabalho.status = 'Revisado'
            trabalho.save()
            messages.success(request, "Trabalho revisado com sucesso!")
        else:
            messages.error(request, "Essa ação ja foi realizada!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('orientador:list_trabalho_ori')

@login_required(login_url='/contas/login/')
@user_passes_test(is_orientador)
def cancelar_trab_ori(request, trabalho_id):
    try:
        trabalho = Trabalho.objects.get(id=trabalho_id)
        if trabalho.status == "Revisado":
            trabalho.status = 'Enviado'
            trabalho.save()
            messages.success(request, "Ação realizada com sucesso!")
        else:
            messages.error(request, "Essa ação ja foi realizada!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('orientador:list_trabalho_ori')

