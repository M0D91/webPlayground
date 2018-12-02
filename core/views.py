from django.shortcuts import render
from django.views.generic.base import TemplateView

# Forma basada en funciones FBV
#def sample(request):  
    # return render(request, "core/sample.html")

# Forma basada en Clases CBV
class HomePageView(TemplateView):  
    template_name = 'core/home.html'

    # Se puede sobreescribir el contexto para añadir contenido de esta forma
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Mi web playground'
    #     return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Mi Web Playground'})

class SamplePageView(TemplateView):
    template_name = 'core/sample.html'