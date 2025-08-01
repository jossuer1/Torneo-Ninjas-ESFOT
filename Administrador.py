from gestion_ninjas import (
    cargar_ninjas_desde_archivo, guardar_ninjas_en_archivo, buscar_ninja_lineal,
    ordenar_ninjas_por_nombre, ordenar_ninjas_por_puntos,
)
from Arbol import  generar_arbol_habilidades
from leer_y_escribir import leer_archivo_lineas, escribir_archivo_lineas
import random

def crear_arbol_habilidades_para_ninja(ninja_nombre):
    arbol = generar_arbol_habilidades()
    habilidades_lista = []
    pila = [arbol.raiz]
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
    print(f"Árbol de habilidades creado para {ninja_nombre}.")

def agregar_ninja():
    print("\n--- Agregar Nuevo Ninja ---")
    ninjas = cargar_ninjas_desde_archivo()
    nombre = input("Ingrese el nombre del ninja: ").strip()
    if buscar_ninja_lineal(ninjas, nombre, "nombre"):
        print(f"❌ El ninja '{nombre}' ya existe. No se puede agregar.")
        return
    fuerza = random.randint(1, 10)
    agilidad = random.randint(1, 10)
    resistencia = random.randint(1, 10)
    estilo = random.choice(["Taijutsu", "Ninjutsu", "Genjutsu"])
    puntos = 0
    nuevo_ninja = {
        "nombre": nombre,
        "fuerza": fuerza, "agilidad": agilidad, "resistencia": resistencia,
        "estilo": estilo, "puntos": puntos
    }
    ninjas.append(nuevo_ninja)
    guardar_ninjas_en_archivo(ninjas)
    print(f"✅ Ninja '{nombre}' agregado exitosamente con atributos:")
    print(f"  Fuerza: {fuerza}, Agilidad: {agilidad}, Resistencia: {resistencia}, Estilo: {estilo}")
    crear_arbol = input("¿Desea crear un árbol de habilidades para este ninja ahora? (s/n): ").lower()
    if crear_arbol == 's':
        crear_arbol_habilidades_para_ninja(nombre)

def listar_ninjas_admin():
    print("\n--- Listar Ninjas ---")
    ninjas = cargar_ninjas_desde_archivo()
    if not ninjas:
        print("No hay ninjas registrados.")
        return
    print("¿Cómo desea ordenar la lista?")
    print("1. Por Nombre (A-Z)")
    print("2. Por Puntos de Victoria (Mayor a Menor)")
    opcion = input("Seleccione una opción: ").strip()
    ninjas_ordenados = []
    if opcion == '1':
        ninjas_ordenados = ordenar_ninjas_por_nombre(ninjas)
    elif opcion == '2':
        ninjas_ordenados = ordenar_ninjas_por_puntos(ninjas)
    else:
        print("Opción no válida. Se mostrarán sin ordenar.")
        ninjas_ordenados = ninjas
    for ninja in ninjas_ordenados:
        print(f"Nombre: {ninja['nombre']}, Fuerza: {ninja['fuerza']}, Agilidad: {ninja['agilidad']}, "
              f"Resistencia: {ninja['resistencia']}, Estilo: {ninja['estilo']}, Puntos: {ninja['puntos']}")

def consultar_ninja():
    print("\n--- Consultar Ninja ---")
    ninjas = cargar_ninjas_desde_archivo()
    if not ninjas:
        print("No hay ninjas registrados para consultar.")
        return
    criterio = input("Buscar ninja por (1) Nombre o (2) Estilo de pelea: ").strip()
    valor_busqueda = input("Ingrese el valor a buscar: ").strip()
    ninja_encontrado = None
    if criterio == '1':
        ninja_encontrado = buscar_ninja_lineal(ninjas, valor_busqueda, "nombre")
    elif criterio == '2':
        ninja_encontrado = buscar_ninja_lineal(ninjas, valor_busqueda, "estilo")
    else:
        print("Criterio de búsqueda no válido.")
        return
    if ninja_encontrado:
        print("\n--- Ninja Encontrado ---")
        print(f"Nombre: {ninja_encontrado['nombre']}")
        print(f"Fuerza: {ninja_encontrado['fuerza']}")
        print(f"Agilidad: {ninja_encontrado['agilidad']}")
        print(f"Resistencia: {ninja_encontrado['resistencia']}")
        print(f"Estilo: {ninja_encontrado['estilo']}")
        print(f"Puntos: {ninja_encontrado['puntos']}")
    else:
        print(f"❌ Ninja con '{valor_busqueda}' no encontrado.")

