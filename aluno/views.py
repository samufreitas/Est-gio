from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PlanoForm, TrabalhoForm
from .models import Plano, Trabalho
from django.core.paginator import Paginator
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime
import locale
from django.db.models import Q


# Create your views here.

def is_aluno(user):
    return user.groups.filter(name='Aluno').exists()

"""@login_required(login_url='/contas/login/')
@user_passes_test(is_aluno)"""
def pag_aluno(request):
    return render(request, 'aluno/base_aluno.html')


"""@login_required(login_url='/contas/login/')
@user_passes_test(is_aluno)"""
def add_plano(request):
    template_name = 'planos_form.html'
    context = {}
    if request.method == 'POST':
        form = PlanoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.tema = f.tema.capitalize()
            f.status = 'Enviado'

            # Renderizar o template HTML com os dados do formulário
            template = get_template('pdf_template.html')

            locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
            data = datetime.now().date()


            data_formatada = data
            context = {'plano': f,
                       'data': data_formatada
                       }
            html = template.render(context)

            # Gerar PDF a partir do HTML renderizado
            pdf_buffer = BytesIO()
            pisa.CreatePDF(html, dest=pdf_buffer)

            # Salvar o PDF no campo 'arquivo'
            f.arquivo.save(f'plano_{f.tema}.pdf', ContentFile(pdf_buffer.getvalue()), save=False)
            f.save()

            messages.success(request, 'Plano salvo com sucesso!')
            return redirect('aluno:list_plano')
    else:
        form = PlanoForm()
    context['form'] = form
    return render(request, template_name, context)


"""@login_required(login_url='/contas/login/')
@user_passes_test(is_aluno)"""
def list_plano(request, status=None):
    template_name = 'list_planos.html'
    # filter pega o usuário que está logado
    consulta = Plano.objects.filter(user=request.user)
    if status:
        consulta = consulta.filter(status=status)

    paginator = Paginator(consulta, 6)
    page_number = request.GET.get("page")
    planos = paginator.get_page(page_number)
    context = {
        'planos': planos,
        'filtro_status': status,
    }
    return render(request, template_name, context)


"""@login_required(login_url='/contas/login/')
@user_passes_test(is_aluno)"""
def add_trabalho(request):
    template_name = 'trabalho_form.html'
    context = {}
    if request.method == 'POST':
        form = TrabalhoForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.titulo = f.titulo.capitalize()
            f.status = 'Enviado'
            f.save()
            messages.success(request, 'Trabalho salvo com sucesso!')
            return redirect('aluno:list_trabalho')
        else:
           print('erro')
    else:
        form = TrabalhoForm()
    context['form'] = form
    return render(request, template_name, context)


"""@login_required(login_url='/contas/login/')
@user_passes_test(is_aluno)"""
def list_trabalho(request, status=None):
    template_name = 'list_trabalho.html'
    # filter pega o usuário que está logado

    consulta = Trabalho.objects.filter(user=request.user)
    if status:
        consulta = consulta.filter(status=status)
    paginator = Paginator(consulta, 6)

    page_number = request.GET.get("page")
    trabalhos = paginator.get_page(page_number)
    context = {
        'trabalhos': trabalhos,
        'filtro_status': status
    }
    return render(request, template_name, context)


@login_required(login_url='/contas/login/')
@user_passes_test(is_aluno)
def excluir_plano(request, plano_id):
    try:
        plano = Plano.objects.get(id=plano_id)
        if plano.status == 'Enviado':
            plano.delete()
            messages.success(request, "Plano excluído com sucesso!")
        else:
            messages.error(request, 'Esse plano não pode ser mais excluído pois já foi corrido pelo orientador!')
    except Plano.DoesNotExist:
        messages.error(request, "Plano não encontrado.")
    return redirect('aluno:list_plano')

@login_required(login_url='/contas/login/')
@user_passes_test(is_aluno)
def excluir_trabalho(request, trabalho_id):
    try:
        trabalho = Trabalho.objects.get(id=trabalho_id)
        if trabalho.status == 'Enviado':
            trabalho.delete()
            messages.success(request, "Trabalho excluído com sucesso!")
        else:
            messages.error(request, 'Esse trabalho não pode ser mais excluído pois já foi corrido pelo orientador!')
    except Plano.DoesNotExist:
        messages.error(request, "Trabalho não encontrado.")
    return redirect('aluno:list_trabalho')

