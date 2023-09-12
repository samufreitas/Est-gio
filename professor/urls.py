from django.urls import path

from . import views

app_name = 'professor'

urlpatterns = [
    path('', views.pag_professor, name='pag_professor'),
    path('add_periodo/', views.add_periodo, name='add_periodo'),
    path('list_periodo/', views.list_periodo, name='list_periodo'),
    path('editar_periodo/editar/<int:id_periodo>/', views.edit_periodo, name='edit_periodo'),
    path('excluir_periodo/<int:periodo_id>/delete/', views.excluir_periodo, name='excluir_periodo'),

    path('add_periodo_disc/', views.add_periodo_disc, name='add_periodo_disc'),
    path('list_periodo_disc/', views.list_periodo_disc, name='list_periodo_disc'),
    path('editar_semestre/editar/<int:id_periodo_disc>/', views.edit_periodo_disc, name='edit_periodo_disc'),
    path('excluir_semestre/<int:id_periodo_disc>/delete/', views.excluir_periodo_disc, name='excluir_periodo_disc'),

    path('list_plano_pro/', views.list_plano_pro, name='list_plano_pro'),
    path('listar_plano_pro/<str:status2>/', views.list_plano_pro, name='list_plano_pro_status'),
    path('aprovar_plano/<int:plano_id>/aprova/', views.aprovar_plano, name='aprovar_plano'),
    path('cancelar_plano/<int:plano_id>/cancelar/', views.cancelar_plano_pro, name='cancelar_plano_pro'),

    path('list_trabalho_pro/', views.list_trabalho_pro, name='list_trabalho_pro'),
    path('listar_trabalho_pro/<str:status2>/', views.list_trabalho_pro, name='list_trabalho_pro_status'),
    path('aprovar_trabalho/<int:trabalho_id>/aprova/', views.aprovar_trabalho, name='aprovar_trabalho'),
    path('cancelar_pro/<int:trabalho_id>/cancelar/', views.cancelar_trab_pro, name='cancelar_trab_pro'),



]