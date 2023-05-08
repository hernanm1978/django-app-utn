from django.contrib import admin
from .models import ContactoConsulta
from .models import ContactoRespuesta

# Register your models here.
class RespuestaInline(admin.TabularInline):
    model = ContactoRespuesta
    extra = 0
    
class ConsultaAdmin(admin.ModelAdmin):
    inlines = [RespuestaInline]
    list_display = [
            'nombre',
            'descripcion',
            'email',
            'telefono',
            'fecha',
            'estado_de_respuesta',
        ]
    list_filter = ['estado_respuesta', 'fecha']
    
admin.site.register(ContactoConsulta, ConsultaAdmin)