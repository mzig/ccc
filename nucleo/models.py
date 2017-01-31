from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.


# clases estructurales

class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)
    # slug = AutoSlugField(populate_from='tag')
    help_text = 'Etiqueta para configuración de URL.'

    def __str__(self):
        return self.tag

    class Meta:
        ordering = ['tag']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'



class Lugar(models.Model):
    lugar = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=50, choices=(('Sala', 'SALA'), ('Patio', 'PATIO')), default='SALA')
    # slug +
    # galeria +

    def __str__(self):
        return self.lugar

    class Meta:
        ordering = ['lugar']
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'



class Galeria(models.Model):
    galeria = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.galeria

    class Meta:
        ordering = ['galeria']
        verbose_name = 'Galería'
        verbose_name_plural = 'Galerías'






class Articulo(models.Model):
    articulo = models.CharField(max_length=255, unique=True)
    texto = models.TextField(max_length=2000, blank=True)
    galerias = models.ForeignKey(Galeria, null=True)
    # incrustados
    tags = models.ManyToManyField(Tag, related_name='articulo_tags', blank=True)
    # slugs

    def __str__(self):
        return self.articulo

    class Meta:
        ordering = ['articulo']
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'



class Incrustado(models.Model):
    incrustado = models.CharField(max_length=50, unique=True)
    url = models.URLField(blank=False, null=False)

    def __str__(self):
        return self.incrustado

    class Meta:
        ordering = ['incrustado']
        verbose_name = 'Incrustados'
        verbose_name_plural = 'Incrustados'