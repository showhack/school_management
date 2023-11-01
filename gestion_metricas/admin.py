from django.contrib import admin
from .models import (DistribucionAcentosCategoria, DistribucionAcentosSubCategoria,
                    DistribucionAcentosPrioridades, DistribucionAcentosRelacionPrioridad,
                    DistribucionVolSemNXContenidoCualidad, DistribucionVolSemNXContenidoDistribucion,
                    DistribucionVolSemNXRelacion)

# Registro de modelos en el panel de administración
admin.site.register(DistribucionAcentosCategoria)
admin.site.register(DistribucionAcentosSubCategoria)
admin.site.register(DistribucionAcentosPrioridades)
admin.site.register(DistribucionAcentosRelacionPrioridad)
admin.site.register(DistribucionVolSemNXContenidoCualidad)
admin.site.register(DistribucionVolSemNXContenidoDistribucion)
admin.site.register(DistribucionVolSemNXRelacion)
