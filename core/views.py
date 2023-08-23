from django.shortcuts import render

# Create your views here.
def template_list(request):
    return render(request, "aluno/base_aluno.html")