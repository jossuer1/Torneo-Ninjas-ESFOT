import tkinter as tk
from tkinter import messagebox

# Opción para registrarse o iniciar sesión
while True:
    print("---------------Registro--------------------")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    registro = input("Seleccione la opción a ejecutar (1) o (2): ")
  
    if registro == "1" or registro == "2":
        break  
    else:
        print(" Opción no válida. Por favor, ingrese (1) o (2): ")

# Opción para registrar nuevo usuario
if registro == "1":
    nombre = input("Ingrese un nombre y un apellido: ")
    identificacion = input("Ingrese su identificación (Cédula o pasaporte): ")
    edad = input("Ingrese su edad: ")
    usuario = input("Registre un correo válido: ")
    
    def validar_contraseña(contraseña):
        # Ver si es menor a 8 para retornar un falso
        if len(contraseña) < 8:
            return False
        
        # Verificar si hay al menos una mayúscula
        tiene_mayuscula = False
        for c in contraseña:
            if c.isupper():
                tiene_mayuscula = True
                break
        
        if not tiene_mayuscula:
            return False
        
        # Verificar si hay al menos un número
        tiene_numero = False
        for c in contraseña:
            if c >= '0' and c <= '9':  # Comprobar si el carácter es un número
                tiene_numero = True
                break
        
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
            print(" La contraseña no cumple con los requisitos. Inténtelo de nuevo.")
    print("----------Registro Exitoso------------")

    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Identificación: {identificacion}\n")
        archivo.write(f"Edad: {edad}\n")
        archivo.write(f"Correo: {usuario}\n")
        archivo.write(f"Contraseña: {contraseña}\n")
        archivo.write("-" * 40 + "\n")  # Separador entre registros

    print("Tu registro ha sido guardado exitosamente.")

# Opción de iniciar sesión
elif registro == "2":
    print("---------------Iniciar Sesión--------------------")
    
    while True:  # Bucle while para solicitar datos hasta que sean correctos
        usuario_login = input("Ingrese su correo: ")
        contraseña_login = input("Ingrese su contraseña: ")
        
        # Verificar si el usuario y la contraseña existen en el archivo
        usuario_encontrado = False
        with open("usuarios.txt", "r") as archivo:
            lineas = archivo.readlines()
            for i in range(0, len(lineas), 6):  # Cada usuario ocupa 6 líneas
                usuario_guardado = lineas[i + 3].strip().split(": ")[1]  # Correo guardado en la línea 4
                contraseña_guardada = lineas[i + 4].strip().split(": ")[1]  # Contraseña guardada en la línea 5

                if usuario_guardado == usuario_login and contraseña_guardada == contraseña_login:
                    usuario_encontrado = True
                    break

        if usuario_encontrado:
            print("Inicio de sesión exitoso.")
            break  # Sale del bucle mientras los datos son correctos
        else:
            print("Usuario o contraseña incorrectos. Inténtelo de nuevo.")
