from django.shortcuts import render
from .models import Project

from django.views.generic import TemplateView # Necesitas importar esto
from django.conf import settings # Necesitas importar esto

class DataHubView(TemplateView):
    """
    Vista personalizada para el Data Hub que inyecta las variables de configuración
    de Firebase necesarias para el frontend.
    """
    #  template_name = 'portfolio/templates/data_hub.html'
    template_name = 'data_hub.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Estas variables son inyectadas por el entorno. 
        # Si no existen (como en un entorno local), usamos valores seguros.
        context['firebase_config'] = getattr(settings, '__firebase_config', '{}')
        context['app_id'] = getattr(settings, '__app_id', 'default-app-id')
        context['initial_auth_token'] = getattr(settings, '__initial_auth_token', 'null')

        return context
    
# Create your views here.
def home(request):
    projects = Project.objects.all()
     # Change 'home.html' to 'portfolio/home.html'
     # This happens when you have a home.html file inside a subdirectory with the same
     # name as the app, for example, portfolio/templates/portfolio/home.html. 
     # It's a common convention in Django to prevent template name collisions 
     # between different apps.
    return render(request,'portfolio/home.html', {'projects': projects})
