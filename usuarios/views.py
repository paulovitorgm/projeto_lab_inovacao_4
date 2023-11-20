from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from ProjetoJogos.settings import DEFAULT_FROM_EMAIL
from usuarios.formularios.NickUsuarioForm import UsuarioJogaForm
from usuarios.models import Usuario
from usuarios.forms import UsuarioForm, EditaUsuarioForm, EditaUserForm
from jogos.models import Jogos, Plataforma


def index(request):
    usuario = Usuario()
    jogos = Jogos.objects.all()
    jogadores = User.objects.all()
    plataforma = Plataforma.objects.all()
    contexto = {'jogos': jogos, 'usuario': usuario, 'jogadores': jogadores, 'plataformas': plataforma}

    if 'busca' in request.GET:
        busca = request.GET.get('busca')
        jogadores_encontrados = jogadores.filter(username__icontains=busca)
        if jogadores_encontrados.first() is None:
            messages.error(request, f'Jogador "{busca}" não encontrado. Tente novamente.')

        contexto = {'jogos': jogos, 'usuario': usuario, 'jogadores': jogadores,
                    'plataformas': plataforma, 'busca': jogadores_encontrados}
    return render(request, 'index.html', contexto)


def cadastrar_usuario(request):
    if request.user.is_authenticated:
        messages.error(request, 'Você não pode fazer um novo cadastro.')
        return redirect('index')
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario, email, nome, sobrenome = recebe_campos_user(request)
            discord, disponivel_para_torneio, foto_de_perfil = recebe_campos_usuario(request)
            senha = request.POST.get('senha')
            try:
                usuario_tabela_user = User.objects.create_user(username=usuario, email=email, password=senha,
                                                               first_name=nome, last_name=sobrenome)

                Usuario.objects.create(discord=discord, disponivel_para_torneio=disponivel_para_torneio,
                                       id_usuario=usuario_tabela_user, foto_de_perfil=foto_de_perfil)

                messages.success(request, f"Usuário {usuario} salvo com sucesso.")
                return redirect('login')
            except IntegrityError as e:
                return HttpResponse(messages.error(request, f'Erro ao salvar novo usuário: {e}'))

    else:
        form = UsuarioForm()
    contexto = {'form': form}
    return render(request, 'registration/cadastrar_usuario.html', contexto)


@login_required(login_url='/accounts/login')
def editar_user(request):
    usuario = User.objects.get(pk=request.user.pk)
    form = EditaUserForm(instance=usuario)
    contexto = {"form": form}
    if request.method == "POST":
        try:
            usuario.username, usuario.email, usuario.first_name, usuario.last_name = recebe_campos_user(request)
            usuario.save(update_fields=['username', 'first_name', 'last_name', 'email'])
            messages.success(request, f"Usuario {usuario.username} editado com sucesso")
            return redirect('index')
        except IntegrityError as e:
            return HttpResponse(messages.error(request, f'Erro ao salvar novo usuário: {e}'))

    return render(request, 'editar_user.html', contexto)


@login_required(login_url='/accounts/login')
def editar_usuario(request):
    usuario = Usuario.objects.get(id_usuario=request.user)
    print(usuario)
    form = EditaUsuarioForm(instance=usuario)
    contexto = {"form": form}
    if request.method == "POST":
        usuario.discord, usuario.disponivel_para_torneio, usuario.foto_de_perfil = recebe_campos_usuario(request)
        usuario.save(update_fields=['discord', 'disponivel_para_torneio', 'foto_de_perfil'])
        return redirect('index')
    return render(request, 'editar_usuario.html', contexto)


@login_required(login_url='/accounts/login')
def deleta_usuario(request):
    usuario = get_object_or_404(User, pk=request.user.pk)
    usuario.delete()
    messages.success(request, "Usuário deletado com sucesso.")
    return redirect('index')


@login_required(login_url='/accounts/login')
def alterar_senha(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('index')
        else:
            return HttpResponse("SENHA NÃO ALTERADA")
    else:
        form = PasswordChangeForm(user=request.user)
        contexto = {'form': form}
        return render(request, 'registration/troca_senha.html', contexto)


#
#
#ainda não está funcionando
#
#
@login_required(login_url='/accounts/login')
def cadastrar_nick(request):
    form = UsuarioJogaForm
    contexto = {'form': form}
    if request.method == 'POST':
        form = UsuarioJogaForm(request.POST)
        print(str(request.user.pk) * 100)
        if form.is_valid():
            form.save(commit=False)
            form.usuario_id_id = get_object_or_404(Usuario, id_usuario_id=request.user.pk)
            form.save()
        messages.success(request, f"Nick {request.POST.get('nick')} salvo com sucesso.")
        return redirect('index')
    return render(request, 'form_nick.html', contexto)


def recebe_campos_user(request):
    usuario = request.POST.get('username')
    email = request.POST.get('email')
    nome = request.POST.get('first_name')
    sobrenome = request.POST.get('last_name')
    return usuario, email, nome, sobrenome


def recebe_campos_usuario(request):
    discord = request.POST['discord']
    disponivel_para_torneio = request.POST.get('disponivel_para_torneio')
    foto_de_perfil = request.FILES.get('foto_de_perfil')
    return discord, disponivel_para_torneio, foto_de_perfil


def recebe_campos_nick(request):
    jogo = request.POST.get('jogo')
    nick = request.POST.get('nick')
    regiao_server = request.POST.get('regiao_server')
    link_perfil_jogador = request.POST.get('link_perfil_jogador')
    plataforma = request.POST.get('plataforma')
    return jogo, nick, regiao_server, link_perfil_jogador, plataforma


def enviar_email(assunto, mensagem, destinatario):
    send_mail(assunto, mensagem, DEFAULT_FROM_EMAIL, recipient_list=[destinatario])
