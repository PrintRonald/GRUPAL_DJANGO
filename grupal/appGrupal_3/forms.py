from django import forms
from django.contrib.auth.models import User
from .models import  Contacto, Cliente

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["nombre", "correo","tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'

class RegistroForm(forms.ModelForm):
    rut = forms.CharField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña',widget=forms.PasswordInput) 

    class Meta:
        model = Cliente
        fields = ['rut','nombre','apellido','correo','password1','password2']
        help_text = { k:"" for k in fields }



