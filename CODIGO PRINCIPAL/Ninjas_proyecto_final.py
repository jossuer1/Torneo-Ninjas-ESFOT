import random
from collections import deque
from datetime import datetime 

class NodoHabilidad:
    def __init__(self, nombre, puntos):
        self.nombre = nombre
        self.puntos = puntos
        self.izquierda = None
        self.derecha = None


class ArbolHabilidades: 
    def __init__(self, habilidades=None):
        self.raiz = None
        if habilidades:
            for nombre, puntos in habilidades:
                self.insertar(nombre, puntos)

    def insertar(self, nombre, puntos):
        nuevo = NodoHabilidad(nombre, puntos)
        if self.raiz is None:
            self.raiz = nuevo
        else:
            self._insertar_recursivo(self.raiz, nuevo)

    def _insertar_recursivo(self, actual, nuevo):
        if nuevo.puntos <= actual.puntos:
            if actual.izquierda is None:
                actual.izquierda = nuevo
            else:
                self._insertar_recursivo(actual.izquierda, nuevo)
        else:
            if actual.derecha is None:
                actual.derecha = nuevo
            else:
                self._insertar_recursivo(actual.derecha, nuevo)


    def recorrido_preorden(self, nodo):
        if nodo is None:
            return 0
        return nodo.puntos + self.recorrido_preorden(nodo.izquierda) + self.recorrido_preorden(nodo.derecha)

    def recorrido_inorden(self, nodo):
        if nodo is None:
            return 0
        return self.recorrido_inorden(nodo.izquierda) + nodo.puntos + self.recorrido_inorden(nodo.derecha)

    def recorrido_postorden(self, nodo):
        if nodo is None:
            return 0
        return self.recorrido_postorden(nodo.izquierda) + self.recorrido_postorden(nodo.derecha) + nodo.puntos


    def mostrar(self, nodo=None, nivel=0, lado="Raíz"):
        if nivel == 0 and nodo is None:
            nodo = self.raiz
        if nodo is None:
            return
        print(" " * (nivel * 4) + f"{lado}: {nodo.nombre} ({nodo.puntos})")
        self.mostrar(nodo.izquierda, nivel + 1, "Izq")
        self.mostrar(nodo.derecha, nivel + 1, "Der")

   
    def obtener_habilidades_en_lista_iterativo(self):
        """Devuelve una lista plana de todas las habilidades (nombre, puntos) en el árbol de forma iterativa."""
        lista = []
        if not self.raiz:
            return lista

        pila = [self.raiz] 

        while pila:
            nodo_actual = pila.pop() 
            lista.append((nodo_actual.nombre, nodo_actual.puntos)) 
            
            if nodo_actual.derecha:
                pila.append(nodo_actual.derecha)
            if nodo_actual.izquierda:
                pila.append(nodo_actual.izquierda)
        return lista
def generar_arbol_habilidades():
    habilidades = [
        ("Rasengan", 5), ("Chidori", 5), ("Jutsu Clon de Sombra", 3),
        ("Amaterasu", 6), ("Susanoo", 7), ("Byakugan", 4),
        ("Modo Sabio", 6), ("Katon: Bola de Fuego", 3), ("Taijutsu", 2),
        ("Kirin", 5), ("Kagemane no Jutsu", 4), ("Arena de Gaara", 4),
        ("Invocación: Gamabunta", 6), ("Genjutsu: Tsukuyomi", 7), ("Elemento Madera", 6)
    ]
    seleccionados = random.sample(habilidades, 5)
    arbol = ArbolHabilidades(seleccionados)
    return arbol


def leer_archivo_lineas(ruta_archivo):
    """Lee el contenido de un archivo y devuelve una lista de líneas.
    Cada línea es un string. Devuelve lista vacía si el archivo no existe o hay error."""
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error al leer el archivo {ruta_archivo}: {e}")
        return []

def escribir_archivo_lineas(ruta_archivo, lineas):
    """Escribe una lista de líneas en un archivo (sobrescribe si existe)."""
    try:
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            f.writelines(lineas)
    except Exception as e:
        print(f"Error al escribir en el archivo {ruta_archivo}: {e}")

def adjuntar_a_archivo(ruta_archivo, linea):
    """Adjunta una línea de texto al final de un archivo."""
    try:
        with open(ruta_archivo, "a", encoding="utf-8") as f:
            f.write(linea + "\n") 
    except Exception as e:
        print(f"Error al adjuntar al archivo {ruta_archivo}: {e}")

