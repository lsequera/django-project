from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('projects/', views.projects, name='projects'),
        path('projects/create', views.create_project, name='create_project'),
        path('projects/detail/<int:project_id>', views.detail, name='detail'),
        path('tasks/create', views.create_task, name='create_task')
]