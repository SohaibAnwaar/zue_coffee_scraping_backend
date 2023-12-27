from django.urls import path
from .views import CoffeeShopListView

urlpatterns = [
    path('coffee-shops/', CoffeeShopListView.as_view(), name='coffee-shop-list'),
]
