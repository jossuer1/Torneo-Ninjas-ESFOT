#Arbol de Habilidades
class NodoHabilidad:
  def __init__(self,nombre,puntos):
    self.nombre = nombre
    self.puntos = puntos
    self.izquierda= None
    self.derecha = None

def sumar_puntos(nodo):
  if nodo is None:
    return 0
  return nodo.puntos +sumar_puntos(nodo.izquierda)+sumar_puntos(nodo.derecha)

raiz=NodoHabilidad("Ataque Rapido",2)
raiz.izquierda=NodoHabilidad("Defensa Fuerte",3)
raiz.derecha=NodoHabilidad("Agilidad Extrema",1)

print("Suma total de puntos: "sumar_puntos(raiz))
