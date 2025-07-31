import random
from Torneo import torneo, cargar_ninjas_desde_archivo
from Combate import simular_combate
from Registro import registrar_usuario, iniciar_sesion
from Arbol import generar_arbol_habilidades

def menujugador():
    ninjas = cargar_ninjas_desde_archivo()

    if not ninjas:
        print("❌ No se pudieron cargar los ninjas. Verifica que el archivo 'ninjas.txt' exista.")
        return

    while True:
        print("\n--- Menú del Jugador ---")
        print("1) Combate 1vs1 muerte súbita")
        print("2) Exámenes Chunin")
        print("3) Buscar Ninja")
        print("4) Jutsu de Ninja")
        print("5) Salir")

        op_jugador = input("Selecciona una opción: ").strip()

        match op_jugador:
            case "1":
                if len(ninjas) < 2:
                    print("❌ No hay suficientes ninjas.")
                else:
                    ninja_a, ninja_b = random.sample(ninjas, 2)
                    resultado, ganador = simular_combate(ninja_a, ninja_b)
                    print("\n⚔️ Resultado del combate:\n", resultado)

            case "2":
                if len(ninjas) < 16:
                    print("Se necesitan al menos 16 ninjas para pruebas Chunin.")
                else:
                    print(" Torneo Pruebas Chunin Iniciadas")
                    ganador = torneo(ninjas)
                    print(f"\n ¡{ganador} ha ganado el torneo ninja!")

            case "3":
                print(" Función Buscar Ninja aún no implementada.")
                pass

            case "4":
                print("\n Árbol de Habilidades Generado:")
                arbol = generar_arbol_habilidades()
                arbol.mostrar()

            case "5":
                print(" Cerrando experiencia Ninja.")
                break

            case _:
                print("⚠️ Opción inválida. (Ingresa un número del 1 al 5)")

def Menu_inicio():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1) Registrarse")
        print("2) Iniciar sesión")
        print("3) Salir")
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                registrar_usuario()
            case "2":
                if iniciar_sesion():
                    print("Bienvenido a Naruto Shippuden: Ultimate Ninja.")
                    menujugador()
            case "3":
                print(" Cerrando experiencia Ninja.")
                exit()
            case _:
                print("⚠️ Opción inválida. (Ingresa un número del 1 al 3)")

if __name__ == "__main__":
    Menu_inicio()
