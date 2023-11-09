from rest_framework import serializers
from gestion_cualidades.models import (
    Cualidades,
    Distribucion,
    RelacionDistribucionCualidades,
    RelacionCualidadEntrenador,
    RelacionGrupoEtarioCualidad
)


class CualidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cualidades
        field = '__all__'


class DistribucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribucion
        field = '__all__'


class RelacionDistribucionCualidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelacionDistribucionCualidades
        field = '__all__'


class RelacionCualidadEntrenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelacionCualidadEntrenador
        field = '__all__'


class RelacionGrupoEtarioCualidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelacionGrupoEtarioCualidad
        field = '__all__'
