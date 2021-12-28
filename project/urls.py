from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from shop.views import ArticleViewset, CategoryViewset, ProductViewset

# Création du routeur
# Le routeur permet de definir en une seule fois toutes les operations du CRUD
# Il faut au preable definir des ViewSet pour que le routeur fonctionne
router = routers.SimpleRouter()
# Ajout d'une url et sa view dans le routeur
router.register('category', CategoryViewset, basename='category')
router.register('product', ProductViewset, basename='product')
router.register('article', ArticleViewset, basename='article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # Ajout des urls du routeur dans les urls disponible
    path('api/', include(router.urls))
]
