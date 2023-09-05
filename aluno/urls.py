from django.urls import path

from . import views

app_name = 'aluno'

urlpatterns = [
    path('pag_aluno', views.pag_aluno, name='pag_aluno'),
    path('add_plano/', views.add_plano, name='add_plano'),
    path('list_plano/', views.list_plano, name='list_plano'),
    path('listar_planos/<str:status>/', views.list_plano, name='listar_planos_status'),
    path('excluir_plano/<int:plano_id>/delete/', views.excluir_plano, name='excluir_plano'),

    path('add_trabalho/', views.add_trabalho, name='add_trabalho'),
    path('list_trabalho/', views.list_trabalho, name='list_trabalho'),
    path('listar_trabalho/<str:status>/', views.list_trabalho, name='listar_trabalho_status'),
    path('excluir_trabalho/<int:trabalho_id>/delete/', views.excluir_trabalho, name='excluir_trabalho'),


]