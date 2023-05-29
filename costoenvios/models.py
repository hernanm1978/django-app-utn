from django.db import models
from django.utils.html import format_html
# Create your models here.

class CostosEnvios(models.Model):
    
    no_act = "Destino No Activo"
    act = "Destino Activo"
    actualizar = "Actualizar"
    ESTADO_ENVIO = (
        (no_act, "Destino No Activo"),
        (act, "Destino Activo"),
        (actualizar, "Actualizar"),
    )
    
    
    destino = models.CharField(max_length=60, null=False)
    precio_std = models.IntegerField("Precio Standard AR$")
    precio_rapido = models.IntegerField("Precio Rapido AR$")
    fecha_actualizacion_valor = models.DateField('Fecha de actualizacion valor')
    estado_actual = models.CharField(max_length=30, choices=ESTADO_ENVIO, default="Destino Activo")

    def __str__(self):
        return str(self.destino) + " - " + str(self.precio_std) + " - " + str(self.precio_rapido) + " - " + str(self.fecha_actualizacion_valor) + " - " + str(self.estado_actual)


    def tipo_de_estado(self):
        if self.estado_actual == "Destino Activo":
            return format_html('<span style="background-color: #31B404; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )

        elif self.estado_actual == "Actualizar":
            return format_html('<span style="background-color: #AEB404; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )

        elif self.estado_actual == "Destino No Activo":
            return format_html('<span style="background-color: #FF0000; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )
