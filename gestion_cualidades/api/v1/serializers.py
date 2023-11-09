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
    entrenador = serializers.SerializerMethodField(read_only=False)
    grupo_etario = serializers.SerializerMethodField(read_only=False)

    class Meta:
        model = Cualidades
        fields = [
            'nombre',
            'entrenador',
            'grupo_etario',
        ]

    def get_entrenador(self, obj):
        entrenador = obj.entrenador
        serializer = EntrenadorSerializer(entrenador, many=True, context=self.context)
        return serializer.data

    def get_grupo_etario(self, obj):
        grupo_etario = obj.grupo_etario
        serializer = GrupoEtarioSerializer(grupo_etario, many=True, context=self.context)
        return serializer.data


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
