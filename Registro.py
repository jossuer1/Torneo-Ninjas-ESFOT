from jugador import menujugador

def registrar_usuario():
    # Opción para registrar nuevo usuario
    nombre = input("Ingrese un nombre y un apellido: ")
    identificacion = input("Ingrese su identificación (Cédula o pasaporte): ")
    edad = input("Ingrese su edad: ")
    usuario = input("Registre un correo válido: ")

    def validar_contraseña(contraseña):
        # Ver si es menor a 8 para retornar un falso
        if len(contraseña) < 8:
            return False

        # Verificar si hay al menos una mayúscula
        tiene_mayuscula = any(c.isupper() for c in contraseña)
        if not tiene_mayuscula:
            return False

        # Verificar si hay al menos un número
        tiene_numero = any(c.isdigit() for c in contraseña)
        if not tiene_numero:
            return False

        return True

    # Bucle para asegurar que la contraseña cumpla los requisitos
    while True:
        contraseña = input("Ingrese una contraseña segura (mínimo 8 caracteres, 1 mayúscula, 1 número): ")
        if validar_contraseña(contraseña):
            print("Contraseña segura registrada.")
            break
        else:
            print("La contraseña no cumple con los requisitos. Inténtelo de nuevo.")

    print("----------Registro Exitoso------------")

    with open("usuarios.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Identificación: {identificacion}\n")
        archivo.write(f"Edad: {edad}\n")
        archivo.write(f"Correo: {usuario}\n")
        archivo.write(f"Contraseña: {contraseña}\n")
        archivo.write("-" * 40 + "\n")  # Separador entre registros

    print("Tu registro ha sido guardado exitosamente.")


def iniciar_sesion():
    # Opción de iniciar sesión
    print("---------------Iniciar Sesión--------------------")

    while True:  # Bucle while para solicitar datos hasta que sean correctos
        usuario_login = input("Ingrese su correo: ")
        contraseña_login = input("Ingrese su contraseña: ")

        # Verificar si el usuario y la contraseña existen en el archivo
        usuario_encontrado = False
        administrador = False  # Indicador de si el usuario es administrador
        with open("usuarios.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for i in range(0, len(lineas), 6):  # Cada usuario ocupa 6 líneas
                usuario_guardado = lineas[i + 3].strip().split(": ")[1]
                contraseña_guardada = lineas[i + 4].strip().split(": ")[1]

                if usuario_guardado == usuario_login and contraseña_guardada == contraseña_login:
                    usuario_encontrado = True
                    
                    # Verificar si las credenciales coinciden con las del administrador
                    if usuario_login == "admin@ninjas.com" and contraseña_login == "Admin123":
                        administrador = True
                    break

        if usuario_encontrado:
            print("Inicio de sesión exitoso.")
            # Si es administrador, abrir el menú de administrador
            if administrador:
                mostrar_menu_administrador()
            else:
                menujugador()
            return True
        else:
            print("Usuario o contraseña incorrectos. Inténtelo de nuevo.")

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
            # Lógica para agregar ninjas
            pass
        elif opcion == "2":
            # Lógica para listar ninjas
            pass
        elif opcion == "3":
            # Lógica para consultar un ninja
            pass
        elif opcion == "4":
            # Lógica para actualizar atributos
            pass
        elif opcion == "5":
            # Lógica para eliminar ninjas
            pass
        elif opcion == "6":
            print("Saliendo del menú de administrador.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

