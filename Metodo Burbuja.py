def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    entrada = input("Introduce los números que quieres ordenar separados por espacios: ")
    datos = list(map(int, entrada.split()))

    print("\nLista original:")
    print(datos)

    bubble_sort(datos)

    print("\nLista ordenada:")
    print(datos)

if __name__ == "__main__":
    main()
