from django.db import models

CHOICE_GENEROS = (
    ('M', 'MASCULINO'),
    ('F', 'FEMENINO')
)


# ------------------------------------------------------------------------------------------
# ****************************************GRUPO ETARIO**************************************
# ------------------------------------------------------------------------------------------

class GrupoEtario(models.Model):
    rango_edad = models.CharField(max_length=50, unique=True)


# ------------------------------------------------------------------------------------------
# ****************************************DIRECciON*****************************************
# ------------------------------------------------------------------------------------------

class Pais(models.Model):
    nombre = models.CharField(max_length=100)


class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)


class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)


class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    municipio = models.ForeignKey(Municipio, on_delete=models.RESTRICT)


# ------------------------------------------------------------------------------------------
# ****************************************PERSONA*******************************************
# ------------------------------------------------------------------------------------------

class Persona(models.Model):
    ci = models.CharField(max_length=11, unique=True, primary_key=True, blank=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(
        max_length=10, choices=CHOICE_GENEROS, default='M')
    edad = models.PositiveBigIntegerField()
    activo = models.BooleanField(default=True)


# ------------------------------------------------------------------------------------------
# ****************************************ATLETAS*******************************************
# ------------------------------------------------------------------------------------------

class Atleta(Persona):
    color_de_piel = models.CharField(max_length=30)
    grado_escolar = models.CharField(max_length=15)
    nuevo_ingreso = models.BooleanField(default=True)
    continuante = models.BooleanField(default=True)
    anno_exp_x_deporte = models.SmallIntegerField()
    direccion = models.ForeignKey(Direccion, on_delete=models.RESTRICT, null=True)
    vive_con = models.CharField(max_length=255, null=True, blank=True)
    padres_fallecidos = models.BooleanField(default=False)
    ocupacion_padre = models.CharField(max_length=255, null=True, blank=True)
    ocupacion_madre = models.CharField(max_length=255, null=True, blank=True)
    grupo_etario = models.ForeignKey(
        GrupoEtario, on_delete=models.SET_NULL, null=True)


# ------------------------------------------------------------------------------------------
# ****************************************ENTRENADORES**************************************
# ------------------------------------------------------------------------------------------

class Entrenador(Persona):
    anno_exp = models.SmallIntegerField()
    grupo_etario = models.ManyToManyField(
        GrupoEtario, through='RelacionEntrenadorGrupoEtario')


# ------------------------------------------------------------------------------------------
# ****************************************INSTRUCTORES**************************************
# ------------------------------------------------------------------------------------------

class Instructor(Persona):
    pass


# ------------------------------------------------------------------------------------------
# *****************************RELAciON ENTRENADOR-GRUPO ETARIO*****************************
# ------------------------------------------------------------------------------------------

class RelacionEntrenadorGrupoEtario(models.Model):
    entrenador = models.ForeignKey(
        Entrenador, on_delete=models.SET_NULL, null=True)
    grupo_etario = models.ForeignKey(
        GrupoEtario, on_delete=models.SET_NULL, null=True, to_field='rango_edad')

# ------------------------------------------------------------------------------------------
# ****************************RELAciON INSTRUCTOR-GRUPO ETARIO*****************************
# ------------------------------------------------------------------------------------------
