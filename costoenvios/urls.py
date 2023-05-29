from django.urls import path
from views import costoenvios



urlpatterns = [
    path('', costoenvios.as_view(), name='carrito'),
]