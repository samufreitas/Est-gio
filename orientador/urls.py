from django.urls import path

from . import views

app_name = 'orientador'

urlpatterns = [
    path('', views.pag_orientador, name='pag_orientador'),
    path('list_plano_ori/', views.list_plano_ori, name='list_plano_ori'),
    path('listar_plano_pro/<str:status>/', views.list_plano_ori, name='list_plano_ori_status'),
    path('corrigi_plano/<int:plano_id>/corrigi/', views.corrigi_plano_ori, name='corrigi_plano_ori'),
    path('cancelar_ori/<int:plano_id>/cancelar/', views.cancelar_plano_ori, name='cancelar_plano_ori'),

    path('list_trabalho_ori/', views.list_trabalho_ori, name='list_trabalho_ori'),
    path('listar_plano_pro/<str:status>/', views.list_trabalho_ori, name='list_trabalho_ori_status'),
    path('corrigi_trabalho/<int:trabalho_id>/corrigi/', views.corrigi_trabalho_ori, name='corrigi_trabalho_ori'),
    path('cancelar_ori/<int:trabalho_id>/cancelar/', views.cancelar_trab_ori, name='cancelar_trab_ori'),

]