"""proy_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store.views import index
from store.views import index2
from store.views import ver_imagen
from store.views import VerProducto
from store.views import VerProductoLs
from store.views import barra_busqueda_ajax
from store.views import BuscarProducto
from store.views import BuscarProducto2
from store import views_agregar_item


urlpatterns = [
    path('construccion/', index2, name='index2'),
    path('', index, name='store_index'),
    path('<int:producto_id>/ver-producto/', ver_imagen, name='ver-producto'),
    path('<int:producto_id>/ver/', VerProducto.as_view() , name='ver'),
    # de aca en adelante es para funcionar con el tema de localStorage (jquery y ajax)
    path('<int:producto_id>/ver-producto-ls/', VerProductoLs.as_view(), name='ver-producto-ls'),
    path("agregar_item/", views_agregar_item.agregar_item, name="agregar_item"),
    path("busqueda_ajax/", barra_busqueda_ajax, name="busqueda_ajax"),
    path("buscar_producto/", BuscarProducto.as_view(), name="buscar_producto"),
    path("buscar_producto2/", BuscarProducto2.as_view(), name="buscar_producto2"),
]
