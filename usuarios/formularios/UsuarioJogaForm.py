from django import forms

from jogos.models import Jogos, Plataforma
from usuarios.models import UsuarioJoga


PLATAFORMA = (
                ('PC', 'PC'),
                ('PS', 'PlayStation'),
                ('XB', 'XBox'),
                ('MB', 'Mobile')
              )

JOGOS = tuple([(campo.pk, campo.nome) for campo in Jogos.objects.all()])


class UsuarioJogaForm(forms.ModelForm):
    jogo = forms.ChoiceField(label="Jogo *", choices=JOGOS)

    regiao_server = forms.CharField(max_length=50, strip=True, required=True, label="Servidor *",
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'Americas', 'class': '', 'autocomplete': 'off'}))

    nick = forms.CharField(max_length=50, strip=True, required=True, label="Nick *",
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'Dendi', 'class': '', 'autocomplete': 'off'}))

    link_perfil_jogador = forms.CharField(max_length=50, strip=True, required=True, label="Nome *",
                                 widget=forms.TextInput(attrs={'placeholder': 'https://steamcommunity.com/profiles/761',
                                            'class': '', 'autocomplete': 'off'}))

    plataforma = forms.ChoiceField(label="Plataforma", choices=PLATAFORMA)

    class Meta:
        model = UsuarioJoga
        fields = ['jogo', 'regiao_server', 'nick', 'link_perfil_jogador']
