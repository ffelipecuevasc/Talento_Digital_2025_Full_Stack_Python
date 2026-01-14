# --- ÁMBITO GLOBAL ---
# Esta variable es como el "Sol", visible para todos
energia_global = "Alta"  #


def entrenar_en_gimnasio():
    # --- ÁMBITO LOCAL ---
    # Esta variable solo existe dentro del gimnasio (la función)
    energia_local = "Agotada"  #

    print(f"--> Dentro del gimnasio:")
    # Podemos ver la global
    print(f"    Energía Global visible: {energia_global}")
    # Y usamos la local
    print(f"    Energía Local (post-entreno): {energia_local}")


def intentar_ver_local():
    # Intentamos ver la variable del gimnasio desde afuera... ¡No se podrá!
    try:
        print(energia_local)
    except NameError:
        print("--> ¡Error! No puedo ver 'energia_local' desde aquí. Ya no existe.")  # [cite: 5167]


# 1. Ejecutamos la función. Todo funciona bien dentro.
entrenar_en_gimnasio()

print("-" * 20)

# 2. Intentamos acceder a la variable local desde el ámbito global
print("--> Fuera del gimnasio:")
print(f"    Energía Global sigue siendo: {energia_global}")
intentar_ver_local()  # Esto demostrará que la variable local murió al terminar la función