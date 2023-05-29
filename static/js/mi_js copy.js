$(document).ready(function () {
    
    console.log("aca")
    $('.increment-btn').click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest('.product_data').find('.vervalor').val();
        var value = parseInt(inc_value,10);
        value = isNaN(value) ? 0 : value;
        console.log("incremento")
        if(value < 10)
        {

            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);

        }   
    });


});
