from django.db import models
from django.utils.html import format_html


# Create your models here.


class Store(models.Model):

    no_pub = "No Publicado"
    pub = "Publicado"
    borr = "Borrador"
    ESTADO_PRODUCTO = (
        (no_pub, "No Publicado"),
        (pub, "Publicado"),
        (borr, "Borrador"),
    )

    filtro80 = "Filtro 80x80mm"
    filtro120 = "Filtro 120x120mm"
    filtro140 = "Filtro 140x140mm"
    hdd = "Disco Rigido"
    software = "Software"
    dir_lister = "Directories Lister"
    hm_meta = "Meta Data Extractor"
    LOS_PRODUCTOS = (
        (filtro80, "Filtro 80x80mm"),
        (filtro120, "Filtro 120x120mm"),
        (filtro140, "Filtro 140x140mm"),
        (hdd, "Disco Rigido"),
        (software, "Software"),
        (dir_lister, "Directories Lister"),
        (hm_meta, "Meta Data Extractor"),
    )



    producto = models.CharField(max_length=60, choices=LOS_PRODUCTOS)
    descripcion_corta = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    fecha_publicacion = models.DateField('Fecha de Publicacion')
    estado_actual = models.CharField(max_length=30, choices=ESTADO_PRODUCTO, default="No Publicado")
    precio = models.IntegerField("Precio AR$")
    cantidad_disponible = models.IntegerField('Unidades Disponibles')
    imagen = models.ImageField(upload_to="producto/%Y/%m/%d", blank=True, null=True) 
    stock_valor = models.IntegerField("Valor Stock AR$", null=True)
    
    # categoria = models.ManyToManyField(Categoria)

    def __str__(self):
        return str(self.producto) + " - " + str(self.cantidad_disponible) + " - "+ str(self.estado_actual)      #sobreescrito por list_display


    def tipo_de_estado(self):
        if self.estado_actual == "Publicado":
            return format_html('<span style="background-color: #31B404; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )

        elif self.estado_actual == "Borrador":
            return format_html('<span style="background-color: #AEB404; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )

        elif self.estado_actual == "No Publicado":
            return format_html('<span style="background-color: #FF0000; padding: 2px; font-weight: bold;">{}</span>', self.estado_actual, )
        
    
    def mostrar_imagen(self):
        if self.imagen:
            return format_html('<img src="{}" width="20" height="20">',self.imagen.url)
    
    def func_stock_valor(self):
        resultado = '{:,}'.format(self.precio * self.cantidad_disponible)
        return resultado