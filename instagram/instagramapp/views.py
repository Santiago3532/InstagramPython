from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from instagramapp.models import *

# Create your views here.
def registrar(request):
    return render(request, 'registro.html')

def iniciar(request):
    return render(request, 'Inicio.html')

def home(request):
    return render(request, 'Ins.html')

def crear_usuario(request):
    _email = (request.POST[ 'email' ])
    _username = (request.POST[ 'username' ])
    _name = (request.POST[ 'name' ])
    _password = (request.POST[ 'password' ])
    user = User.objects.create_user( username = _username, email =_email, first_name =_name, password =_password )
    print(user)
    print(user.password)
    myUser = MiUsuario(usuario = user)
    myUser.save()
    return redirect('iniciar')
