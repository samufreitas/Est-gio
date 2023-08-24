from django.shortcuts import render, redirect
from django.contrib import messages
from aluno.models import Plano, Trabalho
from django.core.paginator import Paginator

# Create your views here.
def pag_orientador(request):
    return render(request, 'orientador/base_orientador.html')

def list_plano_ori(request):
    template_name = 'list_planos_ori.html'
    consulta = Plano.objects.filter(user_orientador=request.user).exclude(status='Aprovado')
    paginator = Paginator(consulta, 10)

    page_number = request.GET.get("page")
    planos = paginator.get_page(page_number)
    context = {
        'planos': planos
    }
    return render(request, template_name, context)

def corrigi_plano_ori(request, plano_id):
    try:
        plano = Plano.objects.get(id=plano_id)
        if plano.status != "Corrigido":
            plano.status = 'Corrigido'
            plano.save()
            messages.success(request, "Plano corrigido com sucesso!")
        else:
            messages.error(request, "Esse plano já foi corrigido!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('orientador:list_plano_ori')


def cancelar_plano_ori(request, plano_id):
    try:
        plano = Plano.objects.get(id=plano_id)
        if plano.status == "Corrigido":
            plano.status = 'Enviado'
            plano.save()
            messages.success(request, "Ação realizada com sucesso!")
        else:
            messages.error(request, "Essa ação ja foi realizada!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('orientador:list_plano_ori')


def list_trabalho_ori(request):
    template_name = 'list_trabalho_ori.html'
    consulta = Trabalho.objects.filter(orientador=request.user).exclude(status='Aprovado')
    paginator = Paginator(consulta, 3)

    page_number = request.GET.get("page")
    trabalhos = paginator.get_page(page_number)
    context = {
        'trabalhos': trabalhos
    }
    return render(request, template_name, context)

def corrigi_trabalho_ori(request, trabalho_id):
    try:
        trabalho = Trabalho.objects.get(id=trabalho_id)
        if trabalho.status != "Corrigido":
            trabalho.status = 'Corrigido'
            trabalho.save()
            messages.success(request, "Trabalho corrigido com sucesso!")
        else:
            messages.error(request, "Essa ação ja foi realizada!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('orientador:list_trabalho_ori')

def cancelar_trab_ori(request, trabalho_id):
    try:
        trabalho = Trabalho.objects.get(id=trabalho_id)
        if trabalho.status == "Corrigido":
            trabalho.status = 'Aprovado'
            trabalho.save()
            messages.success(request, "Ação realizada com sucesso!")
        else:
            messages.error(request, "Essa ação ja foi realizada!")
    except Plano.DoesNotExist:
        messages.error(request, "Solicitação não encontrado.")

    return redirect('orientador:list_trabalho_ori')

