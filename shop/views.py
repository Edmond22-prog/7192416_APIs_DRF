from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer

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