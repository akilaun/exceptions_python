"""
Imprimir os números pares de 1 a 100
"""

contador = 0

while contador <= 100:
    if (contador % 2) == 0: # Operador modulo % verifica se o resto da divisão é igual a 0
        print(f"O número {contador} é par.")
    else:
        print(f"O número {contador} é impar.")

    contador += 1