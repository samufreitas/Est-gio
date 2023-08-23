from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.template_list, name='template_list'),


]