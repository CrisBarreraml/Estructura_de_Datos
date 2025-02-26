from collections import deque

array = [1, 2, 3, 4, 5]
array.append(6)  
array.pop()        
print("Array:", array)

pila = []
pila.append(10)  
pila.append(20)
pila.append(30)
print("Pila antes de pop:", pila)
pila.pop()  
print("Pila después de pop:", pila)

cola = deque()
cola.append(100)  
cola.append(200)
cola.append(300)
print("Cola antes de dequeue:", cola)
cola.popleft()  
print("Cola después de dequeue:", cola)

class ColaCircular:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Cola circular llena")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Cola circular vacía")
            return
        removed = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return removed

    def display(self):
        if self.front == -1:
            print("Cola circular vacía")
            return
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()

cola_circular = ColaCircular(5)
cola_circular.enqueue(1)
cola_circular.enqueue(2)
cola_circular.enqueue(3)
print("Cola circular después de inserciones:")
cola_circular.display()
cola_circular.dequeue()
print("Cola circular después de una eliminación:")
cola_circular.display()

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def insertar(self, data):
        nuevo_nodo = Nodo(data)
        if not self.head:
            self.head = nuevo_nodo
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = nuevo_nodo

    def mostrar(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

lista = ListaEnlazada()
lista.insertar(5)
lista.insertar(10)
lista.insertar(15)
print("Lista enlazada:")
lista.mostrar()
