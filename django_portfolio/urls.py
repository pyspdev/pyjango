# Importaciones necesarias para la configuración de URLs de Django

from django.contrib import admin            # Para incluir la interfaz de administración de Django (admin/).
from django.urls import path                # Función principal para definir patrones de URL.
from django.conf.urls.static import static  # Utilizado para servir archivos estáticos y de medios en modo de desarrollo.
from django.conf import settings            # Accede a la configuración definida en settings.py (necesario para las URLs estáticas/media).
from portfolio import views                 # Importa las vistas de tu aplicación 'portfolio' (e.g., la vista 'home').

# Importamos TemplateView: 
# Es una vista genérica que sirve una plantilla directamente. 
# La usamos específicamente para cargar 'data_hub_react.html' (donde está mi app React) 
# sin tener que escribir una función de vista adicional en views.py.
from django.views.generic import TemplateView 

urlpatterns = [
    # Ruta de administración de Django
    path('admin/', admin.site.urls),
    
    # Ruta principal (Home / Portafolio). Usa la función 'home' en portfolio/views.py.
    # Esta es la página de inicio que lista tus proyectos.
    path('', views.home, name='home'),
    
    # ----------------------------------------------------------------------------------
    # RUTA: Data Hub (Componente React)
    # Define la URL '/data_hub/' que cargará el archivo data_hub_react.html, 
    # funcionando como el contenedor para la aplicación de React.
    # El nombre 'data_hub' es usado por la etiqueta {% url 'data_hub' %} en home.html.
    # ----------------------------------------------------------------------------------
    path('data_hub/', TemplateView.as_view(template_name='portfolio/data_hub_react.html'), name='data_hub'),
]

# Configuración para servir archivos de Medios (MEDIA files) durante el desarrollo.
# Esto es crucial para que las imágenes (archivos adjuntos) de mis proyectos se muestren correctamente.
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
