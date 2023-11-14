from django.contrib import admin
from .models import GrupoEtario, Pais, Provincia, Municipio, Direccion, Persona, Atleta, Entrenador, RelacionEntrenadorGrupoEtario

# Registro de modelos en el panel de administración
admin.site.register(GrupoEtario)
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Municipio)
admin.site.register(Direccion)
admin.site.register(Atleta)
admin.site.register(Entrenador)
admin.site.register(Persona)
admin.site.register(RelacionEntrenadorGrupoEtario)
