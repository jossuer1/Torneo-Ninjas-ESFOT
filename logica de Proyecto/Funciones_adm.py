import os

Ninja_Archivo = "Ninjas.txt"

def agregar_ninja():
    print("\n--- Agregar Nuevo Ninja ---")
    nombre = input("Nombre del ninja: ").strip()
    aldea = input("Aldea de origen: ").strip()
    estilo = input("Estilo de pelea (Taijutsu, Ninjutsu, Genjutsu): ").strip()
    poder = input("Nivel de poder (1-100): ").strip()

    with open(Ninja_Archivo, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{aldea},{estilo},{poder}\n")

    print("Ninja agregado exitosamente.")
    pass

def listar_ninjas():
    print("\n--- Lista de Ninjas ---")
    if not os.path.exists(Ninja_Archivo):
        print("⚠️ No hay ninjas registrados aún.")
        return

    with open(Ninja_Archivo, "r", encoding="utf-8") as f:
        for linea in f:
            nombre, aldea, estilo, poder = linea.strip().split(",")
            print(f"🌀 {nombre} | Aldea: {aldea} | Estilo: {estilo} | Poder: {poder}")
    pass

def consultar_ninja():
    print("\n--- Consultar Ninja ---")
    nombre = input("Ingrese el nombre del ninja: ").strip()

    if not os.path.exists(Ninja_Archivo):
        print("⚠️ No hay ninjas registrados aún.")
        return

    with open(Ninja_Archivo, "r", encoding="utf-8") as f:
        for linea in f:
            if nombre.lower() in linea.lower():
                print(f"🌀 {linea.strip()}")
                return

    print(f"⚠️ Ninja '{nombre}' no encontrado.")
    pass

def actualizar_ninja():
    print("\n--- Actualizar Atributos de Ninja ---")
    nombre = input("Ingrese el nombre del ninja a actualizar: ").strip()

    if not os.path.exists(Ninja_Archivo):
        print("⚠️ No hay ninjas registrados aún.")
        return

    ninjas = []
    encontrado = False

    with open(Ninja_Archivo, "r", encoding="utf-8") as f:
        for linea in f:
            if nombre.lower() in linea.lower():
                encontrado = True
                aldea = input("Nueva aldea de origen: ").strip()
                estilo = input("Nuevo estilo de pelea (Taijutsu, Ninjutsu, Genjutsu): ").strip()
                poder = input("Nuevo nivel de poder (1-100): ").strip()
                ninjas.append(f"{nombre},{aldea},{estilo},{poder}\n")
            else:
                ninjas.append(linea)

    if encontrado:
        with open(Ninja_Archivo, "w", encoding="utf-8") as f:
            f.writelines(ninjas)
        print("Atributos actualizados exitosamente.")
    else:
        print(f"⚠️ Ninja '{nombre}' no encontrado.")
    pass

def eliminar_ninja():
    print("\n--- Eliminar Ninja ---")
    nombre = input("Ingrese el nombre del ninja a eliminar: ").strip()

    if not os.path.exists(Ninja_Archivo):
        print("⚠️ No hay ninjas registrados aún.")
        return

    ninjas = []
    encontrado = False

    with open(Ninja_Archivo, "r", encoding="utf-8") as f:
        for linea in f:
            if nombre.lower() not in linea.lower():
                ninjas.append(linea)
            else:
                encontrado = True

    if encontrado:
        with open(Ninja_Archivo, "w", encoding="utf-8") as f:
            f.writelines(ninjas)
        print(f"Ninja '{nombre}' eliminado exitosamente.")
    else:
        print(f"⚠️ Ninja '{nombre}' no encontrado.")
    pass