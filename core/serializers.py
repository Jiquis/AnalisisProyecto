from rest_framework import serializers
from .models import *

class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentos
        fields = ['id', 'nombre', 'fecha_vencimiento']

class MedicinasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicinas
        fields = ['id', 'nombre', 'principio_activo', 'fecha_vencimiento']

class JuguetesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juguetes
        fields = ['id', 'nombre', 'precio']

class UtensiliosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utensilios
        fields = ['id', 'nombre', 'precio', 'estelirizable']