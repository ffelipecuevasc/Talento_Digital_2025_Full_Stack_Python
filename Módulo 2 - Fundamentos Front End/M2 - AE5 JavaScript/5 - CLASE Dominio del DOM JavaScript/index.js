// Demostración de conceptos del DOM:
// - Árbol de nodos y document
// - Selectores básicos: getElementById, getElementsByTagName, getElementsByClassName
// - innerText, textContent, innerHTML
// - className (y mención de classList)
// - createElement, appendChild, removeChild, remove
// - value de inputs
// - querySelector, querySelectorAll + forEach

console.log("=== Inicio de la demo DOM ===");

// 1) Selectores básicos: getElementById, getElementsByTagName, getElementsByClassName

// Seleccionamos el título principal usando su id (devuelve un solo elemento).
const tituloPrincipal = document.getElementById("main-title");

// Seleccionamos TODOS los párrafos <p> (devuelve una colección).
const parrafos = document.getElementsByTagName("p");

// Seleccionamos elementos por su clase (también una colección).
const descripciones = document.getElementsByClassName("descripcion");

console.log("Título principal:", tituloPrincipal);
console.log("Párrafos:", parrafos);
console.log("Descripciones:", descripciones);

// 2) innerText, textContent, innerHTML

// Cambiamos el texto del título con innerText.
// Esto reemplaza el texto visible dentro del <h1>.
tituloPrincipal.innerText = "Demo DOM: JavaScript controlando el contenido 😎";

// Para el primer párrafo, usamos textContent para cambiar el texto completo.
if (parrafos.length > 0) {
    parrafos[0].textContent =
        "Este texto fue actualizado desde JavaScript usando textContent.";
}

// Para el segundo párrafo, demostramos el uso de innerHTML con etiquetas.
if (parrafos.length > 1) {
    parrafos[1].innerHTML =
        "Este párrafo contiene <strong>HTML dinámico</strong> generado con innerHTML.";
}

// 3) Manejo de clases CSS desde JS: className (y mención de classList)

// Podemos leer las clases actuales del título:
console.log("Clases actuales del título:", tituloPrincipal.className);

// Asignamos una nueva clase al título (sobrescribe las anteriores).
// Si quieres no sobrescribir, podrías concatenar o usar classList.add().
tituloPrincipal.className = "resaltado";

// Si el navegador soporta classList (prácticamente todos hoy en día),
// podríamos hacer algo así (ejemplo ilustrativo, sin condicional):
// tituloPrincipal.classList.add("otra-clase");

// 4) Agregar y quitar nodos del DOM: createElement, appendChild, removeChild, remove

// Primero seleccionamos la lista de notas y algunos botones usando querySelector.
const listaNotas = document.querySelector("#lista-notas");
const botonAgregar = document.querySelector("#btn-agregar");
const botonEliminarUltima = document.querySelector("#btn-eliminar-ultima");

// También el input de nueva nota para leer su value.
const inputNuevaNota = document.querySelector("#nueva-nota");

// Función para agregar una nueva nota a la lista.
function agregarNota() {
    // Obtenemos el texto que el usuario escribió en el input.
    const textoNota = inputNuevaNota.value.trim();

    // Si está vacío, no agregamos nada.
    if (textoNota === "") {
        alert("Por favor, escribe una nota antes de agregar.");
        return;
    }

    // Creamos un nuevo elemento <li>.
    const nuevaLi = document.createElement("li");

    // Le asignamos clases CSS para que se vea como las demás.
    nuevaLi.className = "nota";

    // Usamos innerText para poner el contenido de la nota (solo texto).
    nuevaLi.innerText = textoNota;

    // Agregamos el nuevo <li> como hijo de la lista <ul>.
    listaNotas.appendChild(nuevaLi);

    // Limpiamos el input para que el usuario pueda escribir otra nota.
    inputNuevaNota.value = "";
}

// Función para eliminar la última nota de la lista.
function eliminarUltimaNota() {
    // Obtenemos el último hijo <li> de la lista (lastElementChild).
    const ultimaNota = listaNotas.lastElementChild;

    if (!ultimaNota) {
        alert("No hay notas para eliminar.");
        return;
    }

    // Opción 1 (clásica): usar removeChild en el padre.
    // listaNotas.removeChild(ultimaNota);

    // Opción 2 (moderna y más directa): llamar a remove() en el propio elemento.
    ultimaNota.remove();
}

// Asociamos las funciones a los botones usando addEventListener.
botonAgregar.addEventListener("click", agregarNota);
botonEliminarUltima.addEventListener("click", eliminarUltimaNota);

// 5) Uso de querySelector y querySelectorAll

// Seleccionamos el botón para resaltar el título.
const botonResaltarTitulo = document.querySelector("#btn-resaltar-titulo");

// Esta función alterna (toggle) la clase "resaltado" en el título.
function alternarResaltadoTitulo() {
    // Si tenemos classList, podemos usar toggle para agregar/quitar una clase.
    tituloPrincipal.classList.toggle("resaltado");
}

// Escuchamos el evento click en el botón.
botonResaltarTitulo.addEventListener("click", alternarResaltadoTitulo);

// Seleccionamos el botón para resaltar todos los párrafos.
const botonResaltarParrafos = document.querySelector("#btn-resaltar-parrafos");

// querySelectorAll devuelve un NodeList de todos los párrafos <p>.
const todosLosParrafos = document.querySelectorAll("p");

// Función para resaltar todos los párrafos usando forEach.
function resaltarParrafos() {
    todosLosParrafos.forEach((parrafo) => {
        // Aquí usamos classList.add para no eliminar otras clases.
        parrafo.classList.add("resaltado");
    });
}

// Asignamos el evento click al botón de resaltar párrafos.
botonResaltarParrafos.addEventListener("click", resaltarParrafos);

// 6) Mostrar innerHTML de un contenedor

// Seleccionamos el contenedor de notas y el botón que mostrará su innerHTML.
const contenedorNotas = document.querySelector("#notas-container");
const botonMostrarHTML = document.querySelector("#btn-mostrar-html");

// Esta función muestra el HTML interno del contenedor de notas.
function mostrarHTMLNotas() {
    const htmlActual = contenedorNotas.innerHTML;
    console.log("innerHTML actual de #notas-container:", htmlActual);
    alert("Revisa la consola para ver el innerHTML del contenedor de notas.");
}

// Asociamos la función al botón.
botonMostrarHTML.addEventListener("click", mostrarHTMLNotas);

console.log("=== Fin de la demo DOM ===");