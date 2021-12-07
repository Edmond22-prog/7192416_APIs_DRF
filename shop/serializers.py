from django.db import models
from rest_framework.serializers import ModelSerializer

from shop.models import Category

# Creation de notre Serializer du model Category
# Un Serializer permet de transformer un model Django en un autre format exploitable par une API
# Ainsi il permettra de transformer notre objet en un JSON lorsque notre API sera consultée, et inversement

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']