def ordenar_ninjas_por_puntos(ninjas):
    """Ordena una lista de ninjas por sus puntos de forma descendente."""
    return sorted(ninjas, key=lambda ninja: ninja['puntos'], reverse=True)

def ordenar_ninjas_por_nombre(ninjas):
    """Ordena una lista de ninjas por sus nombres alfabéticamente."""
    return sorted(ninjas, key=lambda ninja: ninja['nombre'].lower())

def buscar_ninja_lineal(ninjas, valor_busqueda, campo="nombre"):
    """Busca un ninja por nombre o por un campo específico (ej: 'estilo')
    usando búsqueda lineal. Devuelve el diccionario del ninja o None si no lo encuentra."""
    for ninja in ninjas:
        if str(ninja.get(campo, '')).lower() == str(valor_busqueda).lower():
            return ninja
    return None

ninjas_iniciales_data = [
    {"nombre": "Naruto", "fuerza": 10, "agilidad": 9, "resistencia": 8, "estilo": "Ninjutsu", "puntos": 3},
    {"nombre": "Sasuke", "fuerza": 9, "agilidad": 10, "resistencia": 7, "estilo": "Genjutsu", "puntos": 2},
    {"nombre": "Sakura", "fuerza": 7, "agilidad": 9, "resistencia": 9, "estilo": "Taijutsu", "puntos": 1},
    {"nombre": "Kakashi", "fuerza": 8, "agilidad": 9, "resistencia": 8, "estilo": "Ninjutsu", "puntos": 2},
    {"nombre": "Rock Lee", "fuerza": 9, "agilidad": 10, "resistencia": 10, "estilo": "Taijutsu", "puntos": 2},
    {"nombre": "Neji", "fuerza": 8, "agilidad": 9, "resistencia": 8, "estilo": "Byakugan", "puntos": 1},
    {"nombre": "Gaara", "fuerza": 9, "agilidad": 7, "resistencia": 10, "estilo": "Defensivo", "puntos": 1},
    {"nombre": "Hinata", "fuerza": 7, "agilidad": 8, "resistencia": 7, "estilo": "Byakugan", "puntos": 0},
    {"nombre": "Shikamaru", "fuerza": 6, "agilidad": 7, "resistencia": 8, "estilo": "Estrategia", "puntos": 1},
    {"nombre": "Jiraiya", "fuerza": 10, "agilidad": 7, "resistencia": 9, "estilo": "Sennin", "puntos": 2},
    {"nombre": "Itachi", "fuerza": 9, "agilidad": 9, "resistencia": 8, "estilo": "Genjutsu", "puntos": 5},
    {"nombre": "Killer Bee", "fuerza": 10, "agilidad": 8, "resistencia": 9, "estilo": "Raiton", "puntos": 4},
    {"nombre": "Orochimaru", "fuerza": 8, "agilidad": 7, "resistencia": 7, "estilo": "Serpiente", "puntos": 3},
    {"nombre": "Tsunade", "fuerza": 9, "agilidad": 7, "resistencia": 10, "estilo": "Médico", "puntos": 3},
    {"nombre": "Minato", "fuerza": 10, "agilidad": 10, "resistencia": 8, "estilo": "Espacio-Tiempo", "puntos": 5},
    {"nombre": "Madara", "fuerza": 10, "agilidad": 9, "resistencia": 10, "estilo": "Uchiha", "puntos": 6}
]

def cargar_ninjas_desde_archivo(ruta="ninjas.txt"):
    """Carga ninjas desde el archivo, devolviendo una lista de diccionarios."""
    lista = []
    lineas = leer_archivo_lineas(ruta)
    for linea in lineas:
        partes = linea.strip().split(",")
        if len(partes) == 6:
            try:
                lista.append({
                    "nombre": partes[0],
                    "fuerza": int(partes[1]),
                    "agilidad": int(partes[2]),
                    "resistencia": int(partes[3]),
                    "estilo": partes[4],
                    "puntos": int(partes[5])
                })
            except ValueError:
                print(f"Advertencia: Línea con formato incorrecto en {ruta}: {linea.strip()}")
                continue
    return lista

