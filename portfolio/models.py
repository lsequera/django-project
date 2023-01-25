from django.db import models

from django.db.models.fields import CharField, URLField, DateTimeField, DecimalField, BooleanField, DateField
from django.db.models.fields.files import ImageField
from django.utils import timezone
from datetime import date

# Create your models here.


class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=500)
    image = ImageField(upload_to='portofolio/images')
    date = DateField(default=date.today)
    url = URLField(blank=True)

    def __str__(self) -> str:
        return super().__str__()

class Task(models.Model):
    title = CharField(max_length=200)
    description = CharField(max_length=500)
    importance = DecimalField(max_digits=3, decimal_places=2, default=0.00)
    creation_date = DateTimeField(default=timezone.now)
    completed = BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()

