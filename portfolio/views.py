from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
from .forms import CreateProject, CreateTask, CreateProject2
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
                image=request.FILES['image'],
                url=request.POST['url'],
                user=request.user
                )
            new_project.save()
            return redirect('projects')
        except ValueError:
            return render(request, 'create_project.html', {'title':"Takions Projects", 'form': CreateProject, 'error': "Error creating project."})

@login_required
def create_task(request):
    project_list = Project.objects.filter(user=request.user)
    if request.method == "GET":
        return render(request, 'create_task.html', {"form": CreateTask, 'projects': project_list})
    else:
        try:
            new_task = Task.objects.create(
                title = request.POST['title'], 
                description = request.POST['description'],
                importance = request.POST['importance'],
                completed = request.POST.get('completed', False),
                project = Project.objects.get(pk=int(request.POST.get('project'))),
                user = request.user
            )
            new_task.save()
            return redirect('projects')
        except ValueError:
            return render(request, 'create_task.html', {"form": CreateTask, "error": "Error creating task.", 'projects': project_list})

def detail(request, project_id):
    project_selected = Project.objects.get(pk=project_id)
    task_list = Task.objects.filter(project=project_selected)
    return render(request, 'project_detail.html', {
        'title':"Takions Projects", 
        'project': project_selected,
        'task_list': task_list
        })

