import random
from datetime import datetime
from gestion_ninjas import cargar_ninjas_desde_archivo, buscar_ninja_lineal, guardar_ninjas_en_archivo
from Arbol import ArbolHabilidades, generar_arbol_habilidades
from leer_y_escribir import adjuntar_a_archivo, leer_archivo_lineas, escribir_archivo_lineas

def guardar_progreso_jugador(user_email, victorias, derrotas):
    archivo_personal = f"datos/combates_{user_email}.txt"
    linea_contenido = f"Victorias: {victorias}, Derrotas: {derrotas}"
    escribir_archivo_lineas(archivo_personal, [linea_contenido + "\n"])
    print(f"Progreso guardado en datos/{archivo_personal}")

def cargar_progreso_jugador(user_email):
    archivo_personal = f"datos/combates_{user_email}.txt"
    lineas = leer_archivo_lineas(archivo_personal)
    if not lineas:
        return 0, 0
    
    try:
        ultima_linea = lineas[-1].strip()
        partes = ultima_linea.split(", ")
        victorias = int(partes[0].split(": ")[1])
        derrotas = int(partes[1].split(": ")[1])
        return victorias, derrotas
    except (IndexError, ValueError):
        print(f"Advertencia: Formato de progreso inválido en datos/{archivo_personal}. Reiniciando progreso.")
        return 0, 0

def cargar_arbol_habilidades_ninja(ninja_nombre):
    lineas = leer_archivo_lineas("datos/habilidades_ninja.txt")
    if not lineas:
        return None
    
    for linea in lineas:
        if linea.strip().startswith(f"{ninja_nombre}:"):
            partes = linea.strip().split(":", 1)
            if len(partes) > 1:
                habilidades_str = partes[1]
                habilidades_para_arbol = []
                for habilidad_par_str in habilidades_str.split(";"):
                    if habilidad_par_str:
                        nombre, puntos_str = habilidad_par_str.split(",")
                        try:
                            habilidades_para_arbol.append((nombre, int(puntos_str)))
                        except ValueError:
                            print(f"Advertencia: Formato de puntos incorrecto para {nombre} en habilidades_ninja.txt")
                            continue
                
                if habilidades_para_arbol:
                    return ArbolHabilidades(habilidades_para_arbol)
            break
    return None

def guardar_arbol_habilidades_ninja(ninja_nombre, arbol_habilidades_obj):
    habilidades_lista = []
    
    # Recorrido para obtener las habilidades sin usar .join
    pila = [arbol_habilidades_obj.raiz]
    while pila:
        nodo_actual = pila.pop()
        habilidades_lista.append((nodo_actual.nombre, nodo_actual.puntos))
        if nodo_actual.derecha:
            pila.append(nodo_actual.derecha)
        if nodo_actual.izquierda:
            pila.append(nodo_actual.izquierda)

    habilidades_str = ""
    for i in range(len(habilidades_lista)):
        nombre, puntos = habilidades_lista[i]
        habilidades_str += f"{nombre},{puntos}"
        if i < len(habilidades_lista) - 1:
            habilidades_str += ";"
    
    nueva_linea_ninja = f"{ninja_nombre}:{habilidades_str}"

    lineas = leer_archivo_lineas("datos/habilidades_ninja.txt")
    lineas_actualizadas = []
    encontrado = False
    for linea in lineas:
        if linea.strip().startswith(f"{ninja_nombre}:"):
            lineas_actualizadas.append(nueva_linea_ninja + "\n")
            encontrado = True
        else:
            lineas_actualizadas.append(linea)

    if not encontrado:
        lineas_actualizadas.append(nueva_linea_ninja + "\n")

    escribir_archivo_lineas("datos/habilidades_ninja.txt", lineas_actualizadas)
    print(f"Árbol de habilidades de {ninja_nombre} guardado/actualizado en datos/habilidades_ninja.txt")

