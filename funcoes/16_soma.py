"""
Exemplo de soma com uso de funções
"""
def soma(numero1, numero2): 
    total = numero1 + numero2
    return total

n1 = int(input("Insira o numero 1: "))
n2 = int(input("Insira o numero 2: "))
resultado = soma(n1,n2)
print(f"O resultado é {resultado}")