from rest_framework import viewsets
from .serializers import GrupoEtarioSerializer, PaisSerializer, ProvinciaSerializer, MunicipioSerializer, DireccionSerializer, PersonaSerializer, AtletaSerializer, EntrenadorSerializer, InstructorSerializer, RelacionEntrenadorGrupoEtarioSerializer
from gestion_miembros.models import GrupoEtario, Pais, Provincia, Municipio, Direccion, Persona, Atleta, Entrenador, Instructor, RelacionEntrenadorGrupoEtario


class GrupoEtarioResource(viewsets.ModelViewSet):
    queryset = GrupoEtario.objects.all()
    serializer_class = GrupoEtarioSerializer


class PaisResource(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer


class ProvinciaResource(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer


class MunicipioResource(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer


class DireccionResource(viewsets.ModelViewSet):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer


class PersonaResource(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer


class AtletaResource(viewsets.ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer


class EntrenadorResource(viewsets.ModelViewSet):
    queryset = Entrenador.objects.all()
    serializer_class = EntrenadorSerializer


class InstructorResource(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class RelacionEntrenadorGrupoEtarioResource(viewsets.ModelViewSet):
    queryset = RelacionEntrenadorGrupoEtario.objects.all()
    serializer_class = RelacionEntrenadorGrupoEtarioSerializer
