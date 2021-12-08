from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class CategoryAPIView(APIView):

    def get(self, *args, **kwargs):
        # Récupération de toutes les categories
        categories = Category.objects.all()
        # Sérialisation les données (categories) récupérer grace à notre classe CategotySerializer
        # Le paramètre many précise au Serializer qu'il va devoir générer une liste d'éléments à 
        # partir de l'itérable transmis categories. Si ce n'etait qu'un element, pas nécessaire de mettre le many
        serializer = CategorySerializer(categories, many=True)
        # Renvoi une reponse avec les donnees serialisées
        return Response(serializer.data)


class ProductAPIView(APIView):

    def get(self, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)