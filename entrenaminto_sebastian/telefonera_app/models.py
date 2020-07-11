from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

class Telefono(models.Model):
    TIPO_CHOICES = Choices('Familia', 'Trabajo')
    tipo = StatusField(choices_name='TIPO_CHOICES')
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    foto = VersatileImageField(
        'Foto',
        upload_to='images/foto',
        blank=True,
        null=True,
        help_text='formato de imagen .jpeg or .png tamańo máximo: 10 MB dimensiones recomendadas: 1372 x 772 px'
    )

    class Meta:
        ordering = ['pk']