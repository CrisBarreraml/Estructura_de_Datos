def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def main():
    entrada = input("Introduce los números que quieres ordenar separados por espacios: ")
    datos = list(map(int, entrada.split()))

    print("\nLista original:")
    print(datos)

    selection_sort(datos)

    print("\nLista ordenada:")
    print(datos)

if __name__ == "__main__":
    main()
