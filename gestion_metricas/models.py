from django.db import models


# ----------------- DISTRIBUCION DE ACENTOS -----------------
class DistribucionAcentosCategoria(models.Model):
    """
    Modelo para Categorías de Distribución de Acentos.
    """
    nombre = models.CharField(max_length=100)

class DistribucionAcentosSubCategoria(models.Model):
    """
    Modelo para Subcategorías de Distribución de Acentos.
    """
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(DistribucionAcentosCategoria, on_delete=models.CASCADE)

    # Relaciones con modelos que aun no existen
    # grupo_etario = models.ManyToManyField('gestion_personas.GrupoEtario')
    # profesor = models.ManyToManyField('gestion_personas.Profesor')
    # instructor = models.ManyToManyField('gestion_personas.Instructor')

class DistribucionAcentosPrioridades(models.Model):
    """
    Modelo para Prioridades de Distribución de Acentos.
    """
    nombre = models.CharField(max_length=100)
    subcategorias = models.ManyToManyField(DistribucionAcentosSubCategoria, 
                through='DistribucionAcentosRelacionPrioridad', related_name='prioridades')

class DistribucionAcentosRelacionPrioridad(models.Model):
    """
    Modelo para la Relación entre Subcategorías y Prioridades de Distribución de Acentos.
    """
    subcategoria = models.ForeignKey(DistribucionAcentosSubCategoria, on_delete=models.CASCADE)
    prioridad = models.ForeignKey(DistribucionAcentosPrioridades, on_delete=models.CASCADE)
    mes = models.CharField(max_length=50)