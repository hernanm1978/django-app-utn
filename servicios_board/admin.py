from django.contrib import admin
from .models import Servicio
#from store.models import Store

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Datos del Cliente", {"fields": ["cliente","telefono", "email"]}),
        ("Datos del Dispositivo", {"fields": ["dispositivo", "descripcion", "fecha_ingreso", "imagen"]}),
        ("Datos del Servicio a Prestar", {"fields": ["servicio", "descripcion_servicio","fecha_presupuesto", "valor_presupuestado1", "estado_actual", "entrega_estimada"]}),
    ]


    list_display = ["id", "servicio", "dispositivo", "descripcion_servicio","cliente", "tipo_de_estado", "fecha_ingreso"]
    # ordering = ["- fecha_ingreso"]          # Esto es para que aparezca ordenado por algun criterio al inicio
    list_filter = ("estado_actual", "servicio")         # Crea menu de filtros
    search_fields = ("cliente",)
    list_display_links = ("servicio", "cliente")
    

admin.site.register(Servicio, ServicioAdmin)
#admin.site.register(Categoria)                 #Para que agregar categorias aparezca en el admin



