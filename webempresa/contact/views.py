from django.http import HttpResponse
from django.shortcuts import render
from contact.forms import ContactForm


# Create your views here.

def contact(request):
    contact_form = ContactForm
    return render(request, "contact/contact.html", {'form': contact_form})