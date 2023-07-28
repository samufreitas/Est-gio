from django.urls import path

from . import views

app_name = 'aluno'

urlpatterns = [
    path('add_plano/', views.add_plano, name='add_plano'),
    path('list_plano/', views.list_plano, name='list_plano'),


]