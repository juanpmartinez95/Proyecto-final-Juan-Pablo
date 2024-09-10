from django.contrib import admin
from . import models

admin.site.site_title = "Mascotas"

class MascotaCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    list_display_links = ("nombre",)

class MascotaAdmin(admin.ModelAdmin):
    list_display = (
        "categoria_id",
        "nombre",
        "especie",
        "tamano",
        "edad",
        "descripcion",
        "fecha_actualizacion",
    )
    list_display_links = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("categoria_id", "nombre")
    list_filter = ("categoria_id",)
    date_hierarchy = "fecha_actualizacion"

admin.site.register(models.MascotaCategoria, MascotaCategoriaAdmin)
admin.site.register(models.Mascota, MascotaAdmin)