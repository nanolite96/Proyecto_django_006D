from django.db import models
from webRayoMakween.models import Trabajos, contacto
from rest_framework import serializers

class TrabajosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trabajos
        fields = ["codigo","diagnostico","fecha","descripcion","nombre"]

class ContactoSerializers(serializers.ModelSerializer):
    class Meta:
        model = contacto
        fields = ["nombre_cl","asunto","sugerencia"]