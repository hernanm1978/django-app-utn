from django.contrib import admin
from .models import CostosEnvios
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
# Register your models here.

class CostosEnviosAdmin(admin.ModelAdmin):

    list_display = ["destino", "precio_std", "precio_rapido", "tipo_de_estado", "fecha_actualizacion_valor"]

    actions = ["ver_productos_desde_backend", "crear_json"]
    
    def crear_json(self, request, queryset):
        
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response    

    def ver_productos_desde_backend(self, request, queryset):
        
        params = {}
        destinos = CostosEnvios.objects.all()
        params["destinos"] = destinos
        print(destinos)
        return render(request, "admin/productos/productos.html", params)
    
    ver_productos_desde_backend.short_description = "Ver Productos"
    
admin.site.register(CostosEnvios, CostosEnviosAdmin)