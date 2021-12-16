from django.shortcuts import render, redirect
from .models import Cliente, productos, Contacto
from .forms import ContactoForm, UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .backend import MyBackend
from django.contrib import messages
# Create your views here.
myBackend = MyBackend()


def home(request):
    if request.method == 'GET':
        producto = productos.objects.all()
        return render(request, 'appGrupal_3/home.html',{'producto':producto})

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, f'Usuario {username} creado')
            return redirect('home')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'appGrupal_3/registro.html', context)

@login_required

def contacto (request):
    data ={
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] ="mensaje guardado"
        
        else :
            data["form"]= formulario
    return render (request, 'appGrupal_3/contacto.html', data)
