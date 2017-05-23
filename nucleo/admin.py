from django.contrib import admin
# from django.contrib.admin import AdminSite
# Register your models here.
from embed_video.admin import AdminVideoMixin

from . models import Tag, Lugar, Articulo, Imagen, Galeria, TipoActividad, Publicacion, Video, Incrustado

# class CCCAdminSite(AdminSite):
#     site_header = 'Administración CCC'
#
# admin.site = CCCAdminSite(name='admin')



class TagAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag, TagAdmin)


class LugarAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lugar, LugarAdmin)


class ArticuloAdmin(admin.ModelAdmin):
    pass


admin.site.register(Articulo, ArticuloAdmin)


class ImagenAdmin(admin.ModelAdmin):
    pass


admin.site.register(Imagen, ImagenAdmin)


class GaleriaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Galeria, GaleriaAdmin)


class TipoActividadAdmin(admin.ModelAdmin):
    pass


admin.site.register(TipoActividad, TipoActividadAdmin)


class PublicacionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Publicacion, PublicacionAdmin)


class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Video, VideoAdmin)


# admin.site.register(Incrustado)