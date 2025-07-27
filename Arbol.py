#Arbol de Habilidades
class NodoHabilidad:
  def __init__(self,nombre,puntos):
    self.nombre = nombre
    self.puntos = puntos
    self.izquierda= None
    self.derecha = None

class ArbolHabilidades:
  def __init__(self):
    self.raiz=None

  def Manual(self):
  "Arbol con tres habilidades fijas"
  self.raiz=NodoHabilidad("Ataque Rapido",2)
  self.raiz.izquierdo=NodoHabilidad("Defensa fuerte",3)
  self.raiz.derecha=NodoHabilidad("Agilidad Extrema",1)
  
  def sumar_puntos(nodo):
  if nodo is None:
    return 0
  return nodo.puntos +sumar_puntos(nodo.izquierda)+sumar_puntos(nodo.derecha)

  def mostrar(self,nodo=None,nivel=0):
    if nivel==0 and nodo is None:
      nodo = self.raiz
    if nodo is None:  
      return
   
  print(" " *(nivel *4)+f"´{nodo.nombre} ({nodo.puntos})")
  self.mostrar(nodo.izquierdo,nivel +1)
  self.mostrar(nodo.derecho,nivel+1)

arbol=ArbolHabilidades()
arbol.Manual()

print("Arbol de habilidades")
arbol.mostrar()

print("\nTotal de puntos:",arbol.sumar_puntos())

  


