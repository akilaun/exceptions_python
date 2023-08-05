"""
Imprimir os numeros pares de 1 até 100, mas deve contar a quantidade de numeros e quando chegar em 10 unidades, parar.
"""

contador = 1
unidades = 1
lista_pares = []

while contador <= 100:
    if (contador % 2) == 0: # Operador modulo % verifica se o resto da divisão é igual a 0
        print(f"O número {contador} é par. \nUnidade = {unidades}.")
        unidades += 1
        lista_pares.append(contador)

    if unidades == 11:
        break

    contador += 1
print(f"A quantidade de numeros pares é {len(lista_pares)}") #Conta quantas vezes os numeros pares foram retornados