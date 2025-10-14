from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('index', views.index, name='index'),

]
