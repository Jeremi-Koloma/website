from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    published = models.BooleanField(default = False) # Par défaut l'article n'est pas publier
    date = models.DateField(blank = True) # Ce champ peut-être vide
    content = models.TextField()
    description = models.TextField()