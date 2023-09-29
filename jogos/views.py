from django.shortcuts import render, redirect
from jogos.forms import JogosForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jogos.models import Jogos, Plataforma



def cadastrar_jogo(request):
    if request.method == 'POST':
        form = JogosForm(request.POST)
        if form.is_valid():
            form.save()
            plataforma = Plataforma.objects.create(jogo=request.POST['plataforma'])
            plataforma.save()
        else:
            messages.error(request, 'Erro ao salvar')
            return redirect('cadastrar_jogo')
    else:
        form = JogosForm()
    contexto = {'form':form}
    return render(request, 'form_jogos.html', contexto)




