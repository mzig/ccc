from django.contrib import admin

# Register your models here.

from . models import Expo, Actividad, Inauguracion


admin.site.register(Expo)
admin.site.register(Actividad)
admin.site.register(Inauguracion)