from django.shortcuts import render
from services import views

# Create your views here.

def services(request):
    return render(request, 'services/services.html')