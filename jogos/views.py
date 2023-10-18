from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from jogos.forms import JogosForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jogos.models import Plataforma, Jogos

#
# @login_required(login_url='/accounts/login')
# def cadastrar_jogo(request):
#     if request.method == 'POST':
#         form = JogosForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 messages.success(request, "Jogo salvo com sucesso.")
#                 return redirect("index")
#             except IntegrityError as e:
#                 messages.error(request, f"Erro ao salvar o jogo. Erro: {e}")
#                 contexto = {'form': form}
#                 return render(request, 'form_jogos.html', contexto)
#     else:
#         form = JogosForm()
#         contexto = {'form': form}
#         return render(request, 'form_jogos.html', contexto)


@login_required(login_url='/accounts/login')
def cadastrar_jogo(request):
    if request.method == 'POST':
        form = JogosForm(request.POST)
        if form.is_valid():
            try:
                nome, empresa_desenvolvedora, ano_lancamento, plataforma = recebe_campos_jogos(request)
                jogo = Jogos.objects.create(nome=nome, empresa_desenvolvedora=empresa_desenvolvedora,
                                      ano_lancamento=ano_lancamento)
                Plataforma.objects.create(jogo_id=jogo.pk, plataforma=plataforma)
                messages.success(request, "Jogo salvo com sucesso.")

                recebe_campos_jogos(request)
                return redirect("index")
            except IntegrityError as e:
                return HttpResponse(messages.error(request, f'Erro ao salvar novo jogo: {e}'))
        else:
            messages.error(request, 'Erro ao salvar')
            return redirect('cadastrar_jogo')
    else:

        form = JogosForm()
    contexto = {'form': form}
    return render(request, 'form_jogos.html', contexto)


def recebe_campos_jogos(request):
    nome = request.POST.get('nome')
    empresa_desenvolvedora = request.POST.get('empresa_desenvolvedora')
    ano_lancamento = request.POST.get('ano_lancamento')
    plataforma = request.POST.getlist('plataforma')
    print(plataforma)
    return nome, empresa_desenvolvedora, ano_lancamento, plataforma
