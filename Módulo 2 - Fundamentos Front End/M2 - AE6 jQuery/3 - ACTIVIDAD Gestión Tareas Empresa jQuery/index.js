// Esperamos a que el DOM esté completamente cargado
$(document).ready(function () {

    // Guardamos algunas referencias a elementos que usaremos varias veces
    var $form = $('#form-usuario');
    var $nombre = $('#nombre');
    var $edad = $('#edad');
    var $tablaUsuarios = $('#tabla-usuarios');

    // 3) Capturamos el evento SUBMIT del formulario
    $form.on('submit', function (evento) {
        // Evitamos que el formulario recargue la página
        evento.preventDefault();

        // Obtenemos y limpiamos los valores
        var nombre = $nombre.val().trim();
        var edad = $edad.val().trim();

        // Validación básica: si falta algo, no agregamos
        if (nombre === '' || edad === '') {
            alert('Por favor completa nombre y edad.');
            return;
        }

        // 4) Creamos una nueva FILA (<tr>) con las celdas (<td>)
        // Las celdas de nombre y edad serán "contenteditable" para poder editarlas.
        var $fila = $('<tr></tr>');

        var $celdaNombre = $('<td></td>')
            .text(nombre)
            .attr('contenteditable', 'true'); // permite editar el texto

        var $celdaEdad = $('<td></td>')
            .text(edad)
            .attr('contenteditable', 'true');

        // Celda de acciones con un botón "Eliminar"
        var $celdaAcciones = $('<td class="text-center"></td>');
        var $botonEliminar = $('<button></button>')
            .addClass('btn btn-sm btn-danger btn-eliminar')
            .text('Eliminar');

        // Agregamos el botón dentro de la celda
        $celdaAcciones.append($botonEliminar);

        // Armamos la fila completa
        $fila.append($celdaNombre, $celdaEdad, $celdaAcciones);

        // 6) Efecto visual: la fila aparece con una pequeña animación
        $fila.hide();              // primero la ocultamos
        $tablaUsuarios.append($fila);
        $fila.fadeIn(300);         // luego la mostramos con fadeIn

        // Limpiamos el formulario para el próximo registro
        $nombre.val('');
        $edad.val('');
        $nombre.focus();           // volvemos a colocar el cursor en el nombre
    });

    // 4) Delegamos el evento CLICK en el botón "Eliminar"
    // Usamos delegación porque las filas se crean dinámicamente.
    $tablaUsuarios.on('click', '.btn-eliminar', function () {
        // "this" es el botón; subimos al <tr> que lo contiene
        var $fila = $(this).closest('tr');

        // 6) Efecto visual al eliminar: desvanecer y luego quitar del DOM
        $fila.fadeOut(300, function () {
            $fila.remove();
        });
    });

    // Nota: la edición (punto 5) se logra gracias a contenteditable="true" en las celdas
    // El navegador permite cambiar el texto directamente sin código extra.
});