from django.db import models

# PERSONA------------------------------------------.


class Persona(models.Model):
    CI = models.CharField(max_length=11, unique=True)
    nombre = models.CharField(max_length=100)
    edad = models.PositiveBigIntegerField()
    activo = models.BooleanField(default=True)

# ATLETAS------------------------------.


class Atleta(Persona):
    color_de_piel = models.CharField(max_length=30)
    grado_escolar = models.CharField(max_length=15)
    # nuevo_ingreso = models.BooleanField(default=True)
    # continuante = models.BooleanField(default=True)
    anno_exp_x_deporte = models.SmallIntegerField()

# ENTRENADORES---------------------------------------


class Entrenador(Persona):
    anno_exp = models.SmallIntegerField()


# INSTRUCTORES-------------------------------------------
class Instructor(Persona):
    pass


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
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
