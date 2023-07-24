"""
Você precisa alugar um carro e a empresa está com duas promoções conforme as tabelas abaixo:

----------Promoção por diária------------
PERIODO                 VALOR_DIARIA      
De 2 até 5 dias       R$ 105,00
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

nome = input("Qual seu nome: ")
dias = int(input("Insira o total de dias: "))
km = int(input("Insira o total de km a ser rodado: "))

total_km = calculos.calcular_kilometro(km)
total_diaria = calculos.calcular_valor_por_diarias(dias)

if total_km < total_diaria:
    print("KM")
if total_diaria < total_km:
    print("DIARIA")
