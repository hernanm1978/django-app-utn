from django.db import models
from django.utils.html import format_html
# Create your models here.

# class Categoria(models.Model):
#     estado_actual = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=100, db_index=True)

#     def __str__(self):
#         return '%s' % self.estado_actual


class Servicio(models.Model):

    esp_diag = "En Espera Diagnostico"
    diag = "En Diagnostico"
    apro_cl = "Esperando Aprobacion Cliente"
    en_serv = "Servicio Iniciado"
    serv_fin = "Servicio Finalizado"
    pago_pdte = "Pago Pendiente"
    pagado_esp = "Esperando Retiro"
    finalizado = "Entregado"
    recha = "No Aprobado Esperando Retiro"
    ESTADO_SERVICIO = (
        (esp_diag, "En Espera Diagnostico"),
        (diag, "En Diagnostico"),
        (apro_cl, "Esperando Aprobacion Cliente"),
        (en_serv, "Servicio Iniciado"),
        (serv_fin, "Servicio Finalizado"),
        (pago_pdte, "Pago Pendiente"),
        (pagado_esp, "Esperando Retiro"),
        (finalizado, "Entregado"),
        (recha, "No Aprobado Esperando Retiro"),

    )

    rec_datos = "Recupero De Datos"
    borr_seg = "Borrado Seguro De Datos"
    rep_ped = "Reparacion Pedal Guitarra/Bajo"
    rer_parl = "Reparacion Parlante"
    rep_j_ps4 = "Reparacion Joystick PS-4"
    rep_j_ps5 = "Reparacion Joystick PS-5"
    rep_j_xb1 = "Reparacion Joystick XBOX-ONE"
    rep_j_xb360 = "Reparacion Joystick XBOX-360"
    rep_pc = "Reparacion PC/Notebook"
    rep_gral = "Reparaciones Varias"
    LOS_SERVICIOS = (
        (rec_datos, "Recupero De Datos"),
        (borr_seg, "Borrado Seguro De Datos"),
        (rep_ped, "Reparacion Pedal Guitarra/Bajo"),
        (rer_parl, "Reparacion Parlante"),
        (rep_j_ps4, "Reparacion Joystick PS-4"),
        (rep_j_ps5, "Reparacion Joystick PS-5"),
        (rep_j_xb1, "Reparacion Joystick XBOX-ONE"),
        (rep_j_xb360, "Reparacion Joystick XBOX-360"),
        (rep_pc, "Reparacion PC/Notebook"),
        (rep_gral, "Reparaciones Varias"),
    )



    servicio = models.CharField(max_length=30, choices=LOS_SERVICIOS)
    cliente = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    dispositivo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    descripcion_servicio = models.CharField(max_length=200, blank=True, null=True)
    fecha_ingreso = models.DateField('Fecha de Ingreso')
    estado_actual = models.CharField(max_length=30, choices=ESTADO_SERVICIO, default="En Espera Diagnostico")
    entrega_estimada = models.DateField('Fecha Entrega', blank=True,null=True)
    valor_presupuestado1 = models.IntegerField("Valor Presupuestado AR$", blank=True, null=True)
    fecha_presupuesto = models.DateField('Fecha Presupuesto', blank=True, null=True)
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True) 
    # categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return str(self.servicio) + " - " + str(self.cliente) + " - "+ str(self.estado_actual)      #sobreescrito por list_display


    def tipo_de_estado(self):
        if self.estado_actual == "Servicio Iniciado":
            return format_html('<span style="background-color: #2E9AFE; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )
        elif self.estado_actual == "En Espera Diagnostico":
            return format_html('<span style="background-color: #B404AE; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )
        elif self.estado_actual == "En Diagnostico":
            return format_html('<span style="background-color: #2E9AFE; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )
        elif self.estado_actual == "Esperando Aprobacion Cliente":
            return format_html('<span style="background-color: #AEB404; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )
        elif self.estado_actual == "Servicio Finalizado":
            return format_html('<span style="background-color: #80FF00; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )
        elif self.estado_actual == "Pago Pendiente":
            return format_html('<span style="background-color: #FF8000; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )
        elif self.estado_actual == "Esperando Retiro":
            return format_html('<span style="background-color: #088A68; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )
        elif self.estado_actual == "Entregado":
            return format_html('<span style="background-color: #31B404; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )
        elif self.estado_actual == "No Aprobado Esperando Retiro":
            return format_html('<span style="background-color: #FF0000; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )
        