# Importamos la función para renderizar templates en Django
from django.shortcuts import render

# Esta función es la que llama tu urls.py cuando alguien visita /data_hub/
def data_hub(request):
    """
    Renderiza el template data_hub.html para mostrar el contenido de Firebase.
    """
    # Renderizamos la página HTML que contiene toda la lógica de la interfaz y Firebase.
    # Nota: Django buscará este archivo dentro de las carpetas 'templates' configuradas.
    # Por simplicidad, asumimos que data_hub.html está directamente en la carpeta 
    # django_portfolio, pero en proyectos reales debería estar en 'templates/'.
    # Si te da error, moveremos data_hub.html a una carpeta llamada 'templates'
    return render(request, 'portfolio/data_hub.html', {})