def guardar_ninjas_en_archivo(ninjas_list, ruta="ninjas.txt"):
    """Guarda la lista completa de ninjas (diccionarios), sobrescribiendo el archivo."""
    lineas_a_guardar = []
    for ninja in ninjas_list:
        lineas_a_guardar.append(f"{ninja['nombre']},{ninja['fuerza']},{ninja['agilidad']},{ninja['resistencia']},{ninja['estilo']},{ninja['puntos']}\n")
    escribir_archivo_lineas(ruta, lineas_a_guardar)
    print(f"Ninjas actualizados y guardados en {ruta}")

def guardar_arbol_habilidades_ninja(ninja_nombre, arbol_habilidades_obj):
    """Guarda el árbol de habilidades de un ninja en habilidades_ninja.txt.
    Formato: NinjaNombre:habilidad1,puntos1;habilidad2,puntos2;..."""
    
    habilidades_lista = arbol_habilidades_obj.obtener_habilidades_en_lista_iterativo()

    habilidades_str = ";".join([f"{nombre},{puntos}" for nombre, puntos in habilidades_lista])
 
    nueva_linea_ninja = f"{ninja_nombre}:{habilidades_str}"

    lineas = leer_archivo_lineas("habilidades_ninja.txt")
    
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

    escribir_archivo_lineas("habilidades_ninja.txt", lineas_actualizadas)
    print(f"Árbol de habilidades de {ninja_nombre} guardado/actualizado en habilidades_ninja.txt")

def cargar_arbol_habilidades_ninja(ninja_nombre):
    """Carga el árbol de habilidades de un ninja desde habilidades_ninja.txt."""
    lineas = leer_archivo_lineas("habilidades_ninja.txt")
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

def guardar_ganador(nombre, archivo="ganadores1vs1.txt"):
    adjuntar_a_archivo(archivo, nombre) 


def mostrar_ganadores(archivo="ganadores1vs1.txt"):
    nombres = [line.strip() for line in leer_archivo_lineas(archivo) if line.strip()]

    if not nombres:
        print("No hay ganadores registrados aún.")
        return

    conteo_victorias = {}
    for nombre in nombres:
        conteo_victorias[nombre] = conteo_victorias.get(nombre, 0) + 1

    print("\n🏆 Ranking de Ganadores 🏆")
    for nombre, victorias in conteo_victorias.items():
        print(f"{nombre}: {victorias} victorias")

def simular_combate(ninja_a, ninja_b):
    print(f"\n--- INICIO DEL COMBATE: {ninja_a['nombre']} vs {ninja_b['nombre']} ---")

    arbol_a = cargar_arbol_habilidades_ninja(ninja_a['nombre'])
    if not arbol_a:
        arbol_a = generar_arbol_habilidades() # Generar uno aleatorio
        print(f"No se encontró árbol de habilidades para {ninja_a['nombre']}. Se creará uno aleatorio.")
        guardar_arbol_habilidades_ninja(ninja_a['nombre'], arbol_a) # Guardar el nuevo árbol
        
    arbol_b = cargar_arbol_habilidades_ninja(ninja_b['nombre'])
    if not arbol_b:
        arbol_b = generar_arbol_habilidades() 
        print(f"No se encontró árbol de habilidades para {ninja_b['nombre']}. Se creará uno aleatorio.")
        guardar_arbol_habilidades_ninja(ninja_b['nombre'], arbol_b) # Guardar el nuevo árbol
    

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
    else: # Empate inicial
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
    adjuntar_a_archivo("combates.txt", historial_linea)
    print(f"Combate guardado en combates.txt")

    return resultado_str, ganador

def mostrar_ranking_combates():
    """Muestra el ranking de ninjas por victorias acumuladas."""
    print("\n--- Ranking de Combates ---")
    
    ninjas_actualizados = cargar_ninjas_desde_archivo("ninjas.txt") 
    
    if not ninjas_actualizados:
        print("No hay ninjas registrados para mostrar el ranking.")
        return

    ranking_ordenado = ordenar_ninjas_por_puntos(ninjas_actualizados)
    
    if not ranking_ordenado:
        print("No hay ninjas con puntos de victoria para el ranking.")
        return

    print("🏆 Ranking de Ninjas por Victorias 🏆")
    for i, ninja in enumerate(ranking_ordenado):
        print(f"{i+1}. {ninja['nombre']}: {ninja['puntos']} victorias")


