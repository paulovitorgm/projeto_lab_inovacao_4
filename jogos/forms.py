from django import forms
from jogos.models import Jogos
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


PLATAFORMAS_CHOICES =(('PC','PC'),
              ('PS', 'PlayStation'),
              ('XB', 'XBox'),
              ('MB', 'Mobile')
              )


class JogosForm(forms.ModelForm):
    nome = forms.CharField(label='Nome do jogo', max_length=100, strip=True, required=True, 
                           widget=forms.TextInput(attrs={'placeholder' : 'World of Warcraft', 'class':'', 'autocomplete' : 'off'}))
    
    empresa_desenvolvedora = forms.CharField(label='Desenvolvedor', max_length=100, strip=True, required=True, 
                                             widget=forms.TextInput(attrs={'placeholder' : 'Blizzard', 'class':'', 'autocomplete' : 'off'}))
    
    ano_lancamento = forms.IntegerField(label='Ano de lançamento', max_value=datetime.today().year, min_value=2004, 
                                    required=True, widget=forms.NumberInput(attrs={'placeholder' : '2021', 'class':'', 'autocomplete' : 'off'}))
    
    plataforma = forms.MultipleChoiceField(label='Plataforma', choices=PLATAFORMAS_CHOICES, required=True,  
                                   widget=forms.CheckboxSelectMultiple(attrs={'class':''}) )
    
    imagem = forms.ImageField(label='Foto de perfil', required=False, 
                              help_text='PNG, JPEG, JPG',validators=[FileExtensionValidator(allowed_extensions=['png','jpeg', 'jpg'], 
                                                                                            message='Arquivo inválido')],
                               widget=forms.FileInput(attrs={'class':''}))

    class Meta:
        model = Jogos
        fields = '__all__'


    def clean_ano_lancamento(self):
        ano_atual = datetime.today().year
        ano = self.cleaned_data.get('ano_lancamento')
        if ano >= 2004 and ano <= ano_atual:
            return ano
        else:
            raise ValidationError(f'O ano digitado deve estar entre 2004 e {ano_atual}.')



