from rest_framework import routers
from .resources import (
    CualidadesResource,
    DistribucionResource,
    RelacionGrupoEtarioCualidadesResource,
    RelacionCualidadEntrenadorResource,
    RelacionDistribucionCualidadesResource,
)

router = routers.DefaultRouter()

router.register(r'cualidades', CualidadesResource)
router.register(r'distribucion', DistribucionResource)
router.register(r'relacion_grupo_etario_cualidades',
                RelacionGrupoEtarioCualidadesResource)
router.register(r'relacion_cualidades_entrenador',
                RelacionCualidadEntrenadorResource)
router.register(r'relacion_distribucion_cualidades',
                RelacionDistribucionCualidadesResource)
