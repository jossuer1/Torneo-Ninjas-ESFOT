import random

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