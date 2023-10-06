from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

from usuarios.models import Usuario
from usuarios.forms import UsuarioForm, UserForm
from jogos.models import Jogos


def index(request):
    usuario = Usuario()
    jogos = Jogos.objects.all()
    jogadores = User.objects.all()
    busca = request.GET.get('busca')

    if busca:
        jogos = jogadores.filter(username__icontains=busca)

    contexto = {'jogos': jogos, 'usuario': usuario, 'jogadores': jogadores}

    return render(request, 'index.html', contexto)


def cadastrar_usuario(request):
    if request.user.is_authenticated:
        messages.error(request, 'Você não pode fazer um novo cadastro.')
        return redirect('index')
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = request.POST['usuario']
            email = request.POST['email']
            senha = request.POST['senha']
            nome_completo = request.POST['nome']
            nome = nome_completo[:nome_completo.find(' ')]
            sobrenome = nome_completo[nome_completo.find(' '):].strip()
            discord = request.POST['discord']
            disponivel_para_torneio = True if request.POST.get('disponivel_para_torneio') == "on" else False

            try:
                usuario_tabela_user = User.objects.create_user(username=usuario, email=email, password=senha,
                                                               first_name=nome, last_name=sobrenome)
                # FALTA IMPLEMENTAR A RECEPÇÃO DA IMAGEM
                Usuario.objects.create(discord=discord, disponivel_para_torneio=disponivel_para_torneio,
                                       id_usuario=usuario_tabela_user)
                messages.success(request, f"Usuário {usuario} salvo com sucesso.")
                return redirect('index')
            except IntegrityError as e:
                messages.error(request, f'Erro ao salvar novo usuário: {e}')
    else:
        form = UsuarioForm()
    contexto = {'form': form}
    return render(request, 'registration/cadastrar_usuario.html', contexto)


@login_required(login_url='/accounts/login')
def editar_usuario(request, pk):
    usuario_a_editar = get_object_or_404(User, pk=pk)
    contexto = {'form': usuario_a_editar}
    if request.method == "POST":
        usuario_a_editar.username = request.POST['usuario']
        usuario_a_editar.email = request.POST['email']

        nome_completo = request.POST['nome_completo']
        nome = nome_completo[: nome_completo.find(' ')]
        sobrenome = nome_completo[nome_completo.find(' '):].strip()

        usuario_a_editar.first_name = nome
        usuario_a_editar.last_name = sobrenome
        usuario_a_editar.save()
        return redirect('index')
    return render(request, 'editar_usuario.html', contexto)


@login_required(login_url='/accounts/login')
def deleta_usuario(request, pk):
    usuario = get_object_or_404(User, pk=pk)
    usuario.delete()
    messages.success(request, "Usuário deletado com sucesso.")
    return redirect('index')


def alterar_senha(request, username):
    obj_usuario = get_object_or_404(User, username=username)
    if request.method == 'POST':
        senha = request.POST['senha']
        obj_usuario.set_password(senha)
        obj_usuario.save()

        return redirect('cadastrar_usuario')
    else:
        form = UserForm()
        contexto = {'form': form}
        return render(request, 'registration/troca_senha.html', contexto)


def busca_usuario(request):
    pass
    # lista_de_usuarios: object = Jogos.objects.all()
    # print(lista_de_usuarios)
    # if 'busca' in request.GET:
    #     nome_a_buscar = request.GET['busca']
    #     lista_de_usuarios = lista_de_usuarios.filter(nome=nome_a_buscar)
    #     return lista_de_usuarios
        # contexto = {'busca': lista_de_usuarios}
        # if lista_de_usuarios:
        #     messages.success(request, 'Usuários encontrados:')
        # else:
        #     messages.error(request, 'Nenhum usuário encontrado. Tente novamente.')
        # return render(request, 'busca_usuarios.html', contexto)
    # else:
    #     return render(request, 'busca_usuarios.html')
