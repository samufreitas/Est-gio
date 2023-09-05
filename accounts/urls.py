from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('novo_usuario/', views.add_user, name='add_user'),
    path('nova_senha/', views.user_new_password, name='user_new_password'),
    path('alterar_senha/', views.log_new_password, name='log_new_password'),
    path('voltar/', views.voltar, name='voltar'),
    path('sair/', views.user_logout, name='user_logout'),

]