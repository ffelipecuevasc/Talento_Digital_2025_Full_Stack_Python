// Esperamos a que el DOM esté listo antes de usar jQuery
$(document).ready(function () {

    // Guardamos en variables los elementos que vamos a usar
    var $inputTarea = $('#input-tarea');   // campo de texto
    var $listaTareas = $('#lista-tareas'); // lista <ul>

    // Cuando el usuario hace clic en "Agregar tarea"
    $('#btn-agregar').on('click', function () {
        // Obtenemos el texto escrito y eliminamos espacios al inicio/fin
        var texto = $inputTarea.val().trim();

        // Si el input está vacío, no hacemos nada
        if (texto === '') {
            return;
        }

        // Creamos un nuevo <li> con clases de Bootstrap
        var $nuevoItem = $('<li></li>')
            .addClass('list-group-item')
            .text(texto);

        // Agregamos un evento para que, al hacer clic en la tarea, se elimine
        $nuevoItem.on('click', function () {
            // this es el <li> clickeado
            $(this).remove();
        });

        // Insertamos la nueva tarea en la lista
        $listaTareas.append($nuevoItem);

        // Limpiamos el campo de texto y volvemos a darle foco
        $inputTarea.val('').focus();
    });

    // Extra: permitir agregar tareas presionando Enter en el input
    $inputTarea.on('keyup', function (evento) {
        if (evento.key === 'Enter') {
            $('#btn-agregar').click();
        }
    });
});