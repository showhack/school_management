from rest_framework import viewsets
from .serializers import (
    CualidadesSerializer,
    DistribucionSerializer,
    RelacionDistribucionCualidadesSerializer,
    RelacionCualidadEntrenadorSerializer,
    RelacionGrupoEtarioCualidadSerializer
)
from gestion_cualidades.models import (
    Cualidades,
    Distribucion,
    RelacionDistribucionCualidades,
    RelacionCualidadEntrenador,
    RelacionGrupoEtarioCualidad
)


class CualidadesResource(viewsets.ModelViewSet):
    queryset = Cualidades.objects.all()
    serializer_class = CualidadesSerializer


class DistribucionResource(viewsets.ModelViewSet):
    queryset = Distribucion.objects.all()
    serializer_class = DistribucionSerializer


class RelacionDistribucionCualidadesResource(viewsets.ModelViewSet):
    queryset = RelacionDistribucionCualidades.objects.all()
    serializer_class = RelacionDistribucionCualidadesSerializer


class RelacionCualidadEntrenadorResource(viewsets.ModelViewSet):
    queryset = RelacionCualidadEntrenador.objects.all()
    serializer_class = RelacionCualidadEntrenadorSerializer


class RelacionGrupoEtarioCualidadesResource(viewsets.ModelViewSet):
    queryset = RelacionGrupoEtarioCualidad.objects.all()
    serializer_class = RelacionGrupoEtarioCualidadSerializer
