from django.db import models
from model_utils.fields import StatusField

# Create your models here.
class Movie(models.Model):
    nombre = models.CharField(max_length=100)
    año = models.IntegerField(max_length=4)
    director = models.CharField(max_length=100)
