from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
from .forms import CreateProject, Task

def index(request):
    return render(request, 'index.html', {'title':"Takions App"})

def projects(request):
    return render(request, 'projects.html', {'title':"Takions Projects"})

@login_required
def create_project(request):
    if request.method == "GET":
        return render(request, 'create_project.html', {"form": CreateProject})
    else:
        try:
            form = CreateProject(request.POST)
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect('projects')
        except ValueError:
            return render(request, 'create_project.html', {"form": CreateProject, "error": "Error creating project."})
