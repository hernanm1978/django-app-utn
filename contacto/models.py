from django.db import models
from datetime import datetime
from django.utils.html import format_html

# Create your models here.
class ContactoConsulta(models.Model):
    
    CONTESTADA = "Contestada"
    NOCONTESTADA = "No Contestada"
    ENPROCESO = "En Proceso" 
    ESTADOS = (
            (CONTESTADA, "Contestada"),
            (NOCONTESTADA, "No Contestada"),
            (ENPROCESO,"En Proceso"),
    )

    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    estado_respuesta = models.CharField(max_length=50, choices=ESTADOS, default=NOCONTESTADA)
    telefono = models.CharField(max_length=50, null=False, blank=False)
    fecha = models.DateField(default=datetime.now, null=False, blank=True, editable=True)
    
    def __str__(self) -> str:
        return self.nombre
    
    def estado_de_respuesta(self):
        if self.estado_respuesta == "Contestada":
            return format_html('<span style="background-color:#0a0; color: #fff; padding:5px;">{}</span>', self.estado_respuesta, )
            
        elif self.estado_respuesta == "No Contestada":
            return format_html("<span style='background-color:#a00; color:#fff; padding:5px;'>{}</span>", self.estado_respuesta,)
 
        elif self.estado_respuesta == "En Proceso":
            return format_html("<span style='background-color:#AEB404; color:#fff; padding:5px;'>{}</span>", self.estado_respuesta,)

        
        
    
class ContactoRespuesta(models.Model):
        
    consulta = models.ForeignKey(ContactoConsulta, blank=False, null=True, on_delete=models.CASCADE)
    respuesta = models.TextField()
    fecha = models.DateField(default=datetime.now, blank=True, null=False, editable=True)
    

    def crear_mensaje(self):
        
        consulta_cambio_estado = ContactoConsulta.objects.get(id=self.consulta.id)
        consulta_cambio_estado.estado_respuesta = "Contestada"
        consulta_cambio_estado.save()

        #aqui va la logica de envio de mail, sms o lo que sea de la respuesta 
        
    def save(self, *args, **kwargs):
        self.crear_mensaje()
        force_update = False
        if self.id:
            force_update = True
        super(ContactoRespuesta, self).save(force_update=force_update)
        
        