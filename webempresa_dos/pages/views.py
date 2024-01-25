from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from pages.models import Page
from pages.forms import PageForm 

# Create your views here.
# Mixin para proteccion de paginas, solo accesos a usuarios staff
class StaffRequiredMixin(object):
    '''
    Este mixin requerirá que el usuario sea mienbro del staff para
    para ver los contenidos de la paginas
    '''
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
    



# Vista encargada de ver el listado de paginas
class PageListView(ListView):
    model = Page

# Vista encargada de ver una pagina
class PageDetailView(DetailView):
    model = Page

# Vista encargada de crear paginas
class PageCreateView(StaffRequiredMixin, CreateView):
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