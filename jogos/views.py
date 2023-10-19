from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from jogos.forms import JogosForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jogos.models import Plataforma, Jogos


@login_required(login_url='/accounts/login')
def cadastrar_jogo(request):
    if request.method == 'POST':
        form = JogosForm(request.POST)
        if form.is_valid():
            try:
                jogo = form.save()
                plataforma = request.POST.getlist('plataforma')
                for p in plataforma:
                    Plataforma.objects.create(jogo_id=jogo.pk, plataforma=p)
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
