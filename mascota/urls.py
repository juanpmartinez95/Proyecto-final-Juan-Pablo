from django.urls import path
from .views import *

app_name = 'mascota'

urlpatterns = [
    path('crear/', mascota_create, name='mascota_create'),
    path('lista/', mascota_list, name='lista_mascotas'),
    path('detalle/<int:pk>/', mascota_detail, name='detalle_mascota'),
    path('actualizar/<int:pk>/', mascota_update, name='actualizar_mascota'),
    path('eliminar/<int:pk>/', mascota_delete, name='mascota_confirm_delete'),
]