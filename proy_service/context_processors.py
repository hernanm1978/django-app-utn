from .constantes import captcha_public_key
 
 
def data_templates(request):
     
    return { 
            'captcha_public_key': captcha_public_key,
            
    } 
    
# def total_carro_cp_f(request):
#         if 'total_carro' in request.session:
#                 temp = request.session['total_carro']
#                 return {'total_carro_cp': temp}
#         else:
#                 request.session['total_carro'] = 0
#                 return {'total_carro_cp': request.session['total_carro']}
        