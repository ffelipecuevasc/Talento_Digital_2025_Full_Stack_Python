# SOLUCIÓN A LA DEMO PRÁCTICA (Páginas 17-18 del PDF M3 AE6)

# 1. Procedimiento para imprimir detalles del usuario [cite: 4181]
# Este procedimiento recibe nombre, edad y una lista de intereses.
def mostrar_perfil_usuario(nombre, edad, intereses):
    print(f"--- Perfil de {nombre} ---")
    print(f"Edad: {edad} años")

    print("Intereses:")
    # Recorremos la lista de intereses con un bucle for [cite: 4184]
    for interes in intereses:
        print(f" - {interes}")
    print("--------------------------")


# 2. Procedimiento para verificar la edad (Control de acceso) [cite: 4186]
# Evalúa si la persona es mayor de edad para entrar a la plataforma.
def verificar_acceso(edad):
    # Usamos condicionales dentro del procedimiento [cite: 4189]
    if edad >= 18:
        print("✅ Acceso CONCEDIDO: Bienvenido a la plataforma.")  # [cite: 4188]
    else:
        print("⛔ Acceso DENEGADO: Debes ser mayor de 18 años.")  # [cite: 4188]


# --- EJECUCIÓN DE PRUEBA ---

# Definimos una lista de intereses (ámbito global)
mis_hobbies = ["Python", "Guitarra", "Videojuegos"]

# Llamamos al primer procedimiento
mostrar_perfil_usuario("Carlos", 20, mis_hobbies)

# Llamamos al segundo procedimiento con diferentes edades
print("\nPrueba de acceso 1:")
verificar_acceso(20)

print("\nPrueba de acceso 2:")
verificar_acceso(15)