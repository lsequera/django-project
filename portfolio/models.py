from django.db import models

from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=500)
    image = ImageField(upload_to='portofolio/images')
    url = URLField(blank=True)

    def __str__(self) -> str:
        return super().__str__()

class Task(models.Model):
    title = CharField(max_length=200)
    decription = CharField(max_length=500)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()

