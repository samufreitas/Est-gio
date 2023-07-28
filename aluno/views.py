from django.shortcuts import render
from django.contrib import messages
from .forms import PlanoForm
from .models import Plano
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
    form = PlanoForm() # No caso do usuário querer apenas visualizar e não submeter nada
    context['form'] = form # form contém os dados de todos os campos do formulário preenchido pelo usuário
    return render(request, template_name, context)

def list_plano(request):
    template_name = 'list_planos.html'
    # filter pega o usuário que está logado
    planos = Plano.objects.filter(user=request.user)
    context = {
        'planos': planos
    }
    return render(request, template_name, context)