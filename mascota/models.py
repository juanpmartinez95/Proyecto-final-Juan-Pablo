from django.db import models
from django.utils import timezone


class MascotaCategoria(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "categoría de mascotas"
        verbose_name_plural = "categorías de mascotas"

class Mascota(models.Model):
    categoria_id = models.ForeignKey(
        MascotaCategoria, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="categoría de mascota"
    )
    adoptada = models.BooleanField(default=False)
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    tamano = models.CharField(max_length=100)
    edad = models.IntegerField()
    descripcion = models.TextField(null=True, blank=True, verbose_name="descripción")
    fecha_actualizacion = models.DateField(
        null=True, blank=True, default=timezone.now, editable=False, verbose_name="fecha de actualización"
    )
    foto = models.ImageField(upload_to='mascotas/', null=True, blank=True, verbose_name="foto")

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "mascota"
        verbose_name_plural = "mascotas"