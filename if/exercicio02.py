"""
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento, se o salário for superior a R$ 1350,00 o percentual de aumento será de 10%, 
caso o valor seja inferior percentual de aumento será de 15%.
"""

nome = str(input("Digite seu nome: "))
salario = float(input("Insira o seu salário: "))


if salario > 1350:
    porcentagem = 0.1
    aumento = salario * porcentagem
    ajuste = salario + aumento
    print(
        f"\nO ajuste será de R${aumento:.2f}"
        f"\nSeu salario atual será de R${ajuste:.2f}\n"
        )
else:
    porcentagem = 0.15
    aumento = salario * porcentagem
    ajuste = salario + aumento
    print(
        f"\nO ajuste será de R${aumento:.2f}"
        f"\nSeu salario atual será de R${ajuste:.2f}\n"
        )