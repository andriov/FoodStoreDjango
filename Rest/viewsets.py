from rest_framework import generics
from rest_framework import viewsets
from .serializers import PersonaSerializer
from Principal.models import Persona

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer 

