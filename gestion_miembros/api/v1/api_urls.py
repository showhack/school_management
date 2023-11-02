from rest_framework import routers
from .resources import GrupoEtarioResource, PaisResource, ProvinciaResource, MunicipioResource, DireccionResource, PersonaResource, AtletaResource, EntrenadorResource, InstructorResource, RelacionEntrenadorGrupoEtarioResource
router = routers.DefaultRouter()

router.register(r'grupo_etario', GrupoEtarioResource)
router.register(r'pais', PaisResource)
router.register(r'provincia', ProvinciaResource)
router.register(r'municipio', MunicipioResource)
router.register(r'direccion', DireccionResource)
router.register(r'persona', PersonaResource)
router.register(r'atleta', AtletaResource)
router.register(r'entrenador', EntrenadorResource)
router.register(r'instructor', InstructorResource)
router.register(r'relacion_entrenador_grupo_etario', RelacionEntrenadorGrupoEtarioResource)
