from django.db import models
from apps.gestion_miembros.models import Entrenador


# ----------------- DISTRIBUCION DE ACENTOS -----------------

# Modelo para Categorías de Distribución de Acentos.--------------------------------------

class DistribucionAcentosCategoria(models.Model):
    nombre = models.CharField(max_length=100)


# Modelo para Subcategorías de Distribución de Acentos.-------------------------------


class DistribucionAcentosSubCategoria(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        DistribucionAcentosCategoria, on_delete=models.CASCADE)

    # Relaciones con modelos que aun no existen
    # grupo_etario = models.ManyToManyField('gestion_personas.GrupoEtario')
    # profesor = models.ManyToManyField()
    # instructor = models.ManyToManyField('gestion_personas.Instructor')


class DistribucionAcentosPrioridades(models.Model):
    """
    Modelo para Prioridades de Distribución de Acentos.
    """
    nombre = models.CharField(max_length=100)
    subcategorias = models.ManyToManyField(
        DistribucionAcentosSubCategoria, through='DistribucionAcentosRelacionPrioridad', related_name='prioridades')


class DistribucionAcentosRelacionPrioridad(models.Model):
    """
    Modelo para la Relación entre Subcategorías y Prioridades de Distribución de Acentos.
    """
    subcategoria = models.ForeignKey(
        DistribucionAcentosSubCategoria, on_delete=models.CASCADE)
    prioridad = models.ForeignKey(
        DistribucionAcentosPrioridades, on_delete=models.CASCADE)
    mes = models.CharField(max_length=50)


# ----------------- DISTRIBUCION DEL VOLUMEN SEMANAL Y % VOLUMEN POR CONTENIDOS -----------------
class DistribucionVolSemNXContenidoCualidad(models.Model):
    """
    Modelo para Cualidades de Distribución de Volumen Semanal y % de Volumen por Contenidos.
    """
    nombre = models.CharField(max_length=100)

    # Relaciones con modelos que aun no existen
    # grupo_etario = models.ManyToManyField('gestion_personas.GrupoEtario')
    # profesor = models.ManyToManyField('gestion_personas.Profesor')
    # instructor = models.ManyToManyField('gestion_personas.Instructor')


class DistribucionVolSemNXContenidoDistribucion(models.Model):
    """
    Modelo para Distribuciones de Volumen Semanal y % de Volumen por Contenidos.
    """
    nombre = models.CharField(max_length=100)


class DistribucionVolSemNXRelacion(models.Model):
    """
    Modelo para la Relación entre Cualidades y Distribuciones de Volumen Semanal y % de Volumen por Contenidos.
    """
    cualidad = models.ForeignKey(
        DistribucionVolSemNXContenidoCualidad, on_delete=models.CASCADE)
    distribucion = models.ForeignKey(
        DistribucionVolSemNXContenidoDistribucion, on_delete=models.CASCADE)
    esta_marcado = models.BooleanField(default=False)
    porciento = models.DecimalField(max_digits=5, decimal_places=2)
