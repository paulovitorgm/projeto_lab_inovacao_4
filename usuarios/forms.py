from django import forms
from django.contrib.auth.models import User

from usuarios.models import Usuario
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


DISPONIVEL = (("S", "Sim"), ("N", "Não"))


class UsuarioForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50,
                                 strip=True,
                                 required=True,
                                 label="Nome *",
                                 widget=forms.TextInput(
                                     attrs={'placeholder': 'José da Silva',
                                            'class': 'form-control',
                                            'autocomplete': 'off',
                                            'oninput': 'receber_apenas_letras(this)'}))

    last_name = forms.CharField(max_length=50,
                                strip=True,
                                required=True,
                                label="Sobrenome *",
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'José da Silva',
                                    'class': 'form-control',
                                    'autocomplete': 'off',
                                    'oninput': 'receber_apenas_letras(this)'}))

    email = forms.EmailField(max_length=100,
                             required=True,
                             label="Email * ",
                             widget=forms.EmailInput(attrs={
                                 'placeholder': 'email@email.com',
                                 'class': 'form-control',
                                 'autocomplete': 'off'}),
                             validators=[EmailValidator()])

    username = forms.CharField(max_length=50,
                               strip=True,
                               required=True,
                               label="Usuário *",
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Dendi',
                                          'class': 'form-control',
                                          'autocomplete': 'off'}))

    password = forms.CharField(max_length=60,
                                min_length=8,
                                strip=True,
                                required=True,
                                label="Senha *",
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': '********',
                                    'class': 'form-control',
                                    'autocomplete': 'off'}))

    senha_confirmacao = forms.CharField(max_length=60,
                                        min_length=8,
                                        strip=True,
                                        required=True,
                                        label="Confirme sua senha *",
                                        widget=forms.PasswordInput(attrs={
                                            'placeholder': '********',
                                            'class': 'form-control',
                                            'autocomplete': 'off'}))

    discord = forms.CharField(max_length=60,
                              strip=True,
                              required=False,
                              label="Discord",
                              widget=forms.TextInput(attrs={
                                    'placeholder': 'link do discord',
                                    'class': 'form-control',
                                    'autocomplete': 'off'}))

    disponivel_para_torneio = forms.ChoiceField(label="Está disponível para torneios",
                                                choices=DISPONIVEL,
                                                widget=forms.Select(attrs={
                                                    'class': 'form-select'}))

    foto_de_perfil = forms.ImageField(label='Foto de perfil',
                                      required=False,
                                      widget=forms.FileInput(attrs={
                                          'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'senha_confirmacao',
                  'discord', 'foto_de_perfil', 'disponivel_para_torneio']

    def clean_nome(self):
        lista_caracteres = [',', '.', '@', '#', '?', '!', '$', '%', '/', '|', '[', ']',
                            '{', '}', "'", '"', '(', ')', '¬', '*', '<', '>']
        nome = self.cleaned_data.get('nome')
        nome = nome.strip()
        for n in nome:
            if n in lista_caracteres:
                raise forms.ValidationError(f'O caractere {n} é inválido.')

        return nome

    def clean(self):
        cleaned_data = super().clean()
        senha_original = self.cleaned_data.get('password')
        senha_confirmacao = self.cleaned_data.get('senha_confirmacao')
        if senha_original and senha_confirmacao and (senha_original != senha_confirmacao):
            raise ValidationError('As senhas não conferem. Tente novamente.')
        return cleaned_data


class ResetarSenhaForm:
    email = forms.EmailField(max_length=100,
                             required=True,
                             label="Email",
                             widget=forms.EmailInput(attrs={
                                    'placeholder': 'email@email.com',
                                    'class': 'form-control',
                                    'autocomplete': 'off'}),
                             validators=[EmailValidator()])


class EditaUsuarioForm(forms.ModelForm):
    discord = forms.CharField(max_length=60,
                              strip=True,
                              required=False,
                              label="Discord",
                              widget=forms.TextInput(attrs={
                                    'placeholder': 'link do discord',
                                    'class': 'form-control',
                                    'autocomplete': 'off'}))

    disponivel_para_torneio = forms.ChoiceField(label="Está disponível para torneios",
                                                choices=DISPONIVEL,
                                                widget=forms.Select(attrs={
                                                    'class': 'form-select'}))

    foto_de_perfil = forms.ImageField(label='Foto de perfil',
                                      required=False,
                                      widget=forms.FileInput(attrs={
                                          'class': 'form-control'}))

    class Meta:
        model = Usuario
        fields = ['discord', 'foto_de_perfil', 'disponivel_para_torneio']


class EditaUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50,
                                 strip=True,
                                 required=True,
                                 label="Nome *",
                                 widget=forms.TextInput(attrs={
                                     'placeholder': 'José da Silva',
                                     'class': 'form-control',
                                     'autocomplete': 'off',
                                     'oninput': 'receber_apenas_letras(this)'}))

    last_name = forms.CharField(max_length=50,
                                strip=True,
                                required=True,
                                label="Sobrenome *",
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'José da Silva',
                                    'class': 'form-control',
                                    'autocomplete': 'off',
                                    'oninput': 'receber_apenas_letras(this)'}))

    email = forms.EmailField(max_length=100,
                             required=True,
                             label="Email * ",
                             widget=forms.EmailInput(attrs={
                                 'placeholder': 'email@email.com',
                                 'class': 'form-control',
                                 'autocomplete': 'off'}),
                             validators=[EmailValidator()])

    username = forms.CharField(max_length=50,
                               strip=True,
                               required=True,
                               label="Usuário *",
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Dendi',
                                   'class': 'form-control',
                                   'autocomplete': 'off'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