def guardar_progreso_jugador(user_email, victorias, derrotas):
    """Guarda el progreso de combates de un jugador en su archivo personal."""
    archivo_personal = f"combates_{user_email}.txt"
    linea_contenido = f"Victorias: {victorias}, Derrotas: {derrotas}"
    escribir_archivo_lineas(archivo_personal, [linea_contenido + "\n"]) # Sobrescribir siempre con el último estado
    print(f"Progreso guardado en {archivo_personal}")

def cargar_progreso_jugador(user_email):
    """Carga el progreso de combates de un jugador desde su archivo personal."""
    archivo_personal = f"combates_{user_email}.txt"
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
        print(f"Advertencia: Formato de progreso inválido en {archivo_personal}. Reiniciando progreso.")
        return 0, 0


def torneo(ninjas_participantes):
    print("-"*30)
    print("=== Inicio Torneo Chunin Ninja ===")
    

    if len(ninjas_participantes) < 16:
        print("No hay suficientes ninjas para el torneo (se necesitan 16).")
        return None
    
  
    random.shuffle(ninjas_participantes) 
    participantes = ninjas_participantes[:16] 

    ronda_num = 1
    cola = deque(participantes)

    while len(cola) > 1:
        print(f"\n>>> Ronda {ronda_num} ({len(cola)} participantes restantes)")
        siguiente_ronda = deque()

     
        parejas_ronda = []
        while len(cola) >= 2:
            ninja1 = cola.popleft()
            ninja2 = cola.popleft()
            parejas_ronda.append((ninja1, ninja2))
        
        if len(cola) == 1:
            siguiente_ronda.append(cola.popleft())
            print(f"Ninja '{siguiente_ronda[-1]['nombre']}' pasa directamente a la siguiente ronda (Bye).")


        for ninja1, ninja2 in parejas_ronda:
            print(f"\nCombate: {ninja1['nombre']} vs {ninja2['nombre']}")
        
            resultado, ganador_nombre = simular_combate(ninja1, ninja2) 
            print(resultado)

            
            for n in ninjas_participantes:
                if n['nombre'] == ganador_nombre:
                    n['puntos'] += 1
                    siguiente_ronda.append(n) 
                    break

        cola = siguiente_ronda
        ronda_num += 1

    campeon = cola[0]
    print(f"\n🏆 Campeón Chunin del torneo: {campeon['nombre']} 🏆")
    print("-"*30)
    
    return campeon["nombre"]


def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    if not any(c.isupper() for c in contraseña):
        return False
    if not any(c.isdigit() for c in contraseña):
        return False
    return True

def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")
    while True:
        nombre_completo = input("Ingrese un nombre y un apellido (sin números): ")
        if any(c.isdigit() for c in nombre_completo):
            print("El nombre no debe contener números. Intente de nuevo.")
        elif nombre_completo.strip() == "":
            print("El nombre no puede estar vacío. Intente de nuevo.")
        else:
            break

    while True:
        identificacion = input("Ingrese su identificación (Cédula de 10 dígitos): ")
        if not identificacion.isdigit():
            print("La cédula debe contener solo números. Intente de nuevo.")
        elif len(identificacion) != 10:
            print("La cédula debe tener exactamente 10 dígitos. Intente de nuevo.")
        else:
            break

    while True:
        edad = input("Ingrese su edad: ")
        if not edad.isdigit():
            print("La edad debe ser un número válido. Intente de nuevo.")
        elif int(edad) <= 0:
            print("La edad debe ser mayor a cero. Intente de nuevo.")
        elif int(edad) >= 100:
            print("La edad debe ser menor a cien. Intenta de nuevo.")
        else:
            edad = int(edad)
            break

    while True:
        usuario = input("Registre un correo válido: ").strip()
        if usuario == "":
            print("El correo no puede estar vacío. Intente de nuevo.")
        elif '@' not in usuario or '.' not in usuario:
             print("Formato de correo inválido. Intente de nuevo (ej. correo@ejemplo.com).")
        else:
            lineas_usuarios = leer_archivo_lineas("usuarios.txt") 
            correo_existente = False
            for i in range(0, len(lineas_usuarios), 6): 
                try:
                    correo_guardado = lineas_usuarios[i + 3].strip().split(": ")[1] 
                    if correo_guardado == usuario:
                        correo_existente = True
                        break
                except IndexError:
                    continue 
            if correo_existente:
                print("Este correo ya está registrado. Intente con otro.")
            else:
                break

    while True:
        contraseña = input("Ingrese una contraseña segura (mínimo 8 caracteres, 1 mayúscula, 1 número): ")
        if validar_contraseña(contraseña):
            print("Contraseña segura registrada.")
            break
        else:
            print("La contraseña no cumple con los requisitos. Inténtelo de nuevo.")

    print("----------Registro Exitoso------------")

    adjuntar_a_archivo("usuarios.txt", f"Nombre: {nombre_completo}")
    adjuntar_a_archivo("usuarios.txt", f"Identificación: {identificacion}")
    adjuntar_a_archivo("usuarios.txt", f"Edad: {edad}")
    adjuntar_a_archivo("usuarios.txt", f"Correo: {usuario}")
    adjuntar_a_archivo("usuarios.txt", f"Contraseña: {contraseña}")
    adjuntar_a_archivo("usuarios.txt", "-" * 40) # Separador

    print("Tu registro ha sido guardado exitosamente.")


