from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
from .forms import CreateProject, CreateTask
from .models import Project, Task

def index(request):
    return render(request, 'index.html', {'title':"Takions App"})

def projects(request):
    project_list = Project.objects.all()
    return render(request, 'projects.html', {
        'title':"Takions Projects",
        'projects': project_list
        })

@login_required
def create_project(request):
    if request.method == "GET":
        return render(request, 'create_project.html', {'title':"Takions Projects", 'form': CreateProject})
    else:
        try:
            new_project = Project.objects.create(
                title=request.POST['title'], 
                description=request.POST['description'],
                image='portfolio/images/'+request.POST['image'],
                url=request.POST['url'],
                user=request.user
                )
            new_project.save()
            return redirect('projects')
        except ValueError:
            return render(request, 'create_project.html', {'title':"Takions Projects", 'form': CreateProject, 'error': "Error creating project."})

@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, 'create_task.html', {"form": CreateTask})
    else:
        try:
            new_task = Task.objects.create(
                title = request.POST['title'], 
                description = request.POST['description'],
                importance = request.POST['importance'],
                completed = request.POST['completed'],
                user = request.user
            )
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {"form": CreateTask, "error": "Error creating project."})

