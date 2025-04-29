def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    entrada = input("Introduce los números que quieres ordenar separados por espacios: ")
    datos = list(map(int, entrada.split()))

    print("\nLista original:")
    print(datos)

    insertion_sort(datos)

    print("\nLista ordenada:")
    print(datos)

if __name__ == "__main__":
    main()
