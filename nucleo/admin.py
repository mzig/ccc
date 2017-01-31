from django.contrib import admin

# Register your models here.

from . models import Tag, Lugar, Articulo, Imagen, Galeria, Incrustado



admin.site.register(Tag)
admin.site.register(Lugar)

admin.site.register(Articulo)
admin.site.register(Imagen)
admin.site.register(Galeria)
admin.site.register(Incrustado)