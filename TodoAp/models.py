from pyexpat import model
from django.db import models

# Create your models here.
class Todoapp(models.Model):
    content = models.TextField()