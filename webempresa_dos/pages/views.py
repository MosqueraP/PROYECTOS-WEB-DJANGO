from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from pages.models import Page
from pages.forms import PageForm 

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
    form_class = PageForm # Viene con con los campos fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')

# Actualizar o editar paginas

class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
    


class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')