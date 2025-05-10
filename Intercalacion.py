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

n1 = int(input("Ingrese la cantidad de elementos de la primera lista ordenada: "))
lista1 = [int(input(f"Elemento {i+1}: ")) for i in range(n1)]

n2 = int(input("Ingrese la cantidad de elementos de la segunda lista ordenada: "))
lista2 = [int(input(f"Elemento {i+1}: ")) for i in range(n2)]

lista1.sort()
lista2.sort()

resultado = intercalacion(lista1, lista2)
print("Resultado de intercalación:", resultado)
