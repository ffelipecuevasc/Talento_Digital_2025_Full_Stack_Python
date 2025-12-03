// Funciones en JS:
// - Concepto de función y ventajas
// - Declaración e invocación
// - Parámetros
// - Ejemplo "Sumar y Mostrar"
// - return y uso del resultado
// - Calculadora con prompt, parseFloat y switch

console.log("=== Inicio de la demo de funciones ===");

// 1. Función simple sin parámetros
// Esta función solo muestra un mensaje en consola.
// Demuestra el concepto básico: declarar e invocar una función.
function mostrarBienvenida() {
    console.log("Hola, esta es una función sin parámetros.");
    console.log("Se ejecuta cada vez que la llamamos.");
}

// Invocamos la función varias veces para ver la reutilización.
mostrarBienvenida();
mostrarBienvenida();

// 2. Función con parámetros
// Esta función recibe datos (nombre y edad) y construye un mensaje dinámico.
// Muestra cómo las funciones se adaptan según los valores de entrada.
function saludarPersona(nombre, edad) {
    console.log(`Hola ${nombre}, tienes ${edad} años. ¡Bienvenid@ a la demo de funciones!`);
}

// Invocamos la función con distintos argumentos.
saludarPersona("Ana", 25);
saludarPersona("Felipe", 30);

// 3. Funciones que colaboran: "Sumar y Mostrar"
// Separar la lógica de cálculo y de presentación hace el código más claro y reutilizable.

// Función que recibe dos números y devuelve la suma usando return.
function sumar(a, b) {
    const resultado = a + b;
    return resultado; // aquí devolvemos el valor calculado
}

// Función que recibe un resultado y lo muestra.
// Esta no devuelve nada, solo muestra información.
function mostrarResultadoSuma(resultado) {
    console.log(`El resultado de la suma es: ${resultado}`);
}

// Usamos ambas funciones juntas:
const sumaEjemplo = sumar(10, 15);       // calculamos la suma
mostrarResultadoSuma(sumaEjemplo);       // mostramos la suma

// 4. Ejemplo con return más elaborado
// Función que calcula el índice de masa corporal (IMC) como ejemplo de función de "cálculo".
function calcularIMC(peso, altura) {
    // IMC = peso / (altura * altura)
    const imc = peso / (altura * altura);
    return imc; // devolvemos el valor para usarlo afuera
}

const imcPersona = calcularIMC(70, 1.75);
console.log(`El IMC calculado es: ${imcPersona.toFixed(2)}`);

// 5. Función calculadora que usa prompt, parseFloat y switch
// Esta función agrupa toda la lógica de una pequeña calculadora.
// Se basa en ejemplos típicos del manual: pedir datos, convertir y usar switch.

function calculadora() {
    // Pedimos los dos números al usuario
    const num1Texto = prompt("Calculadora\nIngresa el primer número:");
    const num2Texto = prompt("Ingresa el segundo número:");

    // Convertimos de texto a número decimal
    const num1 = parseFloat(num1Texto);
    const num2 = parseFloat(num2Texto);

    console.log("Número 1 ingresado:", num1);
    console.log("Número 2 ingresado:", num2);

    // Si alguno de los valores no es un número, avisamos y salimos de la función
    if (isNaN(num1) || isNaN(num2)) {
        alert("Alguno de los valores no es un número válido. Intenta nuevamente.");
        console.error("Error: valores no numéricos en la calculadora.");
        return; // salimos de la función calculadora
    }

    // Pedimos la operación que desea realizar el usuario
    const opcionTexto = prompt(
        "Elige la operación que deseas realizar:\n" +
        "1 - Sumar\n" +
        "2 - Restar\n" +
        "3 - Multiplicar\n" +
        "4 - Dividir"
    );

    const opcion = parseInt(opcionTexto);

    let resultado;      // aquí guardaremos el resultado de la operación
    let descripcion;    // descripción para mostrar al usuario

    // Usamos switch para manejar cada caso según la opción elegida
    switch (opcion) {
        case 1:
            resultado = num1 + num2;
            descripcion = "suma";
            break;
        case 2:
            resultado = num1 - num2;
            descripcion = "resta";
            break;
        case 3:
            resultado = num1 * num2;
            descripcion = "multiplicación";
            break;
        case 4:
            if (num2 === 0) {
                alert("No se puede dividir por cero.");
                console.error("Intento de división por cero.");
                return; // salimos de la función si hay división por cero
            }
            resultado = num1 / num2;
            descripcion = "división";
            break;
        default:
            alert("Opción no válida. Debes elegir 1, 2, 3 o 4.");
            console.error("Opción inválida en el switch de la calculadora.");
            return; // salimos porque la opción no tiene caso definido
    }

    // Construimos un mensaje final usando template literal
    const mensajeFinal = `Has elegido la ${descripcion}.
Los números ingresados fueron: ${num1} y ${num2}.
El resultado es: ${resultado}.`;

    // Mostramos el mensaje al usuario y también en consola
    alert(mensajeFinal);
    console.log("Resultado de la calculadora:", mensajeFinal);
}

// Llamamos a la calculadora para que se ejecute al cargar la página.
// En un proyecto real podrías llamarla desde un botón o evento.
calculadora();

console.log("=== Fin de la demo de funciones ===");