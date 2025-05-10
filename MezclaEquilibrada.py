def dividir_en_archivos(lista):
    archivo1 = []
    archivo2 = []
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
        fusion = intercalar(archivo1[i], archivo2[j])
        resultado.append(fusion)
        i += 1
        j += 1
    resultado.extend(archivo1[i:])
    resultado.extend(archivo2[j:])
    return resultado

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

def mezcla_equilibrada(lista):
    while True:
        archivo1, archivo2 = dividir_en_archivos(lista)
        lista = fusionar_archivos(archivo1, archivo2)
        if len(lista) == 1:
            return lista[0]

n = int(input("Ingrese la cantidad de elementos para ordenar: "))
lista = [int(input(f"Elemento {i+1}: ")) for i in range(n)]

ordenada = mezcla_equilibrada(lista)
print("Resultado de mezcla equilibrada:", ordenada)
