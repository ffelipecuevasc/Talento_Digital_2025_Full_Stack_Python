# 10. Batalla Pokémon Simplificada
# Enfoque: Lógica de juego con múltiples condiciones.

vida_pikachu = 100
ataque_enemigo = 15

while vida_pikachu > 0:
    print(f"¡Pikachu ha sido atacado! (Vida actual: {vida_pikachu})")
    vida_pikachu -= ataque_enemigo

    # Verificación extra (Bonus)
    if 0 < vida_pikachu < 20:
        print("⚠️ ¡Pikachu está en peligro! ⚠️")

    # Verificación de derrota
    if vida_pikachu <= 0:
        print("Pikachu se ha debilitado... 😵")
        break