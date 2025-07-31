import random
from Arbol import generar_arbol_habilidades  

#--------------Guardar_Archivo----------------------------------
def guardar_ganador(nombre, archivo="ganadores1vs1.txt"):
    with open(archivo, "a", encoding="utf-8") as f:
        f.write(nombre + "\n")

#--------------Mostrar Ganadores----------------------------------
def mostrar_ganadores(archivo="ganadores1vs1.txt"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            nombres = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("No hay ganadores registrados aún.")
        return

    if not nombres:
        print("No hay ganadores registrados aún.")
        return

    conteo_victorias = {}
    for nombre in nombres:
        conteo_victorias[nombre] = conteo_victorias.get(nombre, 0) + 1

    print("\n🏆 Ranking de Ganadores 🏆")
    for nombre, victorias in conteo_victorias.items():
        print(f"{nombre}: {victorias} victorias")

#--------------Cargar_Archivo-----------------------------------
def cargar_ninjas_desde_archivo(ruta="C:/Users/aleja/OneDrive/Escritorio/Proyecto_Algoritmos/Torneo-Ninjas-ESFOT/Ninjas.txt"):
    lista = []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
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
        print(f"No se encontró el archivo '{ruta}'.")
    return lista

#--------------Interfaz---------------------------

def simular_combate(ninja_a, ninja_b):
    
    arbol_a = generar_arbol_habilidades()
    arbol_b = generar_arbol_habilidades()

   
    puntos_a = ninja_a["fuerza"] + ninja_a["agilidad"] + ninja_a["resistencia"] + random.randint(0, 5)
    puntos_b = ninja_b["fuerza"] + ninja_b["agilidad"] + ninja_b["resistencia"] + random.randint(0, 5)

    
    if puntos_a > puntos_b:
        puntos_a += arbol_a.recorrido_preorden(arbol_a.raiz)# Ninja A va ganando: suma recorrido preorden (ataque)
        puntos_b += arbol_b.recorrido_postorden(arbol_b.raiz)# Ninja B va perdiendo: suma recorrido postorden (defensa)

    elif puntos_b > puntos_a:
        # Ninja B va ganando
        puntos_b += arbol_b.recorrido_preorden(arbol_b.raiz)
        puntos_a += arbol_a.recorrido_postorden(arbol_a.raiz)

    else:
        # Empate: ambos suman recorrido inorden (estrategia equilibrada)
        puntos_a += arbol_a.recorrido_inorden(arbol_a.raiz)
        puntos_b += arbol_b.recorrido_inorden(arbol_b.raiz)

    resultado = f"{ninja_a['nombre']}: {puntos_a} pts\n{ninja_b['nombre']}: {puntos_b} pts\n"

    # Determinar ganador
    if puntos_a > puntos_b:
        ganador = ninja_a["nombre"]
        resultado += f"🏆 Ganador: {ganador}"
    elif puntos_b > puntos_a:
        ganador = ninja_b["nombre"]
        resultado += f"🏆 Ganador: {ganador}"
    else:
        ganador = random.choice([ninja_a["nombre"], ninja_b["nombre"]])
        resultado += f"🏆 Empate, ganador aleatorio: {ganador}"

    guardar_ganador(ganador)

    return resultado, ganador

