from rest_framework import serializers
from gestion_cualidades.models import (
    Cualidades,
    Distribucion,
    RelacionDistribucionCualidades,
    RelacionCualidadEntrenador,
    RelacionGrupoEtarioCualidad
)
from gestion_miembros.api.v1.serializers import EntrenadorSerializer, GrupoEtarioSerializer

class CualidadesSerializer(serializers.ModelSerializer):
    entrenador = EntrenadorSerializer(many=True, read_only=True)
    grupo_etario = GrupoEtarioSerializer(many=True, read_only=True)

    class Meta:
        model = Cualidades
        fields = ['nombre', 'entrenador', 'grupo_etario']

class DistribucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribucion
        fields = '__all__'

class RelacionDistribucionCualidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelacionDistribucionCualidades
        fields = '__all__'

class RelacionCualidadEntrenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelacionCualidadEntrenador
        fields = '__all__'

class RelacionGrupoEtarioCualidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelacionGrupoEtarioCualidad
        fields = '__all__'
