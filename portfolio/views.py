from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all()
     # Change 'home.html' to 'portfolio/home.html'
     # This happens when you have a home.html file inside a subdirectory with the same
     # name as the app, for example, portfolio/templates/portfolio/home.html. 
     # It's a common convention in Django to prevent template name collisions 
     # between different apps.
    return render(request,'portfolio/home.html', {'projects': projects})
