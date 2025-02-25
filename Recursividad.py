def contar_digitos(n):
    if n == 0:
        return 0
    return 1 + contar_digitos(n // 10)

numero = int(input("Ingresa un número entero positivo: "))
if numero < 0:
    print("Por favor, ingresa un número positivo.")
else:
    print(f"El número {numero} tiene {contar_digitos(numero)} dígitos.")

