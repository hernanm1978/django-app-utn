from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from contacto.models import ContactoConsulta
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class ConsultaForm(ModelForm):
    
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    
    class Meta:
        model = ContactoConsulta
        fields = [
            'nombre',
            'descripcion',
            'email',
            'telefono',
        ]
    
    def send_email(self,):
        
        nombre = self.cleaned_data['nombre']
        descripcion = self.cleaned_data['descripcion']
        email = self.cleaned_data['email']
        #estado_respuesta = self.cleaned_data[estado_respuesta]
        telefono = self.cleaned_data['telefono']
        #fecha_consulta = self.cleaned_data[fecha_consulta]
        
        # logica para el envio de email