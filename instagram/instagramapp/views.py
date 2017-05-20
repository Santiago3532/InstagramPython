from django.shortcuts import render

# Create your views here.
def registrar(request):
    return render(request, 'registro.html')

def iniciar(request):
    return render(request, 'Inicio.html')

def home(request):
    return render(request, 'Ins.html')

def crear_usuario(request):
    email = (request.POST[ 'email' ])
    username = (request.POST[ 'username' ])
    name = (request.POST[ 'name' ])
    password = (request.POST[ 'password' ])
    print(email, username, name, password)
    return render(request, 'registro.html')
