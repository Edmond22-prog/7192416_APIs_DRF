from django.contrib import admin
from django.urls import path, include

from shop.views import CategoryAPIView, ProductAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # Lien de notre endpoint
    path('api/category/', CategoryAPIView.as_view()),
    # Lien de mon premier endpoint
    path('api/product/', ProductAPIView.as_view())
]
