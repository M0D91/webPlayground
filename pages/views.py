from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

class StaffRequiredMixin(object):
    """
    Los mixins son clases con funciones concretas que podremos reutilizar para
    sobreescribir metodos por defecto de otras clases
    """

    """
    El method decorator es necesario para que django permita decorar metodos 
    internos propios como el dispatch
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        # print(request.user)
        # if not request.user.is_staff:
        #     return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class PagesListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

class PageCreate(StaffRequiredMixin,CreateView):
    model = Page
    form_class = PageForm
    # La clase PageForm ya incluye el campo fields, asi que podemos quitarlo
    # fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def  get_success_url (self):
        return reverse_lazy('pages:update',args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')


# @method_decorator(staff_member_required, name='dispatch')
# al usar directamente el decorador antes de una funcion e indicarle con 
# name el parametro a modificar, podemos aplicar las comprobaciones a 
# las vistas que nos interesen
#
# existen otro par de funciones decoradoras: 
# login_required
# permission_required
