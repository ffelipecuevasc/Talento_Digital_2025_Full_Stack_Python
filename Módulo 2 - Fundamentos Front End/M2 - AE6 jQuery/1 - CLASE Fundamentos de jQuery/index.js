// Debemos asegurarnos de programar cuando el DOM efectivamente esté cargado
$(document).ready(function(){

    // 1) Seleccionaremos el botón por su ID y escucharemos el evento 'click'
    $('#boton-detalle').on('click', function(){
        // Usamos una función de jQuery (toggleClass) para alternar la visibilidad,
        // pero coordinada con la animación para que no choque con la clase d-none de Bootstrap
        if($('#detalle-dom').hasClass('d-none')){
            // Está oculto: quitamos d-none, lo mantenemos oculto y lo mostramos con slideDown
            $('#detalle-dom').toggleClass('d-none').hide().slideDown(1000);
            $('#boton-detalle').text('Ocultar detalles del DOM');
        }else{
            // Está visible: lo ocultamos con slideUp y, cuando termina, volvemos a aplicar d-none
            $('#detalle-dom').slideUp(1000, function(){
                $('#detalle-dom').toggleClass('d-none');
            });
            $('#boton-detalle').text('Mostrar detalles del DOM');
        }
    });

    // 2) Cambiar el estilo de la tarjeta usando las clases de Bootstrap
    $('#boton-cambiar-estilo').on('click', function(){
        var $tarjeta = $('#tarjeta-info');
        // Acá alternamos clases de BS para cambiar la apariencia
        $tarjeta.toggleClass('bg-warning border border-dark border-success-shadow');
        $('#texto-dom').text('✨ Acabas de ver el DOM en acción: jQuery modificó las clases y cambió este texto ✨');
    });
});