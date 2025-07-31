
from Registro import registrar_usuario, iniciar_sesion
from Funciones_adm import agregar_ninja, listar_ninjas, consultar_ninja, actualizar_ninja, eliminar_ninja

def mostrar_menu_administrador():
    print("Bienvenido al menú de administrador.")
    while True:
        print("\nSeleccione una opción:")
        print("1. Agregar nuevos ninjas")
        print("2. Listar ninjas")
        print("3. Consultar un ninja por nombre o estilo de pelea")
        print("4. Actualizar atributos de un ninja")
        print("5. Eliminar ninjas")
        print("6. Salir")
        
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            agregar_ninja()
        elif opcion == "2":
            listar_ninjas()
        elif opcion == "3":
            consultar_ninja()
        elif opcion == "4":
            actualizar_ninja()
        elif opcion == "5":
            eliminar_ninja()
        elif opcion == "6":
            print("Saliendo del menú de administrador.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        

def mostrar_menu_usuario():
    print("Bienvenido al menú de usuario.")
    while True:
        print("\nSeleccione una opción:")
        print("1. Ver el árbol de habilidades")
        print("2. Simular combates uno vs uno contra otros ninjas")
        print("3. Simular un torneo completo de peleas ninja")
        print("4. Consultar el ranking actualizado")
        print("5. Guardar progreso e historial de sus combates")
        print("6. Salir")
        
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            # Lógica para ver el árbol de habilidades
            pass
        elif opcion == "2":
            # Lógica para simular combate
            pass
        elif opcion == "3":
            # Lógica para simular torneo
            pass
        elif opcion == "4":
            # Lógica para consultar ranking
            pass
        elif opcion == "5":
            # Lógica para guardar progreso
            pass
        elif opcion == "6":
            print("Saliendo del menú de usuario.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def mostrar_menu_principal():
    while True:
        print("\n---------- MENÚ PRINCIPAL ----------")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
            break  # Sale del bucle del menú una vez inicie sesión
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            