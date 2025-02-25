def contar_digitos(n):
    contador = 0
    while n > 0:
        n //= 10  
        contador += 1
    return contador

numero = int(input("Ingresa un número entero positivo: "))
if numero < 0:
    print("Por favor, ingresa un número positivo.")
else:
    print(f"El número {numero} tiene {contar_digitos(numero)} dígitos.")
