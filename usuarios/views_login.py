from django.shortcuts import render
from usuarios.forms import UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


# def pagina_login(request):
    
#     params = {}
#     #captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
#         user = authenticate(request, username=username, password=password)    
#         if user is not None:
#             login(request, user)
#             return redirect("/")
#         else:
#             return render(request, "usuarios/login.html", params)
        
#     return render(request, "usuarios/login.html", params)
    # return render(request, "usuarios/login.html") 
    
def pagina_login(request):
    

    
    if request.method == "POST":
        
        form = UserLoginForm(request=request, data=request.POST)
        
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hola {user.username.title()}! Te Logueaste Correctamente.")
                return redirect("/")

        else:
            print(form.errors.items())

            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'Este campo es obligatorio.':
                    messages.error(request, 'Atencion!! No pasaste el reCaptcha Test, Reintentlo')
                    continue
                elif key == 'username' or key == 'password' and error[0] == 'Este campo es obligatorio.':
                    messages.error(request, 'Los Campos Usuario y Password son Obligatorios!')
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="usuarios/login.html",
        context={"form": form},
        )