from django import forms
from jogos.models import Jogos, Plataforma
from usuarios.models import NickUsuario


class NickUsuarioForm(forms.ModelForm):
    nick = forms.CharField(label="Nick *",
                           max_length=50,
                           strip=True,
                           required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Dendi',
                                                         'class': 'form-control',
                                                         'autocomplete': 'off'}))

    jogo = forms.ModelChoiceField(label='Jogo',
                                  empty_label="Jogo",
                                  queryset=Jogos.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-select'}))

    regiao_server = forms.CharField(max_length=50,
                                    strip=True,
                                    required=True,
                                    label="Servidor *",
                                    widget=forms.TextInput(
                                        attrs={'placeholder': 'Americas',
                                               'class': 'form-control',
                                               'autocomplete': 'off'}))

    link_perfil_jogador = forms.CharField(max_length=50,
                                          strip=True,
                                          required=True,
                                          label="Link do perfil do jogador *",
                                          widget=forms.TextInput(attrs={
                                            'placeholder': 'https://steamcommunity.com/profiles/761',
                                            'class': 'form-control',
                                            'autocomplete': 'off'}))

    plataforma = forms.ModelChoiceField(label='Plataforma *',
                                        empty_label="Plataforma",
                                        queryset=Plataforma.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = NickUsuario
        fields = ['nick', 'jogo', 'regiao_server', 'link_perfil_jogador', 'plataforma']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
