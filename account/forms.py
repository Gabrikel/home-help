from django import forms
from .models import UserBase


class RegistrationForm(forms.ModelForm):

    user_name = forms.CharField(label='Digite o seu nome de Usuário', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'required': 'Desculpe, você precisa de um emal!'})
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)
        