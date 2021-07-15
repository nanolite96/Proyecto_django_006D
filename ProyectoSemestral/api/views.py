from django.shortcuts import render
from rest_framework import generics
from webRayoMakween.models import Trabajos, contacto
from .serializers import TrabajosSerializers, ContactoSerializers

# Create your views here.

class TrabajosViewSet(generics.ListAPIView):
    queryset = Trabajos.objects.all()
    serializer_class = TrabajosSerializers

class TrabajosCreateViewSet(generics.ListCreateAPIView):
    queryset=Trabajos.objects.all()
    serializer_class=TrabajosSerializers

class TrabajoBuscarViewSet(generics.ListAPIView):
    serializers_class = TrabajosSerializers
    def get_queryset(self):
        nombre_m = self.kwargs['nombre']
        return Trabajos.objects.filter(nombre=nombre_m)
# #################################Contacto############################# #
class ContactoViewSet(generics.ListAPIView):
    queryset = contacto.objects.all()
    serializer_class = ContactoSerializers

class ContactoCreateViewSet(generics.ListCreateAPIView):
    queryset=contacto.objects.all()
    serializer_class=ContactoSerializers

class ContactoBuscarViewSet(generics.ListAPIView):
    serializers_class=ContactoSerializers
    def get_queryset(self):
        nombre = self.kwargs['nombre_cl']
        return contacto.objects.filter(nombre_cl=nombre)