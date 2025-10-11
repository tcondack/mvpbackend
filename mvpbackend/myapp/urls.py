from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadstro'),
    path('login/', views.login, name='login'),
]