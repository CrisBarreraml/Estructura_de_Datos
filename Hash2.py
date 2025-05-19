def contar_palabras(texto):
    palabras = texto.lower().split()
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

def main():
    print("📊 Contador de palabras en texto (usa dict/hash)")

    texto = input("Ingresa un texto: ")

    resultado = contar_palabras(texto)

    print("\nFrecuencia de palabras:")
    for palabra, frecuencia in resultado.items():
        print(f"{palabra}: {frecuencia}")

if __name__ == "__main__":
    main()
