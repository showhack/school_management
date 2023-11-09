from django.contrib import admin

from .models import RelacionGrupoEtarioCualidad, RelacionCualidadEntrenador, \
    Cualidades, RelacionDistribucionCualidades, Distribucion

# Registro de modelos en el panel de administración
admin.site.register(RelacionDistribucionCualidades)
admin.site.register(RelacionCualidadEntrenador)
admin.site.register(Cualidades)
admin.site.register(Distribucion)
admin.site.register(RelacionGrupoEtarioCualidad)
