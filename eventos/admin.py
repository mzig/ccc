from django.contrib import admin
# from django.contrib.admin import AdminSite

# Register your models here.

from . models import Expo, Actividad

# class CCCAdminSite(AdminSite):
#     site_header = 'Administración CCC'
#
# admin.site = CCCAdminSite(name='admin')



class ExpoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'fecha_inicio', 'fecha_fin' )



admin.site.register(Expo,ExpoAdmin)


class ActividadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo', 'fecha_inicio', 'fecha_fin' )


admin.site.register(Actividad,ActividadAdmin)


# admin.site.register(Inauguracion)