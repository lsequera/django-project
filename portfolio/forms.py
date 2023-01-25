from django.forms import ModelForm
from .models import Project, Task

class CreateProject(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'url']

class CreateTask(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'importance', 'completed']