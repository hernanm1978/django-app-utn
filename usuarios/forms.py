from typing import Any
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class CreateUserForm(UserCreationForm):
    
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    # captcha  = CaptchaField()
    
    # Sobreescribo metodos asi formateo el html del usercreationform como quiero (bootstap 5.3)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)
        self.fields["username"].widget.attrs.update({
            'required': "",
            'type': 'text',
            'class': 'form-control',
            'id':"floatingInput",
            'placeholder': "nombre",
            'name': "username"
        })
        self.fields["email"].widget.attrs.update({
            'required': "",
            'type':"email",
            'class': "form-control",
            'id': "floatingInput",
            'placeholder': "email",
            'name':"email"
        })
        self.fields["password1"].widget.attrs.update({
            "type": "password",
            "class": "form-control",
            "id":"floatingPassword",
            "placeholder": "Password1",
            "name": "password1"
            
        })
        self.fields["password2"].widget.attrs.update({
            "type": "password",
            "class": "form-control",
            "id":"floatingPassword",
            "placeholder": "Password2",
            "name": "password2"
            
        })
        
        # self.fields["captcha"].widgets.attrs.update({
        #     "type": "text",
        #     "class": "form-control",
        #     "id": "floatingPassword",
        #     "placeholder": "Password2",
        #     "name": "capthca"
        # })
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
        
class UserLoginForm(AuthenticationForm):
    
    # captcha  = CaptchaField()
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            'required': "",
            'type': 'text',
            'class': 'form-control',
            'id':"floatingInput",
            'placeholder': "nombre",
            'name': "username"
        })

        self.fields["password"].widget.attrs.update({
            'required': "",
            "type": "password",
            "class": "form-control",
            "id":"floatingPassword",
            "placeholder": "Password",
            "name": "password"
            
        })
        
    
    class Meta:
        model = User
        fields = ["username", "password"]