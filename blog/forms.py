from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormCampeones(forms.Form):    
    titulo = forms.CharField(max_length=150, label='Titulo')
    subtitulo = forms.CharField(max_length=100, label='Subtitulo')
    cuerpo = forms.CharField(widget=forms.Textarea, label='Cuerpo')
    imagen = forms.ImageField(label='Imagen')