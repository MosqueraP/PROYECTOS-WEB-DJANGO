from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from contact.forms import ContactForm


# Create your views here.

def contact(request):
    print(f'Tipo de peticion {request.method}')
    contact_form = ContactForm # crear plantill del formulario vacia

    #request = peticion
    # si la peticion viene con datos de envios = POST
    if request.method == 'POST': 
        contact_form = ContactForm(data=request.POST) # rellena la plantilla con la info
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # suponemos que todo ha ido bien, redireccionamos
            # return redirect('/contact/?ok')
            return redirect(reverse('contact') + '?ok')

    return render(request, "contact/contact.html", {'form': contact_form})