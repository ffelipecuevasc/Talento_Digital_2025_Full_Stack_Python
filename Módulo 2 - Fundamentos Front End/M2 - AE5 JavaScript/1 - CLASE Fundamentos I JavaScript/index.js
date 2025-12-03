// Fundamentos a JS: Algoritmo con nombre y edad del usuario

// Paso 1: Mensaje de bienvenida inicial con alert()
// Explicamos al usuario que interactuará con un pequeño programa.
alert("¡Bienvenido! Vamos a probar un pequeño programa con tu nombre y tu edad.");

// Paso 2: Pedimos el nombre del usuario con prompt()
// Guardamos el resultado en una variable de tipo const, porque el nombre no debería cambiar.
const nombreUsuario = prompt("¿Cómo te llamas?");

// Mostramos en la consola lo que el usuario escribió (útil para depuración y seguimiento).
console.log("Nombre ingresado por el usuario:", nombreUsuario);

// Paso 3: Pedimos la edad del usuario con prompt()
// De nuevo, prompt devuelve texto, aunque la persona escriba un número.
const edadTexto = prompt("¿Cuántos años tienes? (escribe solo números)");

// Mostramos el texto tal como llegó desde prompt, antes de convertirlo.
console.log("Edad ingresada (como texto):", edadTexto);

// Paso 4: Convertimos la edad de texto a número usando parseInt()
// Esto nos permitirá hacer operaciones matemáticas con la edad.
const edadNumero = parseInt(edadTexto);

// Verificamos el valor numérico en la consola para asegurarnos de que la conversión funcionó.
console.log("Edad del usuario (como número):", edadNumero);

// Paso 5: Calculamos la edad del usuario para el próximo año
// Esto demuestra cómo podemos usar operaciones aritméticas con variables numéricas.
const edadProximoAnio = edadNumero + 1;

// Paso 6: Determinamos si el usuario es mayor o menor de edad
// Usamos un condicional if/else para tomar una decisión según la edad.
let mensajeMayorOMenor; // Usamos let porque el contenido cambiará según la condición

if (edadNumero >= 18) {
    // Si la edad es 18 o más, consideramos que es mayor de edad.
    mensajeMayorOMenor = "Eres mayor de edad.";
} else {
    // Si la edad es menor a 18, el usuario es menor de edad.
    mensajeMayorOMenor = "Eres menor de edad.";
}

// Mostramos en consola el resultado de esta clasificación.
console.log("Clasificación por edad:", mensajeMayorOMenor);

// Paso 7: Construimos un mensaje final usando un template literal
// Aquí combinamos nombre, edad actual, edad futura y la información de mayor/menor de edad.
const mensajeFinal = `
Hola ${nombreUsuario} ¡Bienvenido!
Tienes actualmente ${edadNumero} años.
El próximo año tendrás ${edadProximoAnio} años.
${mensajeMayorOMenor}
`;

// Mostramos el mensaje final en la consola (útil para revisar el formato completo).
console.log("Mensaje final para el usuario:", mensajeFinal);

// Paso 8: Mostramos el mismo mensaje final en una alerta
// De esta forma, el usuario ve el resultado completo en un solo cuadro.
alert(mensajeFinal);

// Paso 9: Mensaje de cierre en la consola
// Indicamos que el algoritmo terminó su ejecución.
console.log("=== Fin de Fundamentos de JS (algoritmo con nombre y edad) ===");