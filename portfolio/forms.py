from django import forms
from django.forms import ModelForm
from .models import Project, Task

class CreateProject(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea, max_length=500)
    image = forms.FileField(label='Image File')
    url = forms.URLField(label='Project URL')

class CreateTask(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea, max_length=500)
    importance = forms.DecimalField(label='Priority', max_value=1.00, min_value=0.00, max_digits=3, decimal_places=2)
    completed = forms.BooleanField(label='Completed')
    
        