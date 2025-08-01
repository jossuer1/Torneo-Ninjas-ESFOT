import random

# ---------- Clase Nodo ----------
class NodoHabilidad:
    def __init__(self, nombre, puntos):
        self.nombre = nombre            # Nombre de la técnica (ej: Rasengan)
        self.puntos = puntos            # Puntos de poder de la técnica
        self.izquierda = None           # Habilidad menor
        self.derecha = None             # Habilidad mayor

# ---------- Clase Árbol de Habilidades ----------
class ArbolHabilidades: #Se encarga de insertar las habilidades en el arbol 
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

    # ---------- Recorridos que suman puntos ----------
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

    # ---------- Mostrar árbol ----------
    def mostrar(self, nodo=None, nivel=0, lado="Raíz"):
        if nivel == 0 and nodo is None:
            nodo = self.raiz
        if nodo is None:
            return
        print(" " * (nivel * 4) + f"{lado}: {nodo.nombre} ({nodo.puntos})")
        self.mostrar(nodo.izquierda, nivel + 1, "Izq")
        self.mostrar(nodo.derecha, nivel + 1, "Der")

    # ---------- Buscar por nombre (opcional) ----------
    def buscar_por_nombre(self, nombre, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo is None:
            return None
        if nodo.nombre == nombre:
            return nodo
        encontrado = self.buscar_por_nombre(nombre, nodo.izquierda)
        if encontrado:
            return encontrado
        return self.buscar_por_nombre(nombre, nodo.derecha)

# ---------- Generar árbol con 5 técnicas aleatorias ----------
def generar_arbol_habilidades():
    habilidades = [
        ("Rasengan", 5),
        ("Chidori", 5),
        ("Jutsu Clon de Sombra", 3),
        ("Amaterasu", 6),
        ("Susanoo", 7),
        ("Byakugan", 4),
        ("Modo Sabio", 6),
        ("Katon: Bola de Fuego", 3),
        ("Taijutsu", 2),
        ("Kirin", 5),
        ("Kagemane no Jutsu", 4),
        ("Arena de Gaara", 4),
        ("Invocación: Gamabunta", 6),
        ("Genjutsu: Tsukuyomi", 7),
        ("Elemento Madera", 6)
    ]
    seleccionados = random.sample(habilidades, 5)
    arbol = ArbolHabilidades(seleccionados)
    return arbol







  