def iniciar_sesion():
    print("---------------Iniciar Sesión--------------------")

    max_intentos = 3
    intentos = 0

    while intentos < max_intentos:
        usuario_login = input("Ingrese su correo: ")
        contraseña_login = input("Ingrese su contraseña: ")

        if usuario_login == "admin@ninjas.com" and contraseña_login == "Admin123":
            print("Inicio de sesión de ADMINISTRADOR exitoso.")
            mostrar_menu_administrador() 
            return True 
        
        usuario_encontrado = False
        lineas = leer_archivo_lineas("usuarios.txt")
        
        for i in range(0, len(lineas), 6):
            try:
                correo_guardado = lineas[i + 3].strip().split(": ")[1]
                contraseña_guardada = lineas[i + 4].strip().split(": ")[1]

                if correo_guardado == usuario_login and contraseña_guardada == contraseña_login:
                    print(f"Inicio de sesión exitoso. ¡Bienvenido, {lineas[i].strip().split(': ')[1]}!")
                    return usuario_login 
            except (IndexError, AttributeError):
                continue

        print("Usuario o contraseña incorrectos.")
        intentos += 1
        if intentos < max_intentos:
            print(f"Le quedan {max_intentos - intentos} intentos.")
        
    print("Ha excedido el número de intentos. Volviendo al menú principal.")
    return None 

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
        "fuerza": fuerza,
        "agilidad": agilidad,
        "resistencia": resistencia,
        "estilo": estilo,
        "puntos": puntos
    }
    
    ninjas.append(nuevo_ninja)
    guardar_ninjas_en_archivo(ninjas, "ninjas.txt") 

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

        if opcion in ['1', '2', '3']:
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
        
        guardar_ninjas_en_archivo(ninjas, "ninjas.txt")
    else:
        print(f"❌ Ninja '{nombre_buscar}' no encontrado.")


