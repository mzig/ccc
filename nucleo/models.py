from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from tinymce.models import HTMLField

from PIL import Image

# from eventos.models import Evento

# Create your models here.


# clases estructurales

class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)
    slug = AutoSlugField(populate_from='tag', default=None)
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
    galeria = models.CharField(max_length=50, unique=False)
    imagen_01 = models.ImageField(upload_to='galerias/', null=True)
    imagen_02 = models.ImageField(upload_to='galerias/', null=True)
    imagen_03 = models.ImageField(upload_to='galerias/', null=True)
    imagen_04 = models.ImageField(upload_to='galerias/', null=True, blank=True)
    imagen_05 = models.ImageField(upload_to='galerias/', null=True, blank=True)
    imagen_06 = models.ImageField(upload_to='galerias/', null=True, blank=True)
    imagen_07 = models.ImageField(upload_to='galerias/', null=True, blank=True)


    def __str__(self):
        return self.galeria

    class Meta:
        ordering = ['galeria']
        verbose_name = 'Galería'
        verbose_name_plural = 'Galerías'


# def imagePathSpaces(self, filename):
#     filebase, extension = filename.split(".")
#     return "%s/%s.%s" % (Evento.titulo, filename, extension)

class Imagen(models.Model):
    imagen = models.ImageField(upload_to='media')
    texto = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.imagen

    class Meta:
        ordering = ['imagen']
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'








class Articulo(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    subtitulo = models.CharField(max_length=320, blank=True)
    hero = models.ImageField(upload_to='media/hero', default=None)
    texto = HTMLField(max_length=25500)
    galerias = models.ForeignKey(Galeria, null=True, blank=True)
    # incrustados
    tags = models.ManyToManyField(Tag, related_name='articulo_tags', blank=True)
    slug = AutoSlugField(populate_from='titulo', unique=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'


class TipoActividad(models.Model):
    tipo = models.CharField(max_length=50, unique=True, default=None)
    slug = AutoSlugField(populate_from='tipo', default=None)

    def __str__(self):
        return self.tipo

    class Meta:
        ordering = ['tipo']
        verbose_name = 'Tipo de actividad'
        verbose_name_plural = 'Tipos de actividades'


class Incrustado(models.Model):
    incrustado = models.CharField(max_length=50, unique=True)
    url = models.URLField(blank=False, null=False)

    def __str__(self):
        return self.incrustado

    class Meta:
        ordering = ['incrustado']
        verbose_name = 'Incrustados'
        verbose_name_plural = 'Incrustados'


#
# class Estadistica(models.Model):
#     estadistica1 = models.CharField(tuple('cantidad', 'numero'), max_length=50, unique=True)
#
#     def __str__(self):
#         return self.estadistica
#
#     class Meta:
#         ordering = ['estadistica']
#         verbose_name = 'Estadástica'
#         verbose_name_plural = 'Estadásticas'


class Publicacion(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    subtitulo = models.CharField(max_length=255, unique=False, blank=True, null=True)
    slug = AutoSlugField(populate_from='titulo', unique=True)

    imagen = models.ImageField(upload_to='publicaciones')
    link = models.URLField(max_length=500, blank=False)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['titulo']
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'

