from rest_framework import serializers
from Principal.models import Persona

class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Persona
        fields= ("cedulaPer","apellidoPer","nombrePer")