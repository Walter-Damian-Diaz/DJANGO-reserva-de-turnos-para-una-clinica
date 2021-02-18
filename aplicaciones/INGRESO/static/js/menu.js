$(document).ready(mostrar_menu);


function mostrar_menu(){
    
    $('.icono-menu').click(function(){
        
        $('.menu-container').animate({
            left:'0'
        });
        $('.icono-menu').toggleClass("remove");
        $('.x-icono').toggleClass("show");
    });

    $('.x-icono').click(function(){
        
        $('.menu-container').animate({
            left:'-100%'
        });

        $('.x-icono').toggleClass('show');
        $('.icono-menu').toggleClass('remove');
    });

}

