from django.shortcuts import render
from jogos.forms import JogosForm

def index(request):
    return render(request,'index.html')


def jogos(request):
    
    if request.method == "GET":
        jogos = JogosForm
        contexto = {'jogos' : jogos}
    else:
        jogos = JogosForm
        # if jogos.is_valid():
      
            

        
            
        contexto = {'jogos' : jogos}

    return render(request, 'form_jogos.html', contexto)