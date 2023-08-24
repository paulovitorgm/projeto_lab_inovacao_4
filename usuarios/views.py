from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from usuarios.forms import UsuarioForm, UsuarioJogaForm


def index(request):
    return render(request,'index.html')



def fazer_login(request):
    if request.user.is_authenticated:
        messages.error(request, 'Você já fez login.')
        return redirect('############################################################3')
    if request.method == 'POST':
        usuario = request.POST['####################################################']
        senha = request.POST['senha']

    user = authenticate(request,username=usuario, password=senha)
    if user is None:
        messages.error(request, "Usuário ou senha inválidos.")
        return redirect('login')

    if user is not None:
        login(request, user)
        return redirect ('#################################################################')



@login_required(login_url='fazer_login')
def fazer_logout(request):
    logout(request)
    return redirect()


def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        
    else:
        form = UsuarioForm()
    contexto = {'usuario': form}
    return render(request, 'form_usuario.html', contexto)










