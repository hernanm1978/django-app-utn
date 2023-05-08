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
from . import views   # que es lo mismo que from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('administracion_servicios/', views.administracion_servicios, name='administracion_servicios'),
    path('alta_servicio/', views.alta_servicio, name='alta_servicio'),
    path('recuperacion_datos/', views.recuperacion_datos, name='recuperacion_datos'),
    path('electronics/', views.electronics, name='electronics'),
    path('dev/', views.dev, name='dev'),
    path('nosotros/', views.nosotros, name='nosotros'),
    
]
