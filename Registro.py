import tkinter as tk 
from tkinter import messagebox
#Opcion para registrarse o iniciar sesion
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
            print("⚠️ La contraseña no cumple con los requisitos. Inténtelo de nuevo.")
print("----------Registro Exitoso------------")

with open("usuarios.txt", "a") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Identificación: {identificacion}\n")
        archivo.write(f"Edad: {edad}\n")
        archivo.write(f"Correo: {usuario}\n")
        archivo.write(f"Contraseña: {contraseña}\n")
        archivo.write("-" * 40 + "\n")  # Separador entre registros

print("Tu registro ha sido guardado exitosamente.")
#Inciar sesion despues de haberse registrado


      
