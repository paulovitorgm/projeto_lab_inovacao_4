from django.shortcuts import render
from usuarios.forms import UsuarioForm, UsuarioJogaForm



def usuario_form(request):
    usuario = UsuarioForm()

    contexto = {'usuario': usuario}
    return render(request, 'form_usuario.html',contexto)