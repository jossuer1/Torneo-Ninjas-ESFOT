import tkinter as tk 
from tkinter import messagebox
import random
import os 

#--------------Guardar_Archivo----------------------------------

def guardar_ganador(nombre, archivo="ganadores1vs1.txt"):
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(nombre + "\n")
#--------------Mostrar Ganadores----------------------------------

def mostrar_ganadores(archivo="ganadores1vs1.txt"):

    with open(archivo, "r", encoding="utf-8") as f:
        nombres = [line.strip() for line in f if line.strip()]

    if not nombres:
        messagebox.showinfo("Ganadores", "No hay ganadores registrados aún.")
        return

    conteo_victorias = {}
    for nombre in nombres:
        if nombre in conteo_victorias:
            conteo_victorias[nombre] += 1
        else:
            conteo_victorias[nombre] = 1

    line2 = ""
    for nombre, cantidad in conteo_victorias.items():
        line2 += f"{nombre}: {cantidad} 🏆victorias\n"

    messagebox.showinfo("Ganadores registrados", line2)


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
    menu1.pack()

    tk.Label(ventana, text="Selecciona Segundo Ninja : ").pack()
    ninja2 = tk.StringVar(ventana)
    ninja2.set(nombres[1] if len(nombres) > 1 else "")
    menu2 = tk.OptionMenu(ventana, ninja2, *nombres)
    menu2.pack()

    def simular_combate():
        n1 = ninja1.get()
        n2 = ninja2.get()

        if n1 == n2:
            messagebox.showwarning("Error","Debes seleccionar dos ninjas diferentes")
            return
        
        ninja_a = None
        ninja_b = None

        for n in ninjas:
            if n["nombre"] == n1:
                ninja_a = n
            elif n["nombre"] == n2:
                ninja_b = n
        
        puntos_a = ninja_a["fuerza"] + ninja_a["agilidad"] + ninja_a["resistencia"] + random.randint(0, 5)
        puntos_b = ninja_b["fuerza"] + ninja_b["agilidad"] + ninja_b["resistencia"] + random.randint(0, 5)

        resultado = f"{n1}: {puntos_a} pts\n{n2}: {puntos_b} pts\n"

        if puntos_a > puntos_b:
            resultado += f"🏆 Ganador: {n1}"
            guardar_ganador(n1)

        elif puntos_b > puntos_a:
            resultado += f"🏆 Ganador: {n2}"
            guardar_ganador(n2)

        else:
            ganador = random.choice([n1, n2])
            resultado += f"🏆 Empate, ganador aleatorio: {ganador}"
            guardar_ganador(ganador)
        
        messagebox.showinfo("Resultado del combate", resultado)


    tk.Button(ventana, text="Simular combate",command=simular_combate).pack(pady=10)

    tk.Button(ventana, text="Ver ganadores", command=mostrar_ganadores).pack(pady=5)

    ventana.mainloop()
    

if __name__ == "__main__":
    iniciar_Combate()
