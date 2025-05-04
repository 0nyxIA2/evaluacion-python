import random

print("hola profe")

print("""
╔══════════════════════════╗
║   T U R N   M A G I T    ║
║    Turn-Based Combat     ║
╚══════════════════════════╝
""")


# Definición de personajes (diccionarios con atributos en tuplas)
personajes = [
    {"nombre": "Guerrero", "atributos": ("vida", 100, "ataque", 20, "defensa", 10)},
    {"nombre": "Mago",     "atributos": ("vida", 80,  "ataque", 25, "defensa", 5)},
    {"nombre": "Arquero",  "atributos": ("vida", 90,  "ataque", 18, "defensa", 8)},
    {"nombre": "marguinado","atributos": ("vida", 50,  "ataque", 45, "defensa", 1)}
]

# Acciones posibles
acciones = ["atacar", "defender"]

# Bucle del menú principal
while True:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Jugar")
    print("2. Salir")

    # Validación de la opción del menú
    opcion_menu = input("Selecciona una opción (1 o 2): ")
    while opcion_menu not in ("1", "2"):
        print("Entrada inválida. Debes ingresar 1 para Jugar o 2 para Salir.")
        opcion_menu = input("Selecciona una opción (1 o 2): ")

    if opcion_menu == "1":
        # ——— Inicio de la partida ———

        # Mostrar personajes y validar selección
        print("\nElige tu personaje:")
        for i in range(len(personajes)):
            print(f"{i+1}. {personajes[i]['nombre']}")
            
     

        while True:
            entrada = input("Ingresa el número del personaje: ")
            try:
                eleccion = int(entrada) - 1
                if 0 <= eleccion < len(personajes):
                    break
                else:
                    print(f"Debes ingresar un número entre 1 y {len(personajes)}.")
            except ValueError:
                print("Entrada inválida. Ingresa un número entero.")

        jugador = personajes[eleccion]

        # Selección de oponente distinto al jugador
        oponente = random.choice(personajes)
        while oponente == jugador:
            oponente = random.choice(personajes)

        # Extraer atributos del jugador y oponente
        jugador_vida    = jugador["atributos"][1]
        jugador_ataque  = jugador["atributos"][3]
        jugador_defensa = jugador["atributos"][5]
        oponente_vida    = oponente["atributos"][1]
        oponente_ataque  = oponente["atributos"][3]
        oponente_defensa = oponente["atributos"][5]

        print(f"\nHas elegido: {jugador['nombre']}")
        print(f"Tu oponente es: {oponente['nombre']}")

        # Bucle de combate por turnos
        turno = 1
        while jugador_vida > 0 and oponente_vida > 0:
            print(f"\n--- Turno {turno} ---")
            print(f"Tu vida: {jugador_vida} | Vida oponente: {oponente_vida}")
            print("1. Atacar")
            print("2. Defender")

            # Validar acción del jugador
            elec = input("Elige 1 o 2: ")
            while elec not in ("1", "2"):
                print("Entrada inválida. Debes ingresar 1 (Atacar) o 2 (Defender).")
                elec = input("Elige 1 o 2: ")

            if elec == "1":
                accion_jugador = "atacar"
            else:
                accion_jugador = "defender"


            print("\nHaz elegido: ",accion_jugador)
            
            # Acción aleatoria del oponente
            accion_oponente = random.choice(acciones)
            print(f"El oponente decide: {accion_oponente}")

            # Resolver daño según acciones
            if accion_jugador == "atacar" and accion_oponente == "atacar":
                jugador_vida  -= max(oponente_ataque  - jugador_defensa, 0)
                oponente_vida -= max(jugador_ataque  - oponente_defensa, 0)
                
                print("\nEl oponente te quito: ",max(oponente_ataque  - jugador_defensa, 0))
                print("Le quitas al oponente: ",max(jugador_ataque  - oponente_defensa, 0))
                
            elif accion_jugador == "atacar" and accion_oponente == "defender":
                reduccion = int(oponente_defensa * 1.5)
                oponente_vida -= max(jugador_ataque - reduccion, 0)
                
                print("\nNo revistes daños")
                print("Le quitas al oponente: ",max(jugador_ataque  - oponente_defensa, 0))
                
            elif accion_jugador == "defender" and accion_oponente == "atacar":
                reduccion = int(jugador_defensa * 1.5)
                jugador_vida  -= max(oponente_ataque - reduccion, 0)
                
                print("\nEl oponete te quito: ",max(oponente_ataque  - jugador_defensa, 0))
                
            else:
                print("Ambos se defendieron. No hubo daño.")

            turno += 1

        # Mostrar resultado final
        print("\n--- Fin del combate ---")
        if jugador_vida <= 0 and oponente_vida <= 0:
            print("¡Empate! Ambos cayeron al mismo tiempo.")
        elif jugador_vida <= 0:
            print("¡Has perdido!")
        else:
            print("¡Has ganado!")

        # ——— Fin de la partida ———

    else:  # opcion_menu == "2"
        print("¡Gracias por jugar! Hasta la próxima.")
        break
