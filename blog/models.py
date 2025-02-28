from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField()


# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null = True) # Clé étrangère
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    published = models.BooleanField(default = False) # Par défaut l'article n'est pas publier
    date = models.DateField(blank = True, null = True) # Ce champ peut-être vide
    content = models.TextField()
    description = models.TextField()