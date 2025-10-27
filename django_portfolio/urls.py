# Importaciones necesarias para la configuración de URLs de Django

from django.contrib import admin            # Para incluir la interfaz de administración de Django (admin/).
from django.urls import include, path       # Función principal para definir patrones de URL.
from django.conf.urls.static import static  # Utilizado para servir archivos estáticos y de medios en modo de desarrollo.
from django.conf import settings            # Accede a la configuración definida en settings.py (necesario para las URLs estáticas/media).
from portfolio import views                 # Importa las vistas de tu aplicación 'portfolio' (e.g., la vista 'home').

# Eliminamos la importación de TemplateView, ya que usaremos nuestra vista personalizada.
# from django.views.generic import TemplateView 

urlpatterns = [
    # Ruta de administración de Django
    path('admin/', admin.site.urls),

    # Ruta principal (Home / Portafolio). Usa la función 'home' en portfolio/views.py.
    # Esta es la página de inicio que lista tus proyectos.
    path('', views.home, name='home'),

    # ----------------------------------------------------------------------------------
    # RUTA: Data Hub (Componente React)
    # ¡CAMBIO CLAVE! Usamos DataHubView en lugar de TemplateView.
    # DataHubView inyecta las variables globales de Firebase (__firebase_config, etc.) 
    # en el contexto del template, resolviendo el error de inicialización.
    path('data_hub/', views.DataHubView.as_view(), name='data_hub'),
]

# Configuración para servir archivos de Medios (MEDIA files) durante el desarrollo.
# Esto es crucial para que las imágenes (archivos adjuntos) de mis proyectos se muestren correctamente.
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
