from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('ID_usuario', 'nombre_usuario', 'correo_electronico')

@admin.register(Alimentos)
class AlimentosAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "marca",
        "fecha_vencimiento"
    ]

@admin.register(Medicinas)
class MedicinasAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "principio_activo",
        "fecha_vencimiento"
    ]

@admin.register(Juguetes)
class JuguetesAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "precio",
        "cantidad"
    ]

@admin.register(Utensilios)
class JuguetesAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "precio",
        "cantidad",
        "esterilizable"
    ]