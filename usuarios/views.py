from django.http import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from ProjetoJogos.settings import DEFAULT_FROM_EMAIL
from usuarios.models import Usuario
from usuarios.forms import UsuarioForm
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
                envia_email_quando_cria_usuario(nome, destinatario=email)
                messages.success(request, f"Usuário {usuario} salvo com sucesso.")
                return redirect('login')
            except IntegrityError as e:
                messages.error(request, f'Erro ao salvar novo usuário: {e}')
    else:
        form = UsuarioForm()
    contexto = {'form': form}
    return render(request, 'registration/cadastrar_usuario.html', contexto)


@login_required(login_url='/accounts/login')
def editar_usuario(request):
    usuario_a_editar = get_object_or_404(User, pk=request.user.pk)
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


@login_required(login_url='/accounts/login')
def alterar_senha(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('index')
        else:
            return HttpResponse("SENHÃ NÃO ALTERADA")
    else:
        form = PasswordChangeForm(user=request.user)
        contexto = {'form': form}
        return render(request, 'registration/troca_senha.html', contexto)


def enviar_email(assunto, mensagem, destinatario):
    send_mail(assunto, mensagem, DEFAULT_FROM_EMAIL, recipient_list=[destinatario])


def envia_email_quando_cria_usuario(nome, destinatario):
    assunto = "Criação de conta"
    mensagem = f"Obrigado {nome} pelo registro na nossa plataforma, agora você pode desfrutar dos nossos serviços."
    enviar_email(assunto, mensagem, destinatario)
