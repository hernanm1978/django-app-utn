/*jslint browser: true*/
/*jslint plusplus: true*/
/*global FormData: false */
/*global $, jQuery, alert, console*/
/*..............................................................................................
... PARA VALIDAR LOS DATOS .....................................................
.............................................................................................*/
var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method) {
    "use strict";
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
/*-------- Agregar elemento al localstorage , request.session.carro (carrito) ------------*/

function Agregar(cada_producto_id, res) {
    "use strict";
    $.ajax({
        beforeSend : function (xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url : "../../store/agregar_item/",
		type : "GET",
		data : { cada_producto_id:cada_producto_id, valor:res},
		success : function (json) {
            localStorage.setItem(json[0].idproducto.toString(), json[0].cantidad.toString());
            location.reload();
		},
		error : function (xhr, errmsg, err) {
			console.log('Error en carga de respuesta');
		}
    });
}
$('.agregar').click(function (event) {
    "use strict";
    event.preventDefault(); 
    let cada_producto_id = $(this).parent().get(0).id; /*$(this).attr('id'); /*$(this).parent().find("product_data").val();+/       /*$(this).parent().get(0).id;*/
    let valor = $(this).parent().find('.qty-input').val();
    let i;
    console.log("cada_producto_id");
    console.log(cada_producto_id);
    console.log("valor");
    console.log(valor);
    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);
        if(!clave_eliminar.startsWith("hmstore_")){
            localStorage.removeItem(clave_eliminar);
        }
    }
    for(i = 0; i < localStorage.length; i++){
        let clave = localStorage.key(i);
        console.log("clave", clave)
        let el_valor = localStorage[clave];
        if(clave == cada_producto_id){
            valor = parseInt(el_valor)+1;
            var res = valor.toString();
        }else{
            console.log("no hay coincidenciaaaa");
        }   
    }
   Agregar(cada_producto_id, valor);
});


/*--------- Funcion restar cantidad de productos seleccionados del carro ------------------*/

function Quitar(cada_producto_id, valor) {
    "use strict";
    $.ajax({
        beforeSend : function (xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		},
		url : "../../store/quitar_producto/",
		type : "GET",
		data : { cada_producto_id:cada_producto_id, valor:valor},
		success : function (json) {
            $('#'+json[0].idproducto +' .quantity').val(json[0].cantidad);
            let cant = json[0].cantidad
            if (cant == 0){
                console.log("vacío");
                localStorage.removeItem(json[0].idproducto.toString(), json[0].cantidad.toString());
                $.ajax({
                    url: "../../store/crear_ls/",
                    data:{producto : JSON.stringify(localStorage)},
                    type: 'get',
                    dataType: 'json',
                    contentType: 'application/json',
                    success: function (data) {
                        var urla = window.location.origin + "/carrito";    
                        window.location.href = urla;
                    },
                });
                location.reload();
            }else{
                localStorage.setItem(json[0].idproducto.toString(), json[0].cantida.toString());
                location.reload();
            }
            location.reload();
		},
		error : function (xhr, errmsg, err) {
			console.log('Error en carga de respuesta');
		}
    });
}

$('.quitar').click(function (event) {
    "use strict";
    let cada_producto_id = $(this).parent().get(0).id;
    let valor = $(this).parent().find('.qty-input').val();
    let i;
    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);
        if(!clave_eliminar.startsWith("hmstore_")){
            localStorage.removeItem(clave_eliminar);
        }
    }
    for(i = 0; i < localStorage.length; i++){
        let clave = localStorage.key(i);
        let el_valor = localStorage[clave];
        if(clave == cada_producto_id){
            valor = el_valor;
        }else{
            console.log("no hay coincidencia");
        }   
    }
    Quitar(cada_producto_id, valor);
});


/*--------- Funcion eliminar producto del carro ------------------*/

$('.eliminar_producto').click(function (event) {
    "use strict";
    let cada_producto_id = $(this).attr('id');
    cada_producto_id = cada_producto_id.replace(/^el/, "hmstore_"); 
    let i;

    for(i = 0; i < localStorage.length; i++){
        let clave_eliminar = localStorage.key(i);
        if(!clave_eliminar.startsWith("hmstore_")){
            localStorage.removeItem(clave_eliminar);
        }
    }
    localStorage.removeItem(cada_producto_id);
    $.ajax({
        url: "../../store/crear_ls/",
        data:{producto : JSON.stringify(localStorage)},
        type: 'get',
        dataType: 'json',
        contentType: 'application/json',
        success: function (data) {
        var urla = window.location.origin + "/carrito";    
        window.location.href = urla;
        console.log("cada producto idddddddddddd", cada_producto_id)
        },
    });
});

 




// $(document).ready(function (event) {

//     console.log("aca");
//     $('#increment-btn').click(function (e) {
//         e.preventDefault();

//         var inc_value = $(this).closest('.product_data').find('.qty-input').val();
//         var value = parseInt(inc_value,10);
//         value = isNaN(value) ? 0 : value;
//         console.log("incremento");
//         console.log(value)
//         if(value < 10)
//         {

//             value++;
//             $(this).closest('.product_data').find('.qty-input').val(value);
//             console.log(value)
//         }   
//     });


// });
// $('.fas fa-times').click(function (event) {
//     "use strict";
//     console.log("aca estoy")
//     let cada_producto_id = $(this).attr('id');
//     cada_producto_id = cada_producto_id.replace(/^el/, "prestige_"); 
//     let i;

//     for(i = 0; i < localStorage.length; i++){
//         let clave_eliminar = localStorage.key(i);
//         if(!clave_eliminar.startsWith("prestige_")){
//             localStorage.removeItem(clave_eliminar);
//             console.log(i)
//         }
//     }
//     localStorage.removeItem(cada_producto_id);
//     $.ajax({
//         url: "/tienda/crear_localstorage/",
//         data:{producto : JSON.stringify(localStorage)},
//         type: 'get',
//         dataType: 'json',
//         contentType: 'application/json',
//         success: function (data) {
//         var urla = window.location.origin + "/carrito";    
//         window.location.href = urla;
//         },
//     });
// });