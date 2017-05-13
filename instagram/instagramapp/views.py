from django.shortcuts import render

# Create your views here.
def registrar(request):
    return render(request, 'registro.html')

def iniciar(request):
    return render(request, 'Inicio.html')

def home(request):
    return render(request, 'Ins.html')
