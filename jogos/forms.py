from django import forms
from jogos.models import Jogos
from datetime import datetime



PLATAFORMAS =(('PC','PC'),
              ('PS', 'PlayStation'),
              ('XB', 'XBox'),
              ('MB', 'Mobile')
              )


class JogosForm(forms.ModelForm):
    nome = forms.CharField(label='Nome do jogo', max_length=100, strip=True, required=True, 
                           widget=forms.TextInput(attrs={'placeholder' : 'World of Warcraft', 'class' : '', 'autocomplete' : 'off'}))
    
    plataforma = forms.MultipleChoiceField(label='Plataforma', choices=PLATAFORMAS, required=True,  
                                   widget=forms.CheckboxSelectMultiple(attrs={'class': ''}) )
    empresa_desenvolvedora = forms.CharField(label='Desenvolvedor', max_length=100, strip=True, required=True, 
                                             widget=forms.TextInput(attrs={'placeholder' : 'Blizzard', 'class' : '', 'autocomplete' : 'off'}))
    ano_lancamento = forms.IntegerField(label='Ano de lançamento', max_value=datetime.today().year, min_value=2004, 
                                    required=True, widget=forms.NumberInput(attrs={'placeholder' : '2021', 'class' : '', 'autocomplete' : 'off'}))
    
    imagem = forms.ImageField(label='Foto de perfil', required=False, widget=forms.FileInput(attrs={'class': ''}))

    class Meta:
        model = Jogos
        fields = '__all__'