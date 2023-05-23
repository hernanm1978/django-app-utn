from django.urls import path
from carrito.views import Carrito



urlpatterns = [
    path('', Carrito.as_view(), name='carrito'),
]