from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
from .models import Project, Task

def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request=request, template_name='projects.html')