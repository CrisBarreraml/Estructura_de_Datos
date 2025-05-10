def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    menores = [x for x in arr[1:] if x <= pivot]
    mayores = [x for x in arr[1:] if x > pivot]
    return quick_sort(menores) + [pivot] + quick_sort(mayores)

def heapify(arr, n, i):
    largest = i
    izq = 2 * i + 1
    der = 2 * i + 2

    if izq < n and arr[izq] > arr[largest]:
        largest = izq
    if der < n and arr[der] > arr[largest]:
        largest = der

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in arr:
        index = i // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr


def intercalacion(lista1, lista2):
    resultado = []
    i = j = 0
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    resultado.extend(lista1[i:])
    resultado.extend(lista2[j:])
    return resultado


def mezcla_directa(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = mezcla_directa(lista[:medio])
    derecha = mezcla_directa(lista[medio:])
    return intercalacion(izquierda, derecha)


def dividir_en_archivos(lista):
    archivo1, archivo2 = [], []
    toggle = True
    for i in range(0, len(lista), 2):
        sublista = sorted(lista[i:i+2])
        if toggle:
            archivo1.append(sublista)
        else:
            archivo2.append(sublista)
        toggle = not toggle
    return archivo1, archivo2

def fusionar_archivos(archivo1, archivo2):
    resultado = []
    i = j = 0
    while i < len(archivo1) and j < len(archivo2):
        resultado.append(intercalacion(archivo1[i], archivo2[j]))
        i += 1
        j += 1
    resultado.extend(archivo1[i:])
    resultado.extend(archivo2[j:])
    return resultado

def mezcla_equilibrada(lista):
    while True:
        archivo1, archivo2 = dividir_en_archivos(lista)
        lista = fusionar_archivos(archivo1, archivo2)
        if len(lista) == 1:
            return lista[0]


def leer_lista(mensaje):
    n = int(input(f"{mensaje} ¿Cuántos números? "))
    return [int(input(f"Elemento {i+1}: ")) for i in range(n)]


def menu():
    while True:
        print("\n=== MENÚ DE ORDENAMIENTOS ===")
        print("1. Shell Sort")
        print("2. Quick Sort")
        print("3. Heap Sort")
        print("4. Radix Sort")
        print("5. Intercalación")
        print("6. Mezcla Directa")
        print("7. Mezcla Equilibrada")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            datos = leer_lista("Shell Sort")
            print("Ordenado:", shell_sort(datos.copy()))
        elif opcion == "2":
            datos = leer_lista("Quick Sort")
            print("Ordenado:", quick_sort(datos.copy()))
        elif opcion == "3":
            datos = leer_lista("Heap Sort")
            print("Ordenado:", heap_sort(datos.copy()))
        elif opcion == "4":
            datos = leer_lista("Radix Sort")
            print("Ordenado:", radix_sort(datos.copy()))
        elif opcion == "5":
            print("Intercalación - Lista 1")
            lista1 = sorted(leer_lista("Lista 1"))
            print("Intercalación - Lista 2")
            lista2 = sorted(leer_lista("Lista 2"))
            print("Resultado:", intercalacion(lista1, lista2))
        elif opcion == "6":
            datos = leer_lista("Mezcla Directa")
            print("Ordenado:", mezcla_directa(datos.copy()))
        elif opcion == "7":
            datos = leer_lista("Mezcla Equilibrada")
            print("Ordenado:", mezcla_equilibrada(datos.copy()))
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
