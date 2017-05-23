from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from nucleo.models import Tag, Lugar, Galeria, Incrustado, TipoActividad #Estadistica
from embed_video.fields import EmbedVideoField
from PIL import Image

# Create your models here.


# clases de eventos, expos y actividades
class Evento(models.Model):
    titulo = models.CharField(max_length=255, unique=True, null=True)
    subtitulo = models.CharField(max_length=255, blank=True)
    slug = AutoSlugField(populate_from='titulo', unique=True, null=True)

    # imagen = models.ImageField(upload_to=upload_location(params))

    fecha_inicio = models.DateField(null=True)
    fecha_fin = models.DateField(null=True)
    desc_corta = models.TextField(max_length=350, blank=True, null=True)
    lugar = models.ForeignKey(Lugar, blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='expo_tags', blank=True)
    video = EmbedVideoField(blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        abstract = True
        ordering = ['titulo']

    # def upload_location(instance, filename):
    #     # return "%s/%s" %(instance.slug, filename)
    #     path = "media/" + instance.slug
    #     format = instance.slug + instance.file_extension
    #     return os.path.join(path, format)

class Expo(Evento):
    texto_curatorial = HTMLField(max_length=25500)
    imagen = models.ImageField(upload_to='expos')
    galeria = models.ForeignKey(Galeria, null=True, blank=True)
    # incrustado (Video url, etc)
    # estadisticas = models.ForeignKey(Estadistica, null=True, blank=True)
    carrusel = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.expo

    class Meta:
        # ordering = ['expo']
        verbose_name = 'Exposición'
        verbose_name_plural = 'Exposiciones'



class Actividad(Evento):
    tipo = models.ForeignKey(TipoActividad, related_name='tipo_actividad', blank=False, default=None)
    # tipo = models.CharField(max_length=30, choices=(('Educación', 'EDUCACION'), ('Master Class', 'MASTER CLASS'), ('Proyección', 'PROYECCION')), default='EDUCACION')
    texto = HTMLField(max_length=25500, blank=True)
    # imagen = models.ImageField(blank=True, upload_to=upload_location)
    imagen = models.ImageField(blank=True, upload_to='acts')
    tags = models.ManyToManyField(Tag, related_name='actividad_tags', blank=True)
    # galeria = models.ForeignKey(Galeria, blank=True, null=True)

    # def __str__(self):
    #     return self.actividad

    class Meta:
        # ordering = ['actividad']
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'



# class Inauguracion(models.Model):
#     inauguracion = models.CharField(max_length=50, unique=True)
#
#     def __str__(self):
#         return self.inauguracion
#
#     class Meta:
#         ordering = ['inauguracion']
#         verbose_name = 'Inauguración'
#         verbose_name_plural = 'Inauguraciones'

