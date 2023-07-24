"""
Tentativa de passar raiva!

Você precisa alugar um carro e a empresa está com duas promoções conforme as tabelas abaixo:

----------Promoção por diária------------
PERIODO                 VALOR_DIARIA      
De 2 até 5 dias      R$ 105,00
De 6 até 15 dias     R$ 95,00
De 16 até 25 dias    R$ 70,00
Acima de 25 dias     R$ 60,00

-------Promoção por kilometragem---------
KM RODADO            VALOR POR KM
De 100 até 1000      R$ 6,99
De 1001 até 4000     R$ 4,99
De 4001 até 6000     R$ 3,99
Acima de 6000        R$ 2,99

A empresa vai oferecer simulação dos dois planos e com base na inteligência artificial do nosso algoritmo será mostrado para o usuário
a seguinte mensagem ao final:

Com base na simulação realizada segue as informações:
------Plano por diária------
Total dias ?, valor gasto ?

------Plano por kilometragem------
Total kilometros ?, valor gasto ?

Recomendamos usar o plano por ? :)
"""

import calculos

nome = str(input("Digite o seu nome: "))
km = float(input("Insira a distancia em km: "))
dia = int(input("insira o total de dias que usará o carro: "))

total_km = calculos.aluguel_por_kilometro(km)
total_dias = calculos.aluguel_por_dia(dia)
diferenca_km = total_dias - total_km
diferenca_dias = total_km - total_dias


if total_km < total_dias:
    print(
        f"Olá {nome}, espero que você esteja bem."
        "\nA melhor opção é o aluguel por Kilometros!"
        f"\nTotal a ser gasto: R${total_km:.2f}, uma economia de R${diferenca_km:.2f}."
        f"\nPor dia ficaria: R${total_dias:.2f}."
          )
else:
    print(
        f"Olá {nome}, espero que você esteja bem."
        "\nA melhor opção é o aluguel por dias rodados!"
        f"\nTotal a ser gasto: R${total_dias:.2f}, uma diferença de R${diferenca_dias:.2f}."
        f"\nPor km ficaria: R${total_km:.2f}."
          )
