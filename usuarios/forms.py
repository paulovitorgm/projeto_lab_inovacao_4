from typing import Any, Dict
from django import forms
from usuarios.models import Usuario
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

class UsuarioForm(forms.ModelForm):
    
    nome =  forms.CharField(max_length=100, strip=True, required=True, label="Nome completo",  
                            widget=forms.TextInput(attrs={'placeholder':'José da Silva', 'class':'', 'autocomplete': 'off',
                                                          'oninput':'receber_apenas_letras(this)'}))
    email =  forms.EmailField(max_length=100, required=True, label="Email",  
                              widget=forms.EmailInput(attrs={'placeholder':'email@email.com', 'class':'', 'autocomplete':'off'}), validators=[EmailValidator()])
    usuario = forms.CharField(max_length=50, strip=True, required=True, label="Usuario", 
                            widget=forms.TextInput(attrs={'placeholder':'Dendi', 'class':'', 'autocomplete': 'off'}))
    senha = forms.CharField(max_length=60, min_length=8, strip=True, required=True, label="Senha", 
                            widget=forms.PasswordInput(attrs={'placeholder':'********', 'class':'', 'autocomplete': 'off'}))
    senha_confirmacao = forms.CharField(max_length=60, min_length=8, strip=True, required=True, label="Confirme sua senha", 
                            widget=forms.PasswordInput(attrs={'placeholder':'********', 'class':'', 'autocomplete': 'off'}))
    discord = forms.CharField(max_length=60, strip=True, required=False, label="Discord", 
                            widget=forms.TextInput(attrs={'placeholder':'link do discord', 'class':'', 'autocomplete': 'off'}))
    foto_de_perfil = forms.ImageField(label='Foto de perfil', required=False, widget=forms.FileInput(attrs={'class': ''}))
    disponivel_para_torneio = forms.BooleanField(label= "Está disponível para torneios", required=False, widget=forms.CheckboxInput(attrs={'class' : ''}))
    
    
    class Meta:
        model = Usuario
        fields = ['nome', 'usuario', 'email', 'senha', 'senha_confirmacao', 'discord', 'foto_de_perfil', 'disponivel_para_torneio']


    def clean_nome(self):
        lista_caracteres = [',','.','@','#','?','!','$','%','/','|','[',']','{','}',"'",'"','(',')','¬','*','<','>']
        nome = self.cleaned_data.get('nome')
        nome = nome.strip()
        for n in nome:
            if n in lista_caracteres:
                raise ValidationError(f'O caractere {n} é inválido.')
        if len(nome.split()) < 2:
            raise ValidationError('Por favor, digite o nome completo.')
        return nome


    def clean(self):
        cleaned_data = super().clean()
        senha_original = self.cleaned_data.get('senha')
        senha_confirmacao = self.cleaned_data.get('senha_confirmacao')
        if senha_original and senha_confirmacao and (senha_original != senha_confirmacao):
            raise ValidationError('As senhas não conferem. Tente novamente.')
        return cleaned_data


    





class UserForm(forms.ModelForm):
    senha = forms.CharField(max_length=60, min_length=8, strip=True, required=True, label="Senha", 
                            widget=forms.PasswordInput(attrs={'placeholder':'********', 'class':'', 'autocomplete': 'off'}))
    senha_confirmacao = forms.CharField(max_length=60, min_length=8, strip=True, required=True, label="Confirme sua senha", 
                            widget=forms.PasswordInput(attrs={'placeholder':'********', 'class':'', 'autocomplete': 'off'}))
    
    class Meta:
        model = User
        fields = ['senha', 'senha_confirmacao']
        


def clean_senha(self):
        senha_original = self.cleaned_data.get('senha')
        senha_confirmacao = self.cleaned_data.get('senha_confirmacao')
        if senha_original is not None:
            if senha_original == senha_confirmacao:
                return senha_confirmacao
            else:
                raise ValidationError('As senhas não conferem. Tente novamente.')
        else:
            raise ValidationError('Senha inválida.')


