
def leer_archivo_lineas(nombre_archivo):
    ruta_completa = f"datos/{nombre_archivo}"
    try:
        with open(ruta_completa, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error al leer el archivo {ruta_completa}: {e}")
        return []

def escribir_archivo_lineas(nombre_archivo, lineas):
    ruta_completa = f"datos/{nombre_archivo}"
    try:
        with open(ruta_completa, "w", encoding="utf-8") as f:
            f.writelines(lineas)
    except Exception as e:
        print(f"Error al escribir en el archivo {ruta_completa}: {e}")

def adjuntar_a_archivo(nombre_archivo, linea):
    ruta_completa = f"datos/{nombre_archivo}"
    try:
        with open(ruta_completa, "a", encoding="utf-8") as f:
            f.write(linea + "\n")
    except Exception as e:
        print(f"Error al adjuntar al archivo {ruta_completa}: {e}")