def contador_simple():
    print("Inicio del generador")
    yield 1
    print("Entre el 1 y el 2")
    yield 2
    print("Entre el 2 y el 3")
    yield 3
    print("Fin del generador")

# Crea el generador (aún no ejecuta nada)
gen = contador_simple()

print("--- Llamada 1 ---")
print(next(gen))  # Imprime "Inicio..." y devuelve 1

print("\n--- Llamada 2 ---")
print(next(gen))  # Imprime "Entre el 1 y el 2" y devuelve 2

print("\n--- Llamada 3 ---")
print(next(gen))  # Imprime "Entre el 2 y el 3" y devuelve 3

print("\n--- Llamada 4 ---")
print(next(gen))  # ¡Error! StopIteration (se acabaron los yield)