from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PlanoForm, TrabalhoForm
from .models import Plano, Trabalho
from django.core.paginator import Paginator
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django.template.defaultfilters import linebreaks
import pdfkit

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

            # Formatar o campo motivacao com linebreaks e estilos
            f.motivacao = linebreaks(f.motivacao)
            context['plano'] = f

            # Renderizar o template HTML para obter o conteúdo formatado
            rendered_html = render_to_string('pdf_template.html', context)

            # Configurar as opções de PDF, como tamanho da página, etc.
            pdf_options = {
                'page-size': 'A4',
                'encoding': 'UTF-8',
            }

            # Gerar o PDF usando o pacote pdfkit
            pdf_data = pdfkit.from_string(rendered_html, False, options=pdf_options)

            # Salvar o PDF no campo 'arquivo'
            f.arquivo.save(f'plano_{f.tema}.pdf', ContentFile(pdf_data), save=False)
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