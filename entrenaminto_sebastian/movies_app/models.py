from django.db import models
from model_utils.fields import StatusField
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

# Create your models here.

class Year(models.Model):
    year = models.CharField(max_length=4)

    def __str__(self):
        return u'%s' % (self.year)

class Movie(models.Model):
    nombre = models.CharField(max_length=100)
    año = models.ForeignKey( Year, on_delete=models.CASCADE, null=True, blank=True)
    director = models.CharField(max_length=100)
    poster = VersatileImageField(
        'Poster',
        upload_to='images/poster',
        blank=True,
        null=True,
        help_text='Insertar poster en formato .jpeg or .png | Tamaño máximo: 10 MB | Dimensiones recomendadas: 1372 x 772 px'
    )

    def __str__(self):
        return u'%s' % (self.nombre)