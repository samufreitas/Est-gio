from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('novo_usuario/', views.add_user, name='add_user'),
    path('novo_senha/', views.user_new_password, name='user_new_password'),


]