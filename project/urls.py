from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from shop.views import CategoryViewset

# Création du routeur
router = routers.SimpleRouter()
# Ajout d'une url et sa view dans le routeur
router.register('category', CategoryViewset, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # Ajout des urls du routeur dans les urls disponible
    path('api/', include(router.urls))
]
