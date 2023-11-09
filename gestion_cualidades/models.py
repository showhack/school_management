from django.db import models
from gestion_miembros.models import (GrupoEtario, Instructor, Entrenador)

# Create your models here.


class Cualidades(models.Model):
    nombre = models.CharField(max_length=255)
    entrenador = models.ManyToManyField(
        Entrenador, through='RelacionCualidadEntrenador')
    grupo_etario = models.ManyToManyField(
        GrupoEtario, through='RelacionGrupoEtarioCualidad')


class Distribucion(models.Model):
    nombre = models.CharField(max_length=255)
    cualidad = models.ManyToManyField(
        Cualidades, through='RelacionDistribucionCualidades')


class RelacionDistribucionCualidades(models.Model):
    distribucion = models.ForeignKey(
        Distribucion, on_delete=models.SET_NULL, null=True)
    cualidad = models.ForeignKey(
        Cualidades, on_delete=models.SET_NULL, null=True)


class RelacionCualidadEntrenador(models.Model):
    entrenador = models.ForeignKey(
        Entrenador, on_delete=models.SET_NULL, null=True)
    cualidad = models.ForeignKey(
        Cualidades, on_delete=models.SET_NULL, null=True)


class RelacionGrupoEtarioCualidad(models.Model):
    cualidad = models.ForeignKey(
        Cualidades, on_delete=models.SET_NULL, null=True)
    grupo_etario = models.ForeignKey(
        GrupoEtario, on_delete=models.SET_NULL, null=True)
