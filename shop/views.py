from django.utils.translation import activate
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
        queryset = Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset