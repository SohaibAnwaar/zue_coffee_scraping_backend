from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import CoffeeShop
from .serializers import CoffeeShopSerializer


class CoffeeShopPagination(PageNumberPagination):
    page_size = 25


class CoffeeShopListView(generics.ListAPIView):
    queryset = CoffeeShop.objects.all()
    serializer_class = CoffeeShopSerializer
    pagination_class = CoffeeShopPagination
