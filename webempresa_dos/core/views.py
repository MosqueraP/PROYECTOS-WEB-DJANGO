from django.views.generic.base import TemplateView

from django.shortcuts import render

# Vista encarda de mostrar solo un template
class HomePageView(TemplateView):
    template_name = "core/home.html"

class SampleView(TemplateView):
    template_name = "core/sample.html"