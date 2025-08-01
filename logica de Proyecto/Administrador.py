
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
        

            