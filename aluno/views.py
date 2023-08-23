from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PlanoForm, TrabalhoForm
from .models import Plano, Trabalho
from django.core.paginator import Paginator
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template.defaultfilters import linebreaks

# Create your views here.


def add_plano(request):
    template_name = 'planos_form.html'
    context = {}
    if request.method == 'POST':
        form = PlanoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.status = 'Enviado'
            f.motivacao = linebreaks(f.motivacao)
            # Renderizar o template HTML com os dados do formulário
            template = get_template('pdf_template.html')
            context = {'plano': f}
            html = template.render(context)

            # Gerar PDF a partir do HTML renderizado
            pdf_buffer = BytesIO()
            pisa.CreatePDF(html, dest=pdf_buffer)

            # Salvar o PDF no campo 'arquivo'
            f.arquivo.save(f'plano_{f.user.get_full_name}.pdf', ContentFile(pdf_buffer.getvalue()), save=False)
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
    paginator = Paginator(consulta, 5)  # Show 25 contacts per page.

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
            f.status = 'Em andamento'
            f.save()
            messages.success(request, 'Trabalho salvo com sucesso!')
            return redirect('aluno:list_trabalho')
        else:
           print('erro')
    else:
        form = TrabalhoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_trabalho(request):
    template_name = 'list_trabalho.html'
    # filter pega o usuário que está logado
    trabalhos = Trabalho.objects.all()
    context = {
        'trabalhos': trabalhos
    }
    return render(request, template_name, context)