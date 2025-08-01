import os
from autentificacion import iniciar_sesion, registrar_usuario
from Administrador import menu_administrador
from Combate import simular_combate_menu_usuario
from Torneo import menu_torneo
from gestion_ninjas import cargar_ninjas_desde_archivo, ninjas_iniciales_data, guardar_ninjas_en_archivo, ordenar_ninjas_por_puntos

def menu_usuario(user_email):
    while True:
        print(f"\n--- MENÚ DE USUARIO ({user_email}) ---")
        print("1. Simular combate 1 vs 1")
        print("2. Iniciar Torneo")
        print("3. Ver ranking de ninjas")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case '1':
                simular_combate_menu_usuario(user_email)
            case '2':
                menu_torneo()
            case '3':
                ninjas = cargar_ninjas_desde_archivo()
                ninjas_ordenados = ordenar_ninjas_por_puntos(ninjas)
                print("\n🏆 Ranking de Ninjas por Victorias 🏆")
                for i, ninja in enumerate(ninjas_ordenados):
                    print(f"{i+1}. {ninja['nombre']}: {ninja['puntos']} victorias")
            case '4':
                print("Cerrando sesión...")
                break
            case _:
                print("Opción no válida. Inténtelo de nuevo.")

def menu_principal():
    while True:
        print("\n======= MENÚ PRINCIPAL =======")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Seleccione una opción: ").strip()
        
        match opcion:
            case '1':
                resultado_login = iniciar_sesion()
                if resultado_login == True:
                    menu_administrador()
                elif resultado_login:
                    menu_usuario(resultado_login)
            case '2':
                registrar_usuario()
            case '3':
                print("¡Hasta pronto!")
                break
            case _:
                print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    if not os.path.exists("datos"):
        os.makedirs("datos")
    
    ninjas_existentes = cargar_ninjas_desde_archivo()
    if not ninjas_existentes:
        guardar_ninjas_en_archivo(ninjas_iniciales_data)
    
    menu_principal()