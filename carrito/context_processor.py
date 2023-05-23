def total_carrito_cp(request):
    total = 0
    if request.user.is_authenticated:
        if "total_carro" in request.session.keys():
            total = request.session["total_carro"]
    else:
        total = 0
    
    return {"total_carrito_2": total}