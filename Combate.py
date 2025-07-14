import tkinter as tk 
from tkinter import messagebox
import random
import os 

#--------------Cargar_Archivo-----------------------------------

def cargar_ninjas_desde_archivo(ruta="ninjas.txt"):
    lista = []
    try:
        with open(ruta, "r" , encoding= "utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) == 6:
                    lista.append({
                        "nombre": partes[0],
                        "fuerza": int(partes[1]),
                        "agilidad": int(partes[2]),
                        "resistencia": int(partes[3]),
                        "estilo": partes[4],
                        "puntos": int(partes[5])
                    })
    except FileNotFoundError:
        print("No se encontró el archivo 'ninjas.txt'.")
    return lista

#--------------Interfaz---------------------------

def iniciar_Combate():
    ninjas = cargar_ninjas_desde_archivo()
    nombres = [n['nombre'] for n in ninjas]

    ventana = tk.Tk()
    ventana.title("Combate Ninjas")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Selecciona Primer Ninja : ").pack()
    ninja1 = tk.StringVar(ventana) #guarda seleccionado del menu
    ninja1.set(nombres[0] if nombres else "")
    menu1 = tk.OptionMenu(ventana, ninja1 , *nombres)
    menu1.pack()# se guarda vodo vertical

    tk.Label(ventana, text="Selecciona Segundo Ninja : ").pack()
    ninja2 = tk.StringVar(ventana)
    ninja2.set(nombres[1] if len(nombres) > 1 else "")
    menu2 = tk.OptionMenu(ventana, ninja2, *nombres)
    menu2.pack()# se guarda vodo vertical

    tk.Button(ventana, text="Simular combate").pack(pady=10)

    ventana.mainloop()
if __name__ == "__main__":
    iniciar_Combate()

