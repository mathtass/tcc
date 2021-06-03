from django.urls import path
from . import views

urlpatterns = [
    path('', views.tela, name='tela'),
]