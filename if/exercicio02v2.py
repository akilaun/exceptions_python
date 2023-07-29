"""
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento, se o salário for superior a R$ 1350,00 o percentual de aumento será de 10%, 
caso o valor seja inferior percentual de aumento será de 15%.
"""

def calculo_salario(salario):
    porcentagem = 0
    if salario > 1350:
        porcentagem = 0.1
    else: 
        porcentagem = 0.15

    aumento = salario * porcentagem
    ajuste = salario + aumento
    return ajuste

nome = str(input("Digite seu nome: "))
salario = float(input("Insira o seu salário: "))
novo_salario = calculo_salario(salario)
diferenca = novo_salario - salario

print(
    f"\nO ajuste será de R${diferenca:.2f}"
    f"\nSeu salario atual será de R${novo_salario:.2f}\n"
    )