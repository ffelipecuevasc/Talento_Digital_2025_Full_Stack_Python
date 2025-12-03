/*
Demostración de los Fundamentos de JS (JavaScript)
 - Operadores aritméticos
 - Incremento/decremento y asignación compuesta
 - Comparaciones
 - Operadores lógicos
 - if / else / else if
 - switch
 - Operador ternario
 */

console.log("=== Inicio del programa de operadores y condicionales ===");

// 1. Pedimos dos números al usuario
// prompt devuelve texto, así que luego convertimos a número.
const num1Texto = prompt("Ingresa el primer número:");
const num2Texto = prompt("Ingresa el segundo número:");

// Convertimos los textos a números enteros (parseInt) o podrías usar parseFloat si quieres decimales
const num1 = parseFloat(num1Texto);
const num2 = parseFloat(num2Texto);

console.log("Número 1:", num1);
console.log("Número 2:", num2);

// 2. Operadores aritméticos básicos
// Calculamos suma, resta, multiplicación, división, módulo y potencia.
const suma = num1 + num2;
const resta = num1 - num2;
const multiplicacion = num1 * num2;
const division = num1 / num2;
const modulo = num1 % num2;
const potencia = num1 ** num2;

// Mostramos los resultados en consola
console.log("Suma:", suma);
console.log("Resta:", resta);
console.log("Multiplicación:", multiplicacion);
console.log("División:", division);
console.log("Módulo (resto):", modulo);
console.log("Potencia num1 ** num2:", potencia);

// 3. Operadores de asignación compuesta
// Creamos una variable para demostrar cómo se va actualizando.
let acumulador = 0; // empezamos en 0
console.log("Valor inicial del acumulador:", acumulador);

acumulador += num1; // sumamos num1
console.log("Acumulador tras += num1:", acumulador);

acumulador += num2; // sumamos num2
console.log("Acumulador tras += num2:", acumulador);

acumulador *= 2; // multiplicamos por 2
console.log("Acumulador tras *= 2:", acumulador);

acumulador -= 10; // restamos 10
console.log("Acumulador tras -= 10:", acumulador);

// 4. Incremento y decremento
// Incrementamos y decrementamos una variable contador.
let contador = 0;
console.log("Contador inicial:", contador);

contador++; // sumamos 1
console.log("Contador tras ++:", contador);

contador--; // restamos 1
console.log("Contador tras --:", contador);

// 5. Operadores de comparación
// Comparamos num1 y num2 usando diferentes operadores.
console.log("¿num1 > num2?", num1 > num2);
console.log("¿num1 < num2?", num1 < num2);
console.log("¿num1 >= num2?", num1 >= num2);
console.log("¿num1 <= num2?", num1 <= num2);
console.log("¿num1 === num2?", num1 === num2);
console.log("¿num1 !== num2?", num1 !== num2);

// 6. Operadores lógicos
// Creamos algunas condiciones para combinarlas.
const ambosPositivos = num1 > 0 && num2 > 0;
const algunoEsCero = num1 === 0 || num2 === 0;
const noSonIguales = !(num1 === num2);

console.log("¿Ambos números son positivos (num1 > 0 && num2 > 0)?", ambosPositivos);
console.log("¿Alguno de los números es cero (num1 === 0 || num2 === 0)?", algunoEsCero);
console.log("¿No son iguales ( !(num1 === num2) )?", noSonIguales);

// 7. Sentencias if / else / else if
// Vamos a generar un mensaje según la comparación entre num1 y num2.
let mensajeComparacion;

if (num1 > num2) {
    mensajeComparacion = `El primer número (${num1}) es mayor que el segundo (${num2}).`;
} else if (num1 < num2) {
    mensajeComparacion = `El segundo número (${num2}) es mayor que el primero (${num1}).`;
} else {
    mensajeComparacion = `Ambos números son iguales (${num1}).`;
}

console.log("Resultado de la comparación con if/else:", mensajeComparacion);

// 8. Sentencia switch
// Construimos un pequeño menú para que el usuario elija una operación principal.
const opcionTexto = prompt(
    "Elige una operación:\n" +
    "1 - Mostrar suma\n" +
    "2 - Mostrar multiplicación\n" +
    "3 - Mostrar cuál número es mayor\n" +
    "4 - Mostrar si ambos son positivos\n"
);

// Convertimos la opción a número entero
const opcion = parseInt(opcionTexto);

let mensajeSwitch;

switch (opcion) {
    case 1:
        mensajeSwitch = `Elegiste SUMA. La suma de ${num1} y ${num2} es ${suma}.`;
        break;
    case 2:
        mensajeSwitch = `Elegiste MULTIPLICACIÓN. El producto de ${num1} y ${num2} es ${multiplicacion}.`;
        break;
    case 3:
        mensajeSwitch = `Elegiste COMPARAR. ${mensajeComparacion}`;
        break;
    case 4:
        mensajeSwitch = `Elegiste POSITIVOS. ¿Ambos son positivos? ${ambosPositivos ? "Sí" : "No"}.`;
        break;
    default:
        mensajeSwitch = "No elegiste una opción válida.";
        break;
}

console.log("Resultado del switch:", mensajeSwitch);
alert(mensajeSwitch);

// 9. Operador ternario
// Creamos un mensaje corto para saber si la suma es mayor o igual a 100.
const mensajeSuma = (suma >= 100)
    ? `La suma de ${num1} y ${num2} es grande (>= 100).`
    : `La suma de ${num1} y ${num2} es menor a 100.`;

console.log("Mensaje con operador ternario:", mensajeSuma);
alert(mensajeSuma);

// 10. Mensaje final en consola
console.log("=== Fin del programa de operadores y condicionales ===");