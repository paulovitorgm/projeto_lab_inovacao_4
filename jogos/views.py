from django.shortcuts import render
from jogos.forms import JogosForm
from django.contrib.auth.decorators import login_required


#@login_required()
def cadastrar_jogo(request):
    
    if request.method == "POST":
        form = JogosForm(request.POST)
        if form.is_valid():
            print('ok')
        else:
            print('erro')
    else:
        form = JogosForm()
      
    contexto = {'jogos' : form}

    return render(request, 'form_jogos.html', contexto)