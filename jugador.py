import Registro
import Torneo
import Combate
import random
from Arbol import generar_arbol_habilidades

def menujugador():
    ninjas = Torneo.cargar_ninjas_desde_archivo()

    while True:
        print("\n--- Menú del Jugador ---")
        print("1) Combate 1vs1 muerte súbita")
        print("2) Exámenes Chunin")
        print("3) Buscar Ninja")
        print("4) Jutsu de Ninja")
        print("5) Salir")

        op_jugador = input("Selecciona una opción: ")

        match op_jugador:
            case "1":
                if len(ninjas) < 2:
                    print("❌ No hay suficientes ninjas.")
                else:
                    ninja1, ninja2 = random.sample(ninjas, 2)
                    resultado, ganador = Combate.simular_Combate(ninja1, ninja2)
                    print("\n⚔️ Resultado del combate:\n", resultado)

            case "2":
                if len(ninjas) < 16:
                    print("❌ Se necesitan al menos 16 ninjas para pruebas Chunin")
                else:
                    print("Torneo Pruebas Chunin Iniciadas")
                    ganador = Torneo.torneo(ninjas)
                    print(f"\n🏆 ¡{ganador} ha ganado el torneo ninja!")

            case "3":
                pass

            case "4":
                print("\nÁrbol de Habilidades Generado:")
                arbol = generar_arbol_habilidades()
                arbol.mostrar()

            case "5":
                print("Cerrando experiencia Ninja.")
                break

            case _:
                print("⚠️⚠️Opción inválida.⚠️⚠️\n(Ingresa un número del 1 al 4)")

def menu_inicio():
    while True:

        print("\n=== MENÚ PRINCIPAL ===")
        print("1) Registrarse")
        print("2) Iniciar sesión")
        print("3) Administrador")
        print("4) Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                Registro.registrar_usuario()
                break
            case "2":
                if Registro.iniciar_sesion():
                    print("Bienvenido a Naruto Shippuden: Ultimate Ninja.")
                    menujugador()
            case "3":
                pass

            case "4":
                print("Cerrando experiencia Ninja.")
                break

            case _:
                print("⚠️⚠️Opción inválida.⚠️⚠️\n(Ingresa un número del 1 al 4)")

# Inicia el programa
menu_inicio()