def simular_combate(ninja_a, ninja_b):
    print(f"\n--- INICIO DEL COMBATE: {ninja_a['nombre']} vs {ninja_b['nombre']} ---")
    arbol_a = cargar_arbol_habilidades_ninja(ninja_a['nombre'])
    if not arbol_a:
        arbol_a = generar_arbol_habilidades()
        print(f"No se encontró árbol de habilidades para {ninja_a['nombre']}. Se creará uno aleatorio.")
        guardar_arbol_habilidades_ninja(ninja_a['nombre'], arbol_a)
    
    arbol_b = cargar_arbol_habilidades_ninja(ninja_b['nombre'])
    if not arbol_b:
        arbol_b = generar_arbol_habilidades()
        print(f"No se encontró árbol de habilidades para {ninja_b['nombre']}. Se creará uno aleatorio.")
        guardar_arbol_habilidades_ninja(ninja_b['nombre'], arbol_b)
    
    puntos_a = ninja_a["fuerza"] + ninja_a["agilidad"] + ninja_a["resistencia"] + random.randint(0, 5)
    puntos_b = ninja_b["fuerza"] + ninja_b["agilidad"] + ninja_b["resistencia"] + random.randint(0, 5)

    print(f"Puntos iniciales: {ninja_a['nombre']}: {puntos_a}, {ninja_b['nombre']}: {puntos_b}")

    if puntos_a > puntos_b:
        print(f"{ninja_a['nombre']} va ganando, usa estrategia ofensiva (Preorden).")
        puntos_a += arbol_a.recorrido_preorden(arbol_a.raiz)
        print(f"{ninja_b['nombre']} va perdiendo, usa estrategia defensiva (Postorden).")
        puntos_b += arbol_b.recorrido_postorden(arbol_b.raiz)
    elif puntos_b > puntos_a:
        print(f"{ninja_b['nombre']} va ganando, usa estrategia ofensiva (Preorden).")
        puntos_b += arbol_b.recorrido_preorden(arbol_b.raiz)
        print(f"{ninja_a['nombre']} va perdiendo, usa estrategia defensiva (Postorden).")
        puntos_a += arbol_a.recorrido_postorden(arbol_a.raiz)
    else:
        print("Empate inicial, ambos usan estrategia equilibrada (Inorden).")
        puntos_a += arbol_a.recorrido_inorden(arbol_a.raiz)
        puntos_b += arbol_b.recorrido_inorden(arbol_b.raiz)
    
    ganador = None
    if puntos_a > puntos_b:
        ganador = ninja_a["nombre"]
    elif puntos_b > puntos_a:
        ganador = ninja_b["nombre"]
    else:
        ganador = random.choice([ninja_a["nombre"], ninja_b["nombre"]])
        print("¡Combate muy reñido! Empate, el ganador se decide aleatoriamente.")
    
    resultado_str = (f"{ninja_a['nombre']}: {puntos_a} pts\n"
                     f"{ninja_b['nombre']}: {puntos_b} pts\n"
                     f"🏆 Ganador: {ganador}")
    print(resultado_str)

    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    historial_linea = f"{ninja_a['nombre']} vs {ninja_b['nombre']} – Ganador: {ganador} – Fecha: {fecha_actual}"
    adjuntar_a_archivo("datos/combates.txt", historial_linea)
    print("Combate guardado en datos/combates.txt")

    return resultado_str, ganador

def simular_combate_menu_usuario(user_email):
    ninjas = cargar_ninjas_desde_archivo()
    if len(ninjas) < 2:
        print("Se necesitan al menos dos ninjas para el combate.")
        return

    print("\n--- Seleccione a los ninjas para el combate ---")
    for i, ninja in enumerate(ninjas):
        print(f"{i+1}. {ninja['nombre']} (Puntos: {ninja['puntos']})")
    
    ninja_a = None
    ninja_b = None
    
    while ninja_a is None:
        opcion_a = input("Seleccione el número del primer ninja: ")
        try:
            indice_a = int(opcion_a) - 1
            if 0 <= indice_a < len(ninjas):
                ninja_a = ninjas[indice_a]
            else:
                print("Número no válido. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada inválida. Debe ser un número.")
            
    while ninja_b is None:
        opcion_b = input("Seleccione el número del segundo ninja: ")
        try:
            indice_b = int(opcion_b) - 1
            if 0 <= indice_b < len(ninjas):
                if indice_a == indice_b:
                    print("No puedes seleccionar al mismo ninja. Elige otro.")
                else:
                    ninja_b = ninjas[indice_b]
            else:
                print("Número no válido. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada inválida. Debe ser un número.")

    _, ganador = simular_combate(ninja_a, ninja_b)
    
    victorias, derrotas = cargar_progreso_jugador(user_email)
    if ganador == ninja_a['nombre']:
        victorias += 1
    elif ganador == ninja_b['nombre']:
        derrotas += 1
    guardar_progreso_jugador(user_email, victorias, derrotas)
    
    # Actualizamos los puntos de victoria del ninja en el archivo principal
    ninjas_actualizados = cargar_ninjas_desde_archivo()
    for ninja in ninjas_actualizados:
        if ninja['nombre'] == ganador:
            ninja['puntos'] += 1
            break
    guardar_ninjas_en_archivo(ninjas_actualizados)