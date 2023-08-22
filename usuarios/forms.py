from django import forms
from usuarios.models import Usuario, UsuarioJoga


class UsuarioForm(forms.ModelForm):

    nome =  forms.CharField(max_length=100, strip=True, required=True, label="Nome completo", 
                            widget=forms.TextInput(attrs={'placeholder':'José da Silva', 'class':'', 'autocomplete': 'off'}))
    email =  forms.EmailField(max_length=100, required=True, label="Email", 
                              widget=forms.EmailInput(attrs={'placeholder':'email@email.com', 'class':'', 'autocomplete':'off'}))
    usuario = forms.CharField(max_length=50, strip=True, required=True, label="Usuario", 
                            widget=forms.TextInput(attrs={'placeholder':'Dendi', 'class':'', 'autocomplete': 'off'}))
    senha = forms.CharField(max_length=60, min_length=8, strip=True, required=True, label="Senha", 
                            widget=forms.PasswordInput(attrs={'placeholder':'********', 'class':'', 'autocomplete': 'off'}))
    senha_confirmacao = forms.CharField(max_length=60, min_length=8, strip=True, required=True, label="Confirme sua senha", 
                            widget=forms.PasswordInput(attrs={'placeholder':'********', 'class':'', 'autocomplete': 'off'}))
    discord = forms.CharField(max_length=60, strip=True, required=True, label="Confirme sua senha", 
                            widget=forms.TextInput(attrs={'placeholder':'link do discord', 'class':'', 'autocomplete': 'off'}))
    foto_de_perfil = forms.ImageField(label='Foto de perfil', widget=forms.FileInput(attrs={'class': ''}))
    disponivel_para_torneio = forms.BooleanField(label= "Está disponível para torneios", widget=forms.CheckboxInput(attrs={'class' : ''}))
    
    
    class Meta:
        model = Usuario
        fields = ['nome', 'usuario', 'email', 'senha', 'senha_confirmacao', 'discord', 'foto_de_perfil', 'disponivel_para_torneio']


class UsuarioJogaForm(forms.ModelForm):
    class Meta:
        model = UsuarioJoga
        fields = '__all__'