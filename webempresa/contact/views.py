from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from contact.forms import ContactForm
from django.core.mail import EmailMessage
from smtplib import SMTPException


# Create your views here.

def contact(request):
    print(f'Tipo de peticion {request.method}')
    contact_form = ContactForm # crear plantill del formulario vacia

    #request = peticion
    # si la peticion viene con datos de envios = POST
    if request.method == 'POST': 
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Corrige la configuración del EmailMessage
            email = EmailMessage(
                'Howard, nuevo mensaje de contacto',
                'De {} <{}>\n\nEsribio:{}'.format(name, email, content),
                'aux.isidro@gmail.com',  # Cambia a tu dirección de correo real o usa la misma de 'reply_to'
                ["4a2d6fe0859d4d@example.com"],  # Cambia a la dirección de buzón de entrada de Mailtrap
                reply_to=[email],
            )

            try:
                email.send()
                return redirect(reverse('contact') + '?ok')
            except SMTPException as e:
                # algo ha salido mal
                print(f"Error al enviar el correo: {e}")
                return redirect(reverse('contact') + f'?fail={str(e)}')

    return render(request, "contact/contact.html", {'form': contact_form})