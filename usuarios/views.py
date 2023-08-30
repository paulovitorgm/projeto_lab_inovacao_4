from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password

from django.shortcuts import get_object_or_404, get_list_or_404

from usuarios.models import Usuario
from usuarios.forms import UsuarioForm, UsuarioJogaForm




def index(request):
    return render(request,'index.html')



def fazer_login(request):
    if request.user.is_authenticated:
        messages.error(request, 'Você já fez login.')
        return redirect('############################################################')
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
            form.save(commit=False)
            form.senha = make_password(form.senha)
            form.save()
    else:
        form = UsuarioForm()
    contexto = {'usuario': form}
    return render(request, 'form_usuario.html', contexto)



# @login_required
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if request.method == 'GET':
        form = UsuarioForm(instance=usuario) 
        form.fields.pop('senha')
        form.fields.pop('senha_confirmacao')
    else:
        form = UsuarioForm(request.POST, instance=usuario)
        form.fields.pop('senha')
        form.fields.pop('senha_confirmacao')
        if form.is_valid():
            campos = ['nome', 'email', 'discord', 'disponivel_para_torneio', 'foto_de_perfil']
            form.save(commit=False)
            for campo in campos:
                setattr(usuario, campo, form.cleaned_data[campo])
           
            usuario.save()
            messages.success(request,'Cadastro atualizado com sucesso.')
        else:
            messages.error(request,'Erro ao atualizar cadastro, tente novamente.')
    
    contexto = { 'usuario' : usuario, 'form':form }
    return render(request, 'editar_usuario.html', contexto)
        




