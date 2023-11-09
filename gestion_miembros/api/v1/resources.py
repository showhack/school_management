# from core.api.permissions import IsAuthenticatedOnRetrieve, NoDeletes
from rest_framework import viewsets

from core.api.permissions import IsAuthenticatedOnRetrieve, NoDeletes
from gestion_miembros.models import GrupoEtario, Pais, Provincia, Municipio, Direccion, Persona, Atleta, Entrenador, \
    Instructor, RelacionEntrenadorGrupoEtario
from .serializers import GrupoEtarioSerializer, PaisSerializer, ProvinciaSerializer, MunicipioSerializer, \
    DireccionSerializer, PersonaSerializer, AtletaSerializer, EntrenadorSerializer, InstructorSerializer, \
    RelacionEntrenadorGrupoEtarioSerializer


class GrupoEtarioResource(viewsets.ModelViewSet):
    queryset = GrupoEtario.objects.all()
    serializer_class = GrupoEtarioSerializer
    permission_classes = [IsAuthenticatedOnRetrieve, NoDeletes]


class PaisResource(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    # permission_classes = [IsAuthenticatedOnRetrieve, NoDeletes]


class ProvinciaResource(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    # permission_classes = [IsAuthenticatedOnRetrieve, NoDeletes]


class MunicipioResource(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    # permission_classes = [IsAuthenticatedOnRetrieve, NoDeletes]


class DireccionResource(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
    # permission_classes = [IsAuthenticatedOnRetrieve, NoDeletes]


class PersonaResource(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [IsAuthenticatedOnRetrieve, NoDeletes]


class AtletaResource(viewsets.ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer
    # permission_classes = [IsAuthenticatedOnRetrieve, NoDeletes]


class EntrenadorResource(viewsets.ModelViewSet):
    queryset = Entrenador.objects.all()
    serializer_class = EntrenadorSerializer
    # permission_classes = [IsAuthenticatedOnRetrieve, NoDeletes]


class InstructorResource(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    # permission_classes = [IsAuthenticatedOnRetrieve, NoDeletes]


class RelacionEntrenadorGrupoEtarioResource(viewsets.ModelViewSet):
    queryset = RelacionEntrenadorGrupoEtario.objects.all()
    serializer_class = RelacionEntrenadorGrupoEtarioSerializer
    # permission_classes = [IsAuthenticatedOnRetrieve, NoDeletes]
