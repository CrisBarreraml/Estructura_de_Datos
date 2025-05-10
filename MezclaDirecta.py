def mezcla_directa(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = mezcla_directa(lista[:medio])
    derecha = mezcla_directa(lista[medio:])

    return intercalar(izquierda, derecha)

def intercalar(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1

    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

n = int(input("Ingrese la cantidad de elementos para ordenar: "))
lista = [int(input(f"Elemento {i+1}: ")) for i in range(n)]

ordenada = mezcla_directa(lista)
print("Resultado de mezcla directa:", ordenada)
