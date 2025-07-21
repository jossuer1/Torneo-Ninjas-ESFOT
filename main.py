import tkinter as tk
from tkinter import messagebox
from Combate import iniciar_Combate  

def ventana_principal():
    raiz = tk.Tk()
    raiz.title("⛩️Torneo Ninja⛩️")
    raiz.geometry("600x400")

    tk.Label(raiz, text="⚛Ultimate Ninja Storm⚛", font=("Arial", 16)).pack(pady=10)

    btn_combate = tk.Button(raiz, text="⚔️Combate 1 vs 1⚔️", width=25, command=iniciar_Combate)
    btn_combate.pack(pady=5)

    raiz.mainloop()

if __name__ == "__main__":
    ventana_principal()
