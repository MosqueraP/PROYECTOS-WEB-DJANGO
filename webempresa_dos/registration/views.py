from registration.forms import UserCreationFormWithEmail
from django.contrib.auth.forms import UserCreationForm # formulario generico
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

# Create your views here.

# vista de registro ususarios
class SignUpView(CreateView):
    # form_class = UserCreationForm # quitamos el formulario generico
    form_class = UserCreationFormWithEmail # formulario extencion desde registration.form.py
    template_name = 'registration/signup.html' #carag el template en esta ubicación

    def get_success_url(self):
        return reverse_lazy('login') + '?register' # redireccionar a login a login
    
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        # modificar en tiempo real los widges
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder':'Nombre de ususario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-2', 'placeholder':'Direccion email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-2', 'placeholder':'Repite la contraseña'})
        # form.fields['username'].label = '' #quita las label
        return form
    
    

