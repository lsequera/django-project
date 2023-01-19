from django.db import models

from django.db.models.fields import CharField, DateTimeField, BooleanField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = CharField(max_length=50)

class Post(models.Model):
    tittle = CharField(max_length=300)
    date = DateTimeField()
    content = CharField(max_length=5000)
    status = BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

class Tag(models.Model):
    tag_name = CharField(max_length=50)

class PostTags(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_body = CharField(max_length=2000)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)


