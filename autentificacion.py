from leer_y_escribir import leer_archivo_lineas, adjuntar_a_archivo, escribir_archivo_lineas

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    if not any(c.isupper() for c in contraseña):
        return False
    if not any(c.isdigit() for c in contraseña):
        return False
    return True

def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")
    while True:
        nombre_completo = input("Ingrese un nombre y un apellido (sin números): ")
        if any(c.isdigit() for c in nombre_completo):
            print("El nombre no debe contener números. Intente de nuevo.")
        elif nombre_completo.strip() == "":
            print("El nombre no puede estar vacío. Intente de nuevo.")
        else:
            break

    while True:
        identificacion = input("Ingrese su identificación (Cédula de 10 dígitos): ")
        if not identificacion.isdigit():
            print("La cédula debe contener solo números. Intente de nuevo.")
        elif len(identificacion) != 10:
            print("La cédula debe tener exactamente 10 dígitos. Intente de nuevo.")
        else:
            break

    while True:
        edad = input("Ingrese su edad: ")
        if not edad.isdigit():
            print("La edad debe ser un número válido. Intente de nuevo.")
        elif int(edad) <= 0:
            print("La edad debe ser mayor a cero. Intente de nuevo.")
        else:
            edad = int(edad)
            break

    while True:
        usuario = input("Registre un correo válido: ").strip()
        if usuario == "":
            print("El correo no puede estar vacío. Intente de nuevo.")
        elif '@' not in usuario or '.' not in usuario:
            print("Formato de correo inválido. Intente de nuevo (ej. correo@ejemplo.com).")
        else:
            lineas_usuarios = leer_archivo_lineas("datos/usuarios.txt")
            correo_existente = False
            for i in range(0, len(lineas_usuarios), 6):
                try:
                    correo_guardado = lineas[i + 3].strip().split(": ")[1]
                    if correo_guardado == usuario:
                        correo_existente = True
                        break
                except IndexError:
                    continue
            if correo_existente:
                print("Este correo ya está registrado. Intente con otro.")
            else:
                break

    while True:
        contraseña = input("Ingrese una contraseña segura (mínimo 8 caracteres, 1 mayúscula, 1 número): ")
        if validar_contraseña(contraseña):
            print("Contraseña segura registrada.")
            break
        else:
            print("La contraseña no cumple con los requisitos. Inténtelo de nuevo.")

    print("----------Registro Exitoso------------")

    adjuntar_a_archivo("datos/usuarios.txt", f"Nombre: {nombre_completo}")
    adjuntar_a_archivo("datos/usuarios.txt", f"Identificación: {identificacion}")
    adjuntar_a_archivo("datos/usuarios.txt", f"Edad: {edad}")
    adjuntar_a_archivo("datos/usuarios.txt", f"Correo: {usuario}")
    adjuntar_a_archivo("datos/usuarios.txt", f"Contraseña: {contraseña}")
    adjuntar_a_archivo("datos/usuarios.txt", "-" * 40)

    print("Tu registro ha sido guardado exitosamente.")

def iniciar_sesion():
    print("---------------Iniciar Sesión--------------------")
    max_intentos = 3
    intentos = 0
    while intentos < max_intentos:
        usuario_login = input("Ingrese su correo: ")
        contraseña_login = input("Ingrese su contraseña: ")

        if usuario_login == "admin@ninjas.com" and contraseña_login == "Admin123":
            print("Inicio de sesión de ADMINISTRADOR exitoso.")
            return True
        
        lineas = leer_archivo_lineas("datos/usuarios.txt")
        for i in range(0, len(lineas), 6):
            try:
                correo_guardado = lineas[i + 3].strip().split(": ")[1]
                contraseña_guardada = lineas[i + 4].strip().split(": ")[1]
                if correo_guardado == usuario_login and contraseña_guardada == contraseña_login:
                    print(f"Inicio de sesión exitoso. ¡Bienvenido, {lineas[i].strip().split(': ')[1]}!")
                    return correo_guardado
            except (IndexError, AttributeError):
                continue

        print("Usuario o contraseña incorrectos.")
        intentos += 1
        if intentos < max_intentos:
            print(f"Le quedan {max_intentos - intentos} intentos.")
    print("Ha excedido el número de intentos. Volviendo al menú principal.")
    return None