def actualizar_atributos_ninja():
    print("\n--- Actualizar Atributos de Ninja ---")
    ninjas = cargar_ninjas_desde_archivo()
    if not ninjas:
        print("No hay ninjas registrados para actualizar.")
        return
    nombre_buscar = input("Ingrese el nombre del ninja a actualizar: ").strip()
    ninja_a_actualizar = buscar_ninja_lineal(ninjas, nombre_buscar, "nombre")
    if ninja_a_actualizar:
        print(f"Ninja encontrado: {ninja_a_actualizar['nombre']}")
        print("Atributos actuales: ")
        print(f"Fuerza: {ninja_a_actualizar['fuerza']}, Agilidad: {ninja_a_actualizar['agilidad']}, "
              f"Resistencia: {ninja_a_actualizar['resistencia']}, Estilo: {ninja_a_actualizar['estilo']}")
        print("\n¿Qué atributo desea actualizar?")
        print("1. Fuerza")
        print("2. Agilidad")
        print("3. Resistencia")
        print("4. Estilo")
        print("5. Cancelar")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1' or opcion == '2' or opcion == '3':
            try:
                nuevo_valor = int(input("Ingrese el nuevo valor (1-10): "))
                if 1 <= nuevo_valor <= 10:
                    if opcion == '1': ninja_a_actualizar['fuerza'] = nuevo_valor
                    elif opcion == '2': ninja_a_actualizar['agilidad'] = nuevo_valor
                    elif opcion == '3': ninja_a_actualizar['resistencia'] = nuevo_valor
                    print("Atributo actualizado.")
                else:
                    print("Valor fuera de rango (1-10).")
            except ValueError:
                print("Entrada inválida. Debe ser un número.")
        elif opcion == '4':
            nuevo_estilo = input("Ingrese el nuevo estilo (Taijutsu, Ninjutsu, Genjutsu): ").strip()
            if nuevo_estilo in ["Taijutsu", "Ninjutsu", "Genjutsu"]:
                ninja_a_actualizar['estilo'] = nuevo_estilo
                print("Estilo actualizado.")
            else:
                print("Estilo inválido.")
        elif opcion == '5':
            print("Actualización cancelada.")
        else:
            print("Opción no válida.")
        guardar_ninjas_en_archivo(ninjas)
    else:
        print(f"❌ Ninja '{nombre_buscar}' no encontrado.")

def eliminar_ninjas():
    print("\n--- Eliminar Ninjas ---")
    ninjas = cargar_ninjas_desde_archivo()
    if not ninjas:
        print("No hay ninjas para eliminar.")
        return
    nombre_buscar = input("Ingrese el nombre del ninja a eliminar: ").strip()
    ninja_a_eliminar = buscar_ninja_lineal(ninjas, nombre_buscar, "nombre")
    if ninja_a_eliminar:
        ninjas.remove(ninja_a_eliminar)
        guardar_ninjas_en_archivo(ninjas)
        print(f"✅ Ninja '{nombre_buscar}' ha sido eliminado.")
    else:
        print(f"❌ Ninja '{nombre_buscar}' no encontrado.")

def menu_administrador():
    while True:
        print("\n--- MENÚ ADMINISTRADOR ---")
        print("1. Agregar nuevo ninja")
        print("2. Listar ninjas (con opciones de ordenamiento)")
        print("3. Consultar ninja")
        print("4. Actualizar atributos de ninja")
        print("5. Eliminar ninja")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ").strip()
        match opcion:
            case "1":
                agregar_ninja()
            case "2":
                listar_ninjas_admin()
            case "3":
                consultar_ninja()
            case "4":
                actualizar_atributos_ninja()
            case "5":
                eliminar_ninjas()
            case "6":
                print("Volviendo al menú principal...")
                break
            case _:
                print("Opción no válida. Inténtelo de nuevo.")