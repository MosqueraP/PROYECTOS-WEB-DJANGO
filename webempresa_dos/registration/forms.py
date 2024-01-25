from django import forms
from django.contrib.auth.forms import UserCreationForm # formulario generico
from django.contrib.auth.models import User

# Extender el formulario generico para que tenga correo y recuperar contraseñas
class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como maximo y debe ser valido.')

    class Meta:
        # nuevo campo de emeail en el fomulario
        model = User
        fields = ('username', 'email', 'password1', 'password2')

