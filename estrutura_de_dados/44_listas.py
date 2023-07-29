"""
Exemplo do uso de listas com python
"""
numeros = [20 ,50, 78, 3, 2]
print(f"1-Valores: {numeros}")
"""
print(f"A lista tem {len(numeros)} elementos.") # Consulta de quantos elementos
print(f"O elemento na posição 2 é o numero {numeros[2]}") #Print de um elemento da lista
"""
elementos = [29, "Centro", True, 6.9]

# Alteração de elementos
# Alterando valor através da posição
numeros[1] = 1000
print(f"2-Valores: {numeros}")

# Add elementos
# Alterando valor através da posição
numeros.append(890)
print(f"3-Valores: {numeros}")

numeros.insert(2,51)
print(f"4-Valores: {numeros}")

#Remove elementos
# Remover item da lista pela posição
del numeros[2]
print(f"5-Valores: {numeros}")
# Remover item da lista pelo conteudo
numeros.remove(2)
print(f"6-Valores: {numeros}")