def eliminar_ninjas():
    print("\n--- Eliminar Ninjas ---")
    ninjas = cargar_ninjas_desde_archivo()
    if not ninjas:
        print("No hay ninjas registrados para eliminar.")
        return

    nombre_eliminar = input("Ingrese el nombre del ninja a eliminar: ").strip()
    ninja_encontrado = None
    indice_a_eliminar = -1

    for i, ninja in enumerate(ninjas):
        if ninja['nombre'].lower() == nombre_eliminar.lower():
            ninja_encontrado = ninja
            indice_a_eliminar = i
            break

    if ninja_encontrado:
        confirmar = input(f"¿Está seguro que desea eliminar a '{ninja_encontrado['nombre']}'? (s/n): ").lower()
        if confirmar == 's':
            ninjas.pop(indice_a_eliminar)
            guardar_ninjas_en_archivo(ninjas, "ninjas.txt") # Guardar la lista actualizada
            print(f"✅ Ninja '{ninja_encontrado['nombre']}' eliminado exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print(f"❌ Ninja '{nombre_eliminar}' no encontrado.")


def crear_arbol_habilidades_para_ninja(ninja_nombre=None):
    """Permite al administrador crear/modificar el árbol de habilidades para un ninja."""
    print("\n--- Crear/Modificar Árbol de Habilidades de Ninja ---")
    
    ninjas = cargar_ninjas_desde_archivo()
    if not ninjas:
        print("No hay ninjas registrados. Agregue ninjas primero.")
        return

    if ninja_nombre is None:
        print("Ninjas disponibles:")
        for ninja in ninjas:
            print(f"- {ninja['nombre']}")
        ninja_nombre = input("Ingrese el nombre del ninja para el que desea crear/modificar el árbol: ").strip()

    ninja_obj = buscar_ninja_lineal(ninjas, ninja_nombre, "nombre")
    if not ninja_obj:
        print(f"❌ Ninja '{ninja_nombre}' no encontrado.")
        return
    
    arbol_actual = cargar_arbol_habilidades_ninja(ninja_nombre)
    if arbol_actual:
        print(f"\nÁrbol de habilidades actual para {ninja_nombre}:")
        arbol_actual.mostrar()
        modificar = input("¿Desea modificar este árbol? (s/n): ").lower()
        if modificar != 's':
            return 


    habilidades_para_arbol = []
    if arbol_actual:
      
        habilidades_para_arbol = arbol_actual.obtener_habilidades_en_lista_iterativo()

    print("\nIngrese las habilidades y sus puntos (ej: 'Rasengan,5').")
    print("Escriba 'fin' para terminar.")
    
    while True:
        entrada = input("Habilidad y puntos: ").strip()
        if entrada.lower() == 'fin':
            break
        
        partes = entrada.split(",")
        if len(partes) == 2:
            nombre_habilidad = partes[0].strip()
            try:
                puntos_habilidad = int(partes[1].strip())
                if puntos_habilidad > 0:
                 
                    encontrado = False
                    for i, (nombre, puntos) in enumerate(habilidades_para_arbol):
                        if nombre.lower() == nombre_habilidad.lower():
                            habilidades_para_arbol[i] = (nombre_habilidad, puntos_habilidad)
                            encontrado = True
                            print(f"Habilidad '{nombre_habilidad}' actualizada.")
                            break
                    if not encontrado:
                        habilidades_para_arbol.append((nombre_habilidad, puntos_habilidad))
                        print(f"Habilidad '{nombre_habilidad}' agregada.")
                else:
                    print("Los puntos deben ser un número positivo.")
            except ValueError:
                print("Puntos inválidos. Asegúrese de que sea un número entero.")
        else:
            print("Formato incorrecto. Use 'NombreHabilidad,Puntos'.")
    
    if habilidades_para_arbol:
        nuevo_arbol = ArbolHabilidades(habilidades_para_arbol)
        guardar_arbol_habilidades_ninja(ninja_nombre, nuevo_arbol)
        print(f"✅ Árbol de habilidades para '{ninja_nombre}' creado/actualizado exitosamente.")
    else:
        print("No se agregaron habilidades. Árbol no guardado.")


def mostrar_menu_administrador():
    """Menú principal para el administrador."""
    print("Bienvenido al menú de administrador.")
    while True:
        print("\n--- Menú de Administrador ---")
        print("1. Agregar nuevos ninjas")
        print("2. Listar ninjas (y ordenar)")
        print("3. Consultar un ninja por nombre o estilo")
        print("4. Actualizar atributos de un ninja")
        print("5. Eliminar ninjas")
        print("6. Crear/Modificar Árbol de Habilidades de Ninja")
        print("7. Salir del menú de administrador")
        
        opcion = input("Ingrese el número de la opción: ").strip()

        if opcion == "1":
            agregar_ninja()
        elif opcion == "2":
            listar_ninjas_admin()
        elif opcion == "3":
            consultar_ninja()
        elif opcion == "4":
            actualizar_atributos_ninja()
        elif opcion == "5":
            eliminar_ninjas()
        elif opcion == "6":
            crear_arbol_habilidades_para_ninja()
        elif opcion == "7":
            print("Saliendo del menú de administrador.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_jugador_logged_in(user_email):
    """Menú para un usuario (jugador) que ha iniciado sesión."""
    victorias, derrotas = cargar_progreso_jugador(user_email)
    print(f"\n¡Bienvenido, jugador! (Email: {user_email})")
    print(f"Tu progreso actual: Victorias: {victorias}, Derrotas: {derrotas}")
    
    while True:
        print("\n--- Menú de Jugador ---")
        print("1. Simular combate 1 vs 1")
        print("2. Mostrar ranking de combates (general)")
        print("3. Iniciar Torneo Chunin")
        print("4. Ver tu árbol de habilidades (si existe)")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ninjas = cargar_ninjas_desde_archivo()
            if len(ninjas) < 2:
                print("Se necesitan al menos dos ninjas para un combate 1 vs 1.")
                continue
            
            print("\nNinjas disponibles para el combate:")
            for i, ninja in enumerate(ninjas):
                print(f"{i+1}. {ninja['nombre']}")
            
            while True:
                try:
                    idx1 = int(input("Seleccione el número del primer ninja: ")) - 1
                    idx2 = int(input("Seleccione el número del segundo ninja: ")) - 1
                    
                    if not (0 <= idx1 < len(ninjas) and 0 <= idx2 < len(ninjas)):
                        print("Selección de ninja inválida. Intente de nuevo.")
                        continue
                    if idx1 == idx2:
                        print("No puedes seleccionar el mismo ninja para ambos lados. Intente de nuevo.")
                        continue
                    
                    ninja_a_combat = ninjas[idx1]
                    ninja_b_combat = ninjas[idx2]
                    
                    resultado, ganador = simular_combate(ninja_a_combat, ninja_b_combat)
                    
                    # Actualizar puntos del ganador en el archivo de ninjas
                    ninjas_actualizados = cargar_ninjas_desde_archivo() # Recargar para asegurar la lista más reciente
                    for n in ninjas_actualizados:
                        if n['nombre'] == ganador:
                            n['puntos'] += 1
                            break
                    guardar_ninjas_en_archivo(ninjas_actualizados) # Guardar los cambios
                    
                    if ganador == ninja_a_combat['nombre']:
                        victorias += 1
                    else:
                        derrotas += 1
                    guardar_progreso_jugador(user_email, victorias, derrotas)
                    print(f"Tu progreso actualizado: Victorias: {victorias}, Derrotas: {derrotas}")
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")

        elif opcion == "2":
            mostrar_ranking_combates()

        elif opcion == "3":
            ninjas_para_torneo = cargar_ninjas_desde_archivo()
            if len(ninjas_para_torneo) < 16:
                print(f"Se necesitan al menos 16 ninjas para el torneo. Actualmente hay {len(ninjas_para_torneo)}. Por favor, agregue más ninjas.")
            else:
                print("¡Iniciando Torneo Chunin!")
                campeon = torneo(ninjas_para_torneo) 
                if campeon:
                    
                    guardar_ninjas_en_archivo(ninjas_para_torneo) 
                    print(f"El campeón del torneo es: {campeon}")
      

        elif opcion == "4":
            ninjas_usuario = cargar_ninjas_desde_archivo()
            print("\nSelecciona un ninja para ver su árbol de habilidades:")
            for i, ninja in enumerate(ninjas_usuario):
                print(f"{i+1}. {ninja['nombre']}")
            
            try:
                idx_ninja = int(input("Ingrese el número del ninja: ")) - 1
                if 0 <= idx_ninja < len(ninjas_usuario):
                    ninja_seleccionado = ninjas_usuario[idx_ninja]
                    arbol = cargar_arbol_habilidades_ninja(ninja_seleccionado['nombre'])
                    if arbol:
                        print(f"\n--- Árbol de Habilidades de {ninja_seleccionado['nombre']} ---")
                        arbol.mostrar()
                    else:
                        print(f"No se encontró un árbol de habilidades para {ninja_seleccionado['nombre']}.")
                        crear_ahora = input("¿Desea crear uno ahora? (s/n): ").lower()
                        if crear_ahora == 's':
                            crear_arbol_habilidades_para_ninja(ninja_seleccionado['nombre'])
                else:
                    print("Selección de ninja inválida.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

        elif opcion == "5":
            print("Cerrando sesión. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def menu_inicio():
    """Menú principal de la aplicación."""
    print("========================================")
    print("  Bienvenido al Torneo Chunin de Ninjas")
    print("========================================")

    # Inicializar ninjas si el archivo no existe
    if not leer_archivo_lineas("ninjas.txt"):
        print("Creando ninjas iniciales...")
        guardar_ninjas_en_archivo(ninjas_iniciales_data, "ninjas.txt")
        print("Ninjas iniciales creados.")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        
        opcion = input("Ingrese el número de la opción: ").strip()

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            user_logged_in = iniciar_sesion() 
            
            if user_logged_in and user_logged_in is not True: 
                menu_jugador_logged_in(user_logged_in)

        elif opcion == "3":
            print("Saliendo de la aplicación. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_inicio()
