from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Página de teste
def teste(request):
          return render(request, 'teste.html')
# Páginas públicas
def parques(request):
          return render(request, 'parques.html')

def trilhas(request):
    return render(request, 'trilhas.html')

def eventos(request):
    return render(request, 'eventos.html')

# Páginas de cadastro
def cadastro (request):
    if request.method == 'GET':
        return render (request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verifica se existe usuário com o mesmo nome              
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse('Usuário já cadastrado')
                  
        # cria e salva o novo usuário
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return HttpResponse('Usuário cadastrado com sucesso!')

# Login  usuário
def login_view (request):
    if request.method == "GET":
        return render (request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return redirect ('/admin/')
        else:
            return HttpResponse('usuário ou senha inválidos')

@login_required(login_url='/auth/login/')        
def admin(request):
      return HttpResponse('Acesso liberado, Página protegida')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
