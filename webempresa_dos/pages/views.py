from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from pages.models import Page

# Create your views here.

# Vista encargada de ver el listado de paginas
class PageListView(ListView):
    model = Page

# Vista encargada de ver una pagina
class PageDetailView(DetailView):
    model = Page

# Vista encargada de crear paginas
class PageCreateView(CreateView):
    model = Page
    fields = ['title', 'content', 'order'] # campos a llenar
