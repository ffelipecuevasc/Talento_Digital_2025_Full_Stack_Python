// Demostración de los conceptos del manual:
// - Eventos: concepto, event handler, event listener
// - Definir eventos con addEventListener y propiedades como onclick
// - Eventos click y dblclick
// - Eventos del mouse: mousemove, mousedown, mouseup, mouseover, mouseout
// - Eventos del teclado: keydown y keyup
// - Eventos change e input en campos de texto y selects

console.log("=== Inicio de la demo de eventos ===");

// Pequeña función de utilidad para escribir en el "log" de la página.
// Esto nos ayudará a visualizar qué eventos se van disparando.
const logEventos = document.getElementById("log-eventos");

function agregarAlLog(mensaje) {
    const entrada = document.createElement("div");
    entrada.className = "log-entry";
    const hora = new Date().toLocaleTimeString();
    entrada.innerText = `[${hora}] ${mensaje}`;
    logEventos.appendChild(entrada);

    // Scroll automático al final para ver siempre el último evento.
    logEventos.scrollTop = logEventos.scrollHeight;
}

// 1) Eventos de click en botones

// Ejemplo Opción 2 del manual: usar la propiedad onclick como event handler.
// Aquí estamos asignando una función anónima que se ejecutará cuando haya click.
const btnClickProp = document.getElementById("btn-click-prop");

btnClickProp.onclick = function () {
    console.log("Click manejado con propiedad onclick.");
    agregarAlLog("Click en botón (propiedad onclick).");
    alert("Click detectado con propiedad 'onclick'.");
};

// Ejemplo Opción 1 del manual: usar addEventListener.
// Esto nos permite agregar un "escuchador" para el evento "click".
const btnClickAdd = document.getElementById("btn-click-add");

function manejarClickAdd() {
    console.log("Click manejado con addEventListener.");
    agregarAlLog("Click en botón (addEventListener).");
    alert("Click detectado con 'addEventListener'.");
}

btnClickAdd.addEventListener("click", manejarClickAdd);

// Evento dblclick (doble click) en botón específico.
const btnDblClick = document.getElementById("btn-dblclick");

btnDblClick.addEventListener("dblclick", function () {
    console.log("Doble click (dblclick) en el botón.");
    agregarAlLog("Doble click en botón (dblclick).");
    alert("Hiciste doble click en el botón.");
});

// 2) Eventos del mouse en una caja

const cajaMouse = document.getElementById("caja-mouse");
const infoMouse = document.getElementById("info-mouse");

// Función genérica para actualizar la información del último evento de mouse.
function actualizarInfoMouse(tipoEvento) {
    infoMouse.innerText = tipoEvento;
    agregarAlLog(`Evento de mouse: ${tipoEvento}`);
}

// mouseover: el puntero entra en el área de la caja.
cajaMouse.addEventListener("mouseover", function () {
    cajaMouse.classList.add("activa");
    actualizarInfoMouse("mouseover (el mouse entró en la caja)");
});

// mouseout: el puntero sale del área de la caja.
cajaMouse.addEventListener("mouseout", function () {
    cajaMouse.classList.remove("activa");
    actualizarInfoMouse("mouseout (el mouse salió de la caja)");
});

// mousedown: se presiona el botón dentro de la caja.
cajaMouse.addEventListener("mousedown", function () {
    actualizarInfoMouse("mousedown (botón del mouse presionado)");
});

// mouseup: se suelta el botón dentro de la caja.
cajaMouse.addEventListener("mouseup", function () {
    actualizarInfoMouse("mouseup (botón del mouse liberado)");
});

// click: click completo (presionar + soltar).
cajaMouse.addEventListener("click", function () {
    actualizarInfoMouse("click (click completo dentro de la caja)");
});

// mousemove: se mueve el mouse sobre la caja.
// Mostramos coordenadas X/Y relativas a la caja para ejemplificar.
cajaMouse.addEventListener("mousemove", function (evento) {
    const coords = `mousemove (x: ${evento.offsetX}, y: ${evento.offsetY})`;
    infoMouse.innerText = coords;
    // Para no llenar demasiado el log, podemos comentar esta línea si hay demasiados eventos.
    // agregarAlLog(coords);
});

// 3) Eventos del teclado: keydown y keyup en un input

const inputTeclado = document.getElementById("input-teclado");
const infoTeclado = document.getElementById("info-teclado");

// keydown: se dispara cuando una tecla se presiona.
inputTeclado.addEventListener("keydown", function (evento) {
    const mensaje = `keydown - tecla presionada: "${evento.key}" (código: ${evento.keyCode})`;
    console.log(mensaje);
    infoTeclado.innerText = mensaje;
    agregarAlLog(mensaje);
});

// keyup: se dispara cuando una tecla se suelta.
inputTeclado.addEventListener("keyup", function (evento) {
    const mensaje = `keyup - tecla liberada: "${evento.key}"`;
    console.log(mensaje);
    agregarAlLog(mensaje);
});

// 4) Eventos change e input en campos de texto y selects

const inputTexto = document.getElementById("input-texto");
const infoInputTexto = document.getElementById("info-input-texto");
const selectOpcion = document.getElementById("select-opcion");
const infoSelect = document.getElementById("info-select");

// Evento change en el input de texto:
// Se dispara cuando el valor cambia y el campo pierde el foco (o se confirma el cambio).
inputTexto.addEventListener("change", function () {
    const valor = inputTexto.value;
    const mensaje = `change en input-texto: valor final = "${valor}"`;
    console.log(mensaje);
    infoInputTexto.innerText = mensaje;
    agregarAlLog(mensaje);
});

// Evento input en el mismo campo de texto:
// Se dispara en tiempo real cada vez que el usuario escribe o borra.
inputTexto.addEventListener("input", function () {
    const valor = inputTexto.value;
    const longitud = valor.length;
    const mensaje = `input en input-texto: "${valor}" (longitud: ${longitud})`;
    infoInputTexto.innerText = mensaje;
    // No lo mandamos siempre al log para evitar saturarlo, pero podría hacerse.
});

// Evento change en el select:
// Ideal para reaccionar cuando el usuario elige una nueva opción.
selectOpcion.addEventListener("change", function () {
    const valor = selectOpcion.value;

    if (valor === "") {
        infoSelect.innerText = "Ninguna opción seleccionada.";
        agregarAlLog("change en select: sin opción válida.");
        return;
    }

    const mensaje = `change en select-opcion: seleccionaste "${valor}".`;
    console.log(mensaje);
    infoSelect.innerText = mensaje;
    agregarAlLog(mensaje);

    // Pequeño ejemplo visual: cambiar el color de fondo de la página según la opción.
    if (valor === "rojo") {
        document.body.style.backgroundColor = "#ffe5e5";
    } else if (valor === "verde") {
        document.body.style.backgroundColor = "#e5ffe5";
    } else if (valor === "azul") {
        document.body.style.backgroundColor = "#e5f0ff";
    }
});

console.log("=== Fin de la demo de eventos ===");