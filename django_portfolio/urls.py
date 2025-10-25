"""
URL configuration for django_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import  include,path
#from django.conf.urls.static import static
#from django.conf import settings
#from portfolio import views
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    
    # 1. Rutas para la página principal y el blog (probablemente ya están bien)
    path('', views.home, name='home'),
    path('blog/', include ('blog.urls')),
    # 2. Nueva ruta para el Data Hub. Usamos 'include' para que las rutas
    # de la aplicación 'portfolio' manejen todo lo que empiece con 'data-hub/'.
    # Si la ruta es solo 'data-hub/', esto apuntará a la URL principal de portfolio/urls.py
        # path('data_hub/', TemplateView.as_view(template_name='data_hub.html'), name='data_hub'),
    #path('data-hub/', include('portfolio.urls')), 

    # Ruta para el Data Hub
    # La ruta completa será '/data-hub/' debido al include en urls.py principal
    path('', views.data_hub_view, name='data_hub')

]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)