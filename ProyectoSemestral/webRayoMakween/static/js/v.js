$(function(){
    $("#formula1").validate({
        rules:{
            txtnombre:{
                required:true,
                minlength:2

            },
            txtusuario:{
                required:true
                
            },
            txtasunto:{
                required:true
                
            },
            txtsuge:{
                required:true
            }
        },messages:{
            txtnombre:{
                required:"Este Campo es obligatorio",
                minlength:"No cumple con los caracteres definidos(2)"
                
            },txtusuario:{
                required:"Este Campo es obligatorio"
            },txtasunto:{
                required:"Este Campo es obligatorio"
            },txtsuge:{
                required:"Este Campo es obligatiorio"
            }
        }
         
    
   
         
    });
});
$(function(){
    $("#registro").validate({
        rules:{
            txtnombre:{
                required:true,
                minlength:2

            },
            txtcorreo:{
                required:true,
                email:true
                
            },
            txtcontra:{
                required:true   
            }
        },messages:{
            txtnombre:{
                required:"Este Campo es obligatorio",
                minlength:"No cumple con los caracteres definidos(2)"
                
            },txtcorreo:{
                required:"Este Campo es obligatorio",
                email:"No cumple con el formato de un email"
            },txtcontra:{
                required:"Este Campo es obligatorio"
            }
        }
         
    
   
         
    });
});

$(function(){
    $("#login").validate({
        rules:{
            txtusuario:{
                required:true,
                
            },
            txtcontra:{
                required:true   
            }
        },messages:{
            txtcorreo:{
                required:"Este Campo es obligatorio",
            },txtcontra:{
                required:"Este Campo es obligatorio"
            }
        }
         
    
   
         
    });
});
