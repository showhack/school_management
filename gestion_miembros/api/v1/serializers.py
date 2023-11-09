from rest_framework import serializers

from gestion_miembros.models import GrupoEtario, Pais, Provincia, Municipio, Direccion, Persona, Atleta, Entrenador, \
    Instructor, RelacionEntrenadorGrupoEtario


class GrupoEtarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoEtario
        fields = '__all__'

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = '__all__'

class EntrenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenador
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class RelacionEntrenadorGrupoEtarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelacionEntrenadorGrupoEtario
        fields = '__all__'
