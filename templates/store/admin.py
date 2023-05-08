from django.contrib import admin
from django.http import HttpResponse
from .models import Store
from django.shortcuts import render
from django.core import serializers


# Register your models here.
class StoreAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Informacion Del Producto", {"fields": ["producto","descripcion_corta", "descripcion"]}),
        ("Cantidad y Precio", {"fields": ["precio", "cantidad_disponible"]}),
        ("Informacion Adicional", {"fields": ["estado_actual", "imagen","fecha_publicacion"]}),
    ]    

    list_display = ["producto", "descripcion", "precio", "cantidad_disponible", "tipo_de_estado", "mostrar_imagen", "fecha_publicacion", "func_stock_valor"]

    actions=["cambiar_estado_a_publicado", "crear_json", "ver_productos_desde_backend"]
    

    def cambiar_estado_a_publicado(self, request, queryset):
        
        registro = queryset.update(estado_actual="Publicado")
        if registro == "1":
            mensaje = "Se ha actualizado 1 estado"
        else:
            mensaje = f"Se han actualizado {registro} estados"
        self.message_user(request, f"{mensaje} con exito!")

    cambiar_estado_a_publicado.short_description = "Cambiar estado a publicado".title()
    
    
    def crear_json(self, request, queryset):
        
        response = HttpResponse(content_type="application/json")
        serializers.serialize("json", queryset, stream=response)
        return response
    
    crear_json.short_description = "Crear JSON"
    
    
    def ver_productos_desde_backend(self, request, queryset):
        
        params = {}
        productos = Store.objects.all()
        params["productos"] = productos
        print(productos)
        return render(request, "admin/productos/productos.html", params)
    
    ver_productos_desde_backend.short_description = "Ver Productos"
    
admin.site.register(Store, StoreAdmin)