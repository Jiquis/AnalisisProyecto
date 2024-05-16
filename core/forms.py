from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }

class AlimentosForm(forms.ModelForm):
    class Meta:
        model = Alimentos
        fields = [
            "nombre",
            "marca",
            "precio",
            "cantidad",
            "descripcion",
            "fecha_vencimiento",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Especificar el tipo de campo de fecha de vencimiento como 'date'
        self.fields['fecha_vencimiento'].widget = forms.DateInput(attrs={'type': 'date'})

class MedicinasForm(forms.ModelForm):
    class Meta:
        model = Medicinas
        fields = [
            "nombre",
            "principio_activo",
            "precio",
            "cantidad",
            "descripcion",
            "fecha_vencimiento",
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Especificar el tipo de campo de fecha de vencimiento como 'date'
        self.fields['fecha_vencimiento'].widget = forms.DateInput(attrs={'type': 'date'})

class JuguetesForm(forms.ModelForm):
    class Meta:
        model = Juguetes
        fields = [
            "nombre",
            "precio",
            "cantidad",
            "descripcion",
        ]

class UtensiliosForm(forms.ModelForm):
    class Meta:
        model = Utensilios
        fields = [
            "nombre",
            "precio",
            "cantidad",
            "descripcion",
            "esterilizable",
        ]