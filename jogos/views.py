from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from jogos.forms import JogosForm, EditaJogosForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jogos.models import Plataforma, Jogos


@login_required(login_url='/accounts/login')
def cadastrar_jogo(request):
    if request.method == 'POST':
        form = JogosForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                jogo = form.save(commit=False)
                jogo.plataforma = get_object_or_404(Plataforma, pk=request.POST.get('plataforma'))
                jogo.save()
                messages.success(request, "Jogo salvo com sucesso.")
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


@login_required(login_url='/accounts/login')
def editar_jogo(request, pk):
    jogo = get_object_or_404(Jogos, pk=pk)
    form = EditaJogosForm(instance=jogo)
    contexto = {'form': form, 'jogo': jogo}
    if request.method == 'POST':
        try:
            jogo.nome = request.POST.get('nome')
            jogo.empresa_desenvolvedora = request.POST.get('empresa_desenvolvedora')
            jogo.ano_lancamento = request.POST.get('ano_lancamento')
            jogo.plataforma = get_object_or_404(Plataforma, pk=request.POST.get('plataforma'))
            jogo.save(update_fields=['nome', 'empresa_desenvolvedora', 'ano_lancamento', 'plataforma'])
            messages.success(request, "Jogo salvo com sucesso.")
            return redirect('index')
        except IntegrityError as e:
            return HttpResponse(messages.error(request, f'Erro ao salvar novo jogo: {e}'))
    return render(request, 'editar_jogo.html', contexto)


@login_required(login_url='/accounts/login')
def deletar_jogo(request, pk):
    jogo = get_object_or_404(Jogos, pk=pk)
    jogo.delete()
    messages.success(request, "Jogo deletado com sucesso.")
    return redirect('index')
