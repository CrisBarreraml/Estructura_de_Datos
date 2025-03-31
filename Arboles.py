class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
    
    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo, valor):
        if nodo is None or nodo.valor == valor:
            return nodo is not None
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        return self._buscar_recursivo(nodo.derecha, valor)
    
    def inorden(self):
        return self._inorden_recursivo(self.raiz)
    
    def _inorden_recursivo(self, nodo):
        if nodo is None:
            return []
        return self._inorden_recursivo(nodo.izquierda) + [nodo.valor] + self._inorden_recursivo(nodo.derecha)
    
    def preorden(self):
        return self._preorden_recursivo(self.raiz)
    
    def _preorden_recursivo(self, nodo):
        if nodo is None:
            return []
        return [nodo.valor] + self._preorden_recursivo(nodo.izquierda) + self._preorden_recursivo(nodo.derecha)
    
    def postorden(self):
        return self._postorden_recursivo(self.raiz)
    
    def _postorden_recursivo(self, nodo):
        if nodo is None:
            return []
        return self._postorden_recursivo(nodo.izquierda) + self._postorden_recursivo(nodo.derecha) + [nodo.valor]

arbol = Arbol()
while True:
    print("\nMenú:")
    print("1. Insertar un valor")
    print("2. Buscar un valor")
    print("3. Mostrar recorrido Inorden")
    print("4. Mostrar recorrido Preorden")
    print("5. Mostrar recorrido Postorden")
    print("6. Salir")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        valor = int(input("Ingresa el valor a insertar: "))
        arbol.insertar(valor)
        print(f"Valor {valor} insertado.")
    elif opcion == "2":
        valor = int(input("Ingresa el valor a buscar: "))
        encontrado = arbol.buscar(valor)
        print(f"El valor {valor} {'se encuentra' if encontrado else 'no se encuentra'} en el árbol.")
    elif opcion == "3":
        print("Recorrido Inorden:", arbol.inorden())
    elif opcion == "4":
        print("Recorrido Preorden:", arbol.preorden())
    elif opcion == "5":
        print("Recorrido Postorden:", arbol.postorden())
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
