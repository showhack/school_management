from django.db import models


choice_generos = (
    ('M', 'MASCULINO'),
    ('F', 'FEMENINO')
)

# ------------------------------------------------------------------------------------------
# ****************************************GRUPO ETARIO**************************************
# ------------------------------------------------------------------------------------------


class GrupoEtario(models.Model):
    rango_edad = models.CharField(max_length=50)

# ------------------------------------------------------------------------------------------
# ****************************************DIRECCION*****************************************
# ------------------------------------------------------------------------------------------


class Pais(models.Model):
    nombre = models.CharField(max_length=100)


class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)


class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    Provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)


class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    municipio = models.ForeignKey(Municipio, on_delete=models.RESTRICT)

# ------------------------------------------------------------------------------------------
# ****************************************PERSONA*******************************************
# ------------------------------------------------------------------------------------------


class Persona(models.Model):
    CI = models.CharField(max_length=11, unique=True, primary_key=True)
    nombre = models.CharField(max_length=100)
    genero = models.CharField(
        max_length=10, choices=choice_generos, default='M')
    edad = models.PositiveBigIntegerField()
    activo = models.BooleanField(default=True)

# ------------------------------------------------------------------------------------------
# ****************************************ATLETAS*******************************************
# ------------------------------------------------------------------------------------------


class Atleta(Persona):
    CI = models.ForeignKey(Persona, on_delete=models.RESTRICT, to_field='CI')
    color_de_piel = models.CharField(max_length=30)
    grado_escolar = models.CharField(max_length=15)
    nuevo_ingreso = models.BooleanField(default=True)
    continuante = models.BooleanField(default=True)
    anno_exp_x_deporte = models.SmallIntegerField()
    direccion = models.ForeignKey(Direccion, on_delete=models.RESTRICT)
    vive_con = models.CharField(max_length=255)
    padres_fallecidos = models.BooleanField(default=False)
    ocupacion_padre = models.CharField(max_length=255, default=None)
    ocupacion_madre = models.CharField(max_length=255, default=None)
    grupo_etario = models.ForeignKey(
        GrupoEtario, on_delete=models.SET_NULL, null=True, to_field='CI')

# ------------------------------------------------------------------------------------------
# ****************************************ENTRENADORES**************************************
# ------------------------------------------------------------------------------------------


class Entrenador(Persona):
    CI = models.ForeignKey(Persona, on_delete=models.RESTRICT, to_field='CI')
    anno_exp = models.SmallIntegerField()
    grupo_etario = models.ManyToManyField(
        GrupoEtario, through='RelacionEntrenadorGrupoEtario')


# ------------------------------------------------------------------------------------------
# ****************************************INSTRUCTORES**************************************
# ------------------------------------------------------------------------------------------

class Instructor(Persona):
    pass

# ------------------------------------------------------------------------------------------
# *****************************RELACION ENTRENADOR-GRUPO ETARIO*****************************
# ------------------------------------------------------------------------------------------


class RelacionEntrenadorGrupoEtario(models.Model):
    entrenador = models.ForeignKey(
        Entrenador, on_delete=models.SET_NULL, null=True, to_field='CI')
    grupo_etario = models.ForeignKey(
        GrupoEtario, on_delete=models.SET_NULL, null=True, to_field='rango_edad')


# ------------------------------------------------------------------------------------------
# ****************************RELACION INSTRUCTOR-GRUPO ETARIO*****************************
# ------------------------------------------------------------------------------------------
