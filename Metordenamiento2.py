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
    else:
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

def get_numbers():
    cantidad = int(input("Ingrese la cantidad de números: "))
    numeros = []
    for i in range(cantidad):
        num = int(input(f"Ingrese el número {i + 1}: "))
        numeros.append(num)
    return numeros

def menu():
    while True:
        print("\nMenú de Métodos de Ordenamiento")
        print("1. Shell Sort")
        print("2. Quick Sort")
        print("3. Heap Sort")
        print("4. Radix Sort")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            datos = get_numbers()
            print("Ordenado:", shell_sort(datos.copy()))
        elif opcion == "2":
            datos = get_numbers()
            print("Ordenado:", quick_sort(datos.copy()))
        elif opcion == "3":
            datos = get_numbers()
            print("Ordenado:", heap_sort(datos.copy()))
        elif opcion == "4":
            datos = get_numbers()
            print("Ordenado:", radix_sort(datos.copy()))
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
