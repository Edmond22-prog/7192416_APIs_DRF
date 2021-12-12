from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryViewset(ReadOnlyModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

# Création d'un ModelViewSet pour les produits
class ProductViewset(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()