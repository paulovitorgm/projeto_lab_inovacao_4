from django.shortcuts import render
from jogos.forms import JogosForm

def index(request):
    return render(request,'index.html')


def jogos(request):
    jogos = JogosForm
    contexto = {'jogos' : jogos}
    return render(request, 'form_jogos.html', contexto)