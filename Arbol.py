import ramdom 

class NodoHabilidad:
  def __init__(self,nombre,puntos):
    self.nombre = nombre
    self.puntos = puntos
    self.izquierda= None
    self.derecha = None

class ArbolHabilidades:
  def __init__(self,habilidades=None):
    self.raiz=None
    if habilidades:
      for nombre.puntos in habilidades:
        self.insert(nombre,puntos)

  def insertar(self,nombre,puntos):
    nuevo=NodoHabilidad(nombre,puntos)
    if self.raiz is None:
      self.raiz=nuevo
    else:
      self._insertar_recursivo(self.raiz,nuevo)

  def _insertar_recursivo(self,actual,nuevo):
    if nuevo.puntos <= actual.puntos:
      if actual.izquierda is None:
        actual.izquierda = nuevo
      else:
        if actual.derecha is None:
          actual.derecha=nuevo
        else:
          self._insertar_recursivo(actual.derecha,nuevo)
  
  def sumar_puntos(self):
    return self._sumar_recursivo(self.raiz)

  def _sumar_recursivo(self,nodo):
    if nodo is None:
      return 0
    return nodo.puntos + self._sumar_recursivo(nodo.izquierda)+self._sumar_recursivo(nodo.derecha)
    
    
  def mostrar(self,nodo=None,nivel=0,lado ="Raiz"):
    if nivel==0 and nodo is None:
      nodo = self.raiz
    if nodo is None:  
      return
    print(" " *(nivel *4)+f"´{nodo.nombre} ({nodo.puntos})") 
    self.mostrar(nodo.izquierdo,nivel +1)
    self.mostrar(nodo.derecho,nivel+1)

  def buscar_por_nombre(self,nombre,nodo=None):
    if nodo is None:
      nodo = self.raiz
    if nodo is None:
      return None
    if nodo.nombre== nombre:
      return nodo

    encontrado=self.buscar_por_nombre(nombre,nodo.izquierda)
    if encontrado:
      return encontrado
    return self._buscar_por_nombre(nombre,nodo.derecho)

  def genarar_arbol():
    hanilidades= [
      
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
    seleccionados=ramdom.sample(habilidades,5)
    arbol=ArbolHabilidades(seleccionados)
    return arbol

   if __name__ == "__main__":
    arbol = generar_arbol_habilidades()
    print("Árbol de habilidades generado:")
    arbol.mostrar()

    print(f"\nSuma total de puntos: {arbol.sumar_puntos()}")

    nombre_a_buscar = "Susanoo"
    resultado = arbol.buscar_por_nombre(nombre_a_buscar)
    if resultado:
        print(f"\nHabilidad encontrada: {resultado.nombre} con {resultado.puntos} puntos")
    else:
        print(f"\nHabilidad '{nombre_a_buscar}' no encontrada en el árbol.")


    







  


