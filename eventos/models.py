from django.db import models
from autoslug import AutoSlugField
from nucleo.models import Tag, Lugar, Galeria, Incrustado

# Create your models here.


# clases de eventos, expos y actividades

class Expo(models.Model):
    expo = models.CharField(max_length=255, blank=True, unique=True)
    autor = models.CharField(max_length=255, blank=True)
    slug = AutoSlugField(populate_from='expo', unique=True)
    fechaInaugura = models.DateField()
    fechaClausura = models.DateField()
    textoCur = models.TextField(max_length=1500)
    imagen = models.FileField(blank=True, upload_to='static')
    lugar = models.ForeignKey(Lugar, null=True)
    # sala = models.CharField(max_length=20, blank=True, choices=(('SALA1', 'Sala 1'), ('SALA2', 'Sala 2'), ('SALA3', 'Sala 3'), ('SALA4', 'Sala 4'), ('SALA5', 'Sala 5'), ('SALA6', 'Sala 6'), ('SALA7', 'Sala 7'), ('SALA8', 'Sala 8'), ('SALA9', 'Sala 9')))
    tags = models.ManyToManyField(Tag, related_name='expo_tags', blank=True)
    galeria = models.ForeignKey(Galeria, null=True)
    # incrustado (Video url, etc)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.expo

    class Meta:
        ordering = ['expo']
        verbose_name = 'Exposición'
        verbose_name_plural = 'Exposiciones'



class Actividad(models.Model):
    actividad = models.CharField(max_length=255, unique=True)
    realizador = models.CharField(max_length=255, blank=True)
    tipo = models.CharField(max_length=30, choices=(('Educación', 'EDUCACION'), ('Master Class', 'MASTER CLASS'), ('Proyección', 'PROYECCION')), default='EDUCACION')
    inicio = models.DateField(null=True)
    fin = models.DateField(null=True)
    lugar = models.ForeignKey(Lugar, null=True)
    # slug = AutoSlugField(populate_from='actividad', unique=True)
    tags = models.ManyToManyField(Tag, related_name='actividad_tags', blank=True)
    galeria = models.ForeignKey(Galeria, blank=True, null=True)
    imagen = models.FileField(blank=True, upload_to='license')



    def __str__(self):
        return self.actividad

    class Meta:
        ordering = ['actividad']
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'



class Inauguracion(models.Model):
    inauguracion = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.inauguracion

    class Meta:
        ordering = ['inauguracion']
        verbose_name = 'Inauguración'
        verbose_name_plural = 'Inauguraciones'

