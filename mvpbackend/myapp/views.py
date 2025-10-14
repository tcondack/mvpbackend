from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def teste(request):
          return render(request, 'teste.html')

def parques(request):
          return render(request, 'parques.html')

def trilhas(request):
    return render(request, 'trilhas.html')

def eventos(request):
    return render(request, 'eventos.html')

def cadastro (request):
    if request.method == 'GET':
        return render (request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Usuário já cadastrado')
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse('Usuário cadastrado com sucesso!')

def login (request):
    if request.method == "GET":
        return render (request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse ('autenticado')
        else:
            return HttpResponse('usuário ou senha inválidos')

@login_required(login_url='/auth/login/')        
def ingressos(request):
      return HttpResponse('teste')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
