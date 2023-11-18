from django import forms
from jogos.models import Jogos, Plataforma
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

PLATAFORMA = tuple([(campo.pk, campo.plataforma) for campo in Plataforma.objects.all()])


def verifica_campo_vazio(campo):
    return not campo.strip()


class JogosForm(forms.ModelForm):
    nome = forms.CharField(label='Nome do jogo *', max_length=100, strip=True, required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'World of Warcraft',
                                                         'class': 'form-control', 'autocomplete': 'off'}))

    empresa_desenvolvedora = forms.CharField(label='Desenvolvedor *', max_length=100, strip=True, required=True,
                                             widget=forms.TextInput(attrs={'placeholder': 'Blizzard',
                                                                           'class': 'form-control', 'autocomplete': 'off'}))
    
    ano_lancamento = forms.IntegerField(label='Ano de lançamento *', max_value=datetime.today().year, min_value=2004,
                                        required=True, widget=forms.NumberInput(
                                        attrs={'placeholder': '2021', 'class': 'form-control', 'autocomplete': 'off'}))

    plataforma = forms.ModelChoiceField(label='Plataforma *', empty_label="Plataforma",
                                        queryset=Plataforma.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))

    imagem = forms.ImageField(label='Foto de perfil', required=False, help_text='PNG, JPEG, JPG',
                              validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'],
                              message='Arquivo inválido')], widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Jogos
        fields = ['nome', 'empresa_desenvolvedora', 'ano_lancamento', 'plataforma', 'imagem']

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if verifica_campo_vazio(nome):
            raise ValidationError('O campo "Nome do jogo" não pode ficar em branco.')
        if nome is None:
            raise ValidationError('Digite um valor válido.')
        return nome

    def clean_empresa_desenvolvedora(self):
        empresa = self.cleaned_data.get('empresa_desenvolvedora')
        if verifica_campo_vazio(empresa):
            raise ValidationError('O campo "Desenvolvedor" não pode ficar em branco.')
        if empresa is None:
            raise ValidationError('Digite um valor válido.')
        return empresa

    def clean_ano_lancamento(self):
        ano_atual = datetime.today().year
        ano = self.cleaned_data.get('ano_lancamento')
        if ano is None:
            raise ValidationError('Digite um valor válido.')
        if ano < 2004 or ano > ano_atual:
            raise ValidationError(f'O ano digitado deve estar entre 2004 e {ano_atual}.')
        return ano


class EditaJogosForm(forms.ModelForm):
    nome = forms.CharField(label='Nome do jogo', max_length=100, strip=True, required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'World of Warcraft',
                                                         'class': 'form-control', 'autocomplete': 'off'}))

    empresa_desenvolvedora = forms.CharField(label='Desenvolvedor', max_length=100, strip=True, required=True,
                                             widget=forms.TextInput(attrs={'placeholder': 'Blizzard',
                                                                           'class': 'form-control', 'autocomplete': 'off'}))

    ano_lancamento = forms.IntegerField(label='Ano de lançamento', max_value=datetime.today().year, min_value=2004,
                                        required=True, widget=forms.NumberInput(
            attrs={'placeholder': '2021', 'class': 'form-control', 'autocomplete': 'off'}))

    plataforma = forms.ModelChoiceField(label='Plataforma *',
                                        empty_label="Plataforma",
                                        queryset=Plataforma.objects.all(),
                                        widget=forms.Select(attrs={'class':'form-select'}))

    class Meta:
        model = Jogos
        fields = ['nome', 'empresa_desenvolvedora', 'ano_lancamento', 'plataforma']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
