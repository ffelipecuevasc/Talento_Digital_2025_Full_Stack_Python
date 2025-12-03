// Precio de referencia del bootcamp (puedes ajustarlo si quieres)
const PRECIO_BASE = 2550000;

// Referencias a elementos del DOM
const form = document.querySelector("#form-becas");
const resultado = document.querySelector("#resultado-contenido");

// Evento principal: envío del formulario
form.addEventListener("submit", function (event) {
    event.preventDefault(); // Evita que la página se recargue

    const nombre = form.nombre.value.trim();
    const edad = Number(form.edad.value);
    const puntaje = Number(form.puntaje.value);
    const situacion = form.situacionLaboral.value;

    // Validación mínima
    if (!nombre || isNaN(edad) || isNaN(puntaje)) {
        resultado.innerHTML = `
      <p class="mb-0">
        Por favor completa tu <strong>nombre</strong>, <strong>edad</strong> y <strong>puntaje</strong>
        para hacer el cálculo.
      </p>`;
        return;
    }

    let descuento = 0;
    let becasHTML = "";

    // Beca Talento Joven
    if (edad <= 25 && puntaje >= 80) {
        descuento += 50;
        becasHTML += "<li>Beca Talento Joven (50%)</li>";
    }

    // Beca Reconversión Laboral
    if (situacion === "cesante" && puntaje >= 60) {
        descuento += 40;
        becasHTML += "<li>Beca Reconversión Laboral (40%)</li>";
    }

    // Si no aplica ninguna beca
    if (!becasHTML) {
        resultado.innerHTML = `
      <p class="mb-0">
        Hola <strong>${nombre}</strong>, con los datos ingresados no calificas
        a las becas definidas en este simulador.
      </p>`;
        return;
    }

    // Tope de descuento (opcional)
    if (descuento > 80) {
        descuento = 80;
    }

    const precioFinal = Math.round(PRECIO_BASE * (1 - descuento / 100));

    // Mostramos el resultado
    resultado.innerHTML = `
    <p class="mb-2">
      Hola <strong>${nombre}</strong>, las becas que aplican son:
    </p>
    <ul class="mb-2">
      ${becasHTML}
    </ul>
    <p class="mb-0">
      Descuento total: <strong>${descuento}%</strong><br>
      Valor estimado de tu matrícula: 
      <strong>$${precioFinal.toLocaleString("es-CL")}</strong>
    </p>`;
});

// Botón "Limpiar formulario"
form.addEventListener("reset", function () {
    resultado.innerHTML = `
    <p class="mb-0">
      Completa el formulario y presiona <strong>"Calcular beca"</strong>.
    </p>`;
});