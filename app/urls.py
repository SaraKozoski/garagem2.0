from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import UserViewSet
#AQUI TAMBEM NAO ESQUECEEEEER DESSA LINHAAAAA-------->>>>>>>>>>
from core.views import AcessoriosViewSet, CorViewSet, ModeloViewSet, VeiculoViewSet #<<<<<<<<<<<<<--------------------------

router = DefaultRouter()

router.register(r'usuarios', UserViewSet, basename='usuarios')
#AQUI DE JEITO NENHUM PODE ESQUECEEEEEER
router.register(r"acessorios", AcessoriosViewSet)
# nova linha
router.register(r"cores", CorViewSet)
# nova linha
router.register(r"modelo", ModeloViewSet)
# nova linha
router.register(r"veiculo", VeiculoViewSet)
# nova linha

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
