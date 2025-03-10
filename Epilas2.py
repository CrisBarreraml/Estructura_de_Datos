class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.items = []
    
    def push(self, item):
        if self.size() < self.capacidad:
            self.items.append(item)
        else:
            print("Pila llena, no se puede agregar más elementos.")
    
    def pop(self):
        return self.items.pop() if not self.is_empty() else None
    
    def peek(self):
        return self.items[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Programa principal
capacidad = int(input("Ingrese el tamaño de la pila: "))
pila = Pila(capacidad)

while True:
    print("\nOpciones:")
    print("1. Agregar elemento a la pila")
    print("2. Eliminar elemento de la pila")
    print("3. Ver el elemento en la cima")
    print("4. Ver el tamaño de la pila")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        elemento = input("Ingrese el elemento a agregar: ")
        pila.push(elemento)
    elif opcion == "2":
        eliminado = pila.pop()
        if eliminado:
            print(f"Elemento eliminado: {eliminado}")
        else:
            print("La pila está vacía.")
    elif opcion == "3":
        cima = pila.peek()
        if cima:
            print(f"Elemento en la cima: {cima}")
        else:
            print("La pila está vacía.")
    elif opcion == "4":
        print(f"Tamaño actual de la pila: {pila.size()} de {capacidad}")
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

