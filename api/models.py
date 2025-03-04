from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.EmailField()
    password = models.TextField()

    # string version
    def __str__(self):
        return self.first_name