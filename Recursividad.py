def invertir_cadena(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + invertir_cadena(s[:-1])

cadena = input("Ingresa una cadena: ")
cadena_invertida = invertir_cadena(cadena)
print(f"Cadena invertida: {cadena_invertida}")

