from django.urls import path

from . import views

app_name = 'professor'

urlpatterns = [
    path('add_periodo/', views.add_periodo, name='add_periodo'),
    path('add_periodo_disc/', views.add_periodo_disc, name='add_periodo_disc'),

]