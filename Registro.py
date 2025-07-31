from jugador import menujugador

def registrar_usuario():
    # Validar nombre (sin números)
    while True:
        nombre = input("Ingrese un nombre y un apellido (sin números): ")
        if any(c.isdigit() for c in nombre):
            print("El nombre no debe contener números. Intente de nuevo.")
        elif nombre.strip() == "":
            print("El nombre no puede estar vacío. Intente de nuevo.")
        else:
            break

    # Validar identificación (cédula de 10 números)
    while True:
        identificacion = input("Ingrese su identificación (Cédula de 10 dígitos): ")
        if not identificacion.isdigit():
            print("La cédula debe contener solo números. Intente de nuevo.")
        elif len(identificacion) != 10:
            print("La cédula debe tener exactamente 10 dígitos. Intente de nuevo.")
        else:
            break

    # Validar edad (número positivo)
    while True:
        edad = input("Ingrese su edad: ")
        if not edad.isdigit():
            print("La edad debe ser un número válido. Intente de nuevo.")
        elif int(edad) <= 0:
            print("La edad debe ser mayor a cero. Intente de nuevo.")
        else:
            break

    # Validar correo (no vacío, puedes agregar más validaciones si quieres)
    while True:
        usuario = input("Registre un correo válido: ").strip()
        if usuario == "":
            print("El correo no puede estar vacío. Intente de nuevo.")
        else:
            break

    def validar_contraseña(contraseña):
        if len(contraseña) < 8:
            return False
        if not any(c.isupper() for c in contraseña):
            return False
        if not any(c.isdigit() for c in contraseña):
            return False
        return True

    # Bucle para validar contraseña
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
        archivo.write("-" * 40 + "\n")

    print("Tu registro ha sido guardado exitosamente.")


def iniciar_sesion():
    print("---------------Iniciar Sesión--------------------")

    while True:
        usuario_login = input("Ingrese su correo: ")
        contraseña_login = input("Ingrese su contraseña: ")

        usuario_encontrado = False
        administrador = False
        with open("usuarios.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for i in range(0, len(lineas), 6):
                usuario_guardado = lineas[i + 3].strip().split(": ")[1]
                contraseña_guardada = lineas[i + 4].strip().split(": ")[1]

                if usuario_guardado == usuario_login and contraseña_guardada == contraseña_login:
                    usuario_encontrado = True
                    if usuario_login == "admin@ninjas.com" and contraseña_login == "Admin123":
                        administrador = True
                    break

        if usuario_encontrado:
            print("Inicio de sesión exitoso.")
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

