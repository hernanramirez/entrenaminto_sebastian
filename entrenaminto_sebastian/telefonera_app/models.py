from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField


class Telefono(models.Model):
    TIPO_CHOICES = Choices('Familia', 'Trabajo')
    tipo = StatusField(choices_name='TIPO_CHOICES')
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)