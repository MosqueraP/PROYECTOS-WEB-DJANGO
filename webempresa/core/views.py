from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return HttpResponse('Inicio')

def about(request):
    return HttpResponse('Acerca de')

def services(request):
    return HttpResponse('Servicios')

def store(request):
    return HttpResponse('store')

def contact(request):
    return HttpResponse('Contacto')

def blog(request):
    return HttpResponse('Blog')

def sample(request):
    return HttpResponse('Sample')

