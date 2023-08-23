from django.urls import path

from . import views

app_name = 'professor'

urlpatterns = [
    path('', views.pag_professor, name='pag_professor'),
    path('add_periodo/', views.add_periodo, name='add_periodo'),
    path('add_periodo_disc/', views.add_periodo_disc, name='add_periodo_disc'),
    path('list_plano_pro/', views.list_plano_pro, name='list_plano_pro'),
    path('aprovar_plano/<int:plano_id>/aprova/', views.aprovar_plano, name='aprovar_plano'),
]