from django import forms
from jogos.models import Jogos, Plataforma
from usuarios.models import NickUsuario


JOGOS = tuple([(campo.pk, campo.nome) for campo in Jogos.objects.all()])
PLATAFORMA = tuple([(campo.pk, campo.plataforma) for campo in Plataforma.objects.all()])


class UsuarioJogaForm(forms.ModelForm):
    nick = forms.CharField(max_length=50, strip=True, required=True, label="Nick *",
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Dendi', 'class': '', 'autocomplete': 'off'}))

    jogo = forms.ChoiceField(label="Jogo *", choices=JOGOS)

    regiao_server = forms.CharField(max_length=50, strip=True, required=True, label="Servidor *",
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'Americas', 'class': '', 'autocomplete': 'off'}))

    link_perfil_jogador = forms.CharField(max_length=50, strip=True, required=True, label="Link do perfil do jogador *",
                                 widget=forms.TextInput(attrs={'placeholder': 'https://steamcommunity.com/profiles/761',
                                            'class': '', 'autocomplete': 'off'}))

    plataforma = forms.ChoiceField(label="Plataforma", choices=PLATAFORMA)

    class Meta:
        model = NickUsuario
        fields = ['nick', 'jogo', 'regiao_server', 'link_perfil_jogador', 'plataforma']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
