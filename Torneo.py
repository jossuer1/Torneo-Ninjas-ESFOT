from collections import deque
from Arbol import simular_combate  

def torneo(ninjas):
    print("=== Inicio Torneo Ninja ===")
    participantes = ninjas[:16]  

    ronda_num = 1
    cola = deque(participantes)

    while len(cola) > 1:
        print(f"\n>>> Ronda {ronda_num} ({len(cola)} participantes)")
        siguiente_ronda = deque()

        while len(cola) > 1:
            ninja1 = cola.popleft()
            ninja2 = cola.popleft()

            print(f"\nCombate: {ninja1['nombre']} vs {ninja2['nombre']}")
            resultado, ganador = simular_combate(ninja1, ninja2)
            print(resultado)

            for ninja in participantes:
                if ninja["nombre"] == ganador:
                    siguiente_ronda.append(ninja)
                    break

        cola = siguiente_ronda
        ronda_num += 1

    campeon = cola[0]
    print(f"\n🏆 Campeón absoluto del torneo: {campeon['nombre']} 🏆")
    return campeon["nombre"]


