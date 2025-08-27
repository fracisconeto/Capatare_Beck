from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import (
    UserViewSet,
    UsuarioViewSet,
    EnderecoViewSet,
    CategoriaViewSet,
    ProdutoViewSet,
    PedidoViewSet,
    ItenViewSet,
    CarrinhoViewSet,
    CarrinhoItemViewSet
)

router = DefaultRouter()

router.register(r'usuario', UserViewSet, basename='usuario')
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'enderecos', EnderecoViewSet, basename='endereco')
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'produtos', ProdutoViewSet, basename='produto')
router.register(r'pedidos', PedidoViewSet, basename='pedido')
router.register(r'itens', ItenViewSet, basename='itens')
router.register(r'carrinhos', CarrinhoViewSet, basename='carrinho')
router.register(r'carrinho-itens', CarrinhoItemViewSet, basename='carrinho-itens')

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
