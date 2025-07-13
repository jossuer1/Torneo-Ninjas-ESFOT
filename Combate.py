import tkinter as tk 
from tkinter import messagebox
import random
import os 

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

