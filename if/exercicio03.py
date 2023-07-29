"""
Escreva um programa que pergunte a distância que o passageiro deseja percorrer em km. 
Calcule o preço da passagem cobrando R$ 0,50 por km para viagens até 200 km e R$ 0,45 para viagens acima de 200 km.
"""

distancia = float(input("Qual a deistacia que será percorrida?: "))
passagem = 0

if distancia <= 200:
    passagem = 0.5 * distancia
    print(f'O valor da passagem é: R${passagem:.2f}')
else:
    passagem = 0.45 * distancia
    print(f'O valor da passagem é: R${passagem:.2f}')

