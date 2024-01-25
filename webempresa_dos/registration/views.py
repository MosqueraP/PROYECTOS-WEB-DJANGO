from django.contrib.auth.forms import UserCreationForm # formulario generico
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

# vista de registro ususarios
class SignUpView(CreateView):
    form_class = UserCreationForm 
    template_name = 'registration/signup.html' #carag el template en esta ubicación

    def get_success_url(self):
        return reverse_lazy('login') + '?register' # redireccionar a login a login