def calcula_viagem(km, valor, media):
    qtde_litros = km / media
    total = qtde_litros * valor
    return total

def aluguel_por_dia(dias):
    valor_diaria = 0.0
    total_por_dia = dias * valor_diaria
    if dias >= 2 and dias <= 5:
        valor_diaria = 105.00
    if dias > 5 and dias <= 15:
        valor_diaria = 95.00
    if dias > 15 and dias <= 25:
        valor_diaria = 70.00
    if dias > 25:
        valor_diaria = 60.00
    return total_por_dia

def aluguel_por_kilometro(kilometros):
    valor_por_km = 0.0
    total_por_km = kilometros * valor_por_km
    if kilometros >= 100 and kilometros <= 1000:
        valor_por_km = 6.99
    if kilometros > 1000 and kilometros <= 4000:
        valor_por_km = 4.99
    if kilometros > 4000 and kilometros <= 6000:
        valor_por_km = 3.99
    if kilometros > 6000:
        valor_por_km = 2.99
    return total_por_km



def aumento_salarial(salario_atual):
    porcentagem = 0.0
    ajuste = salario_atual * porcentagem
    salario_novo = salario_atual + ajuste
    if salario_atual > 1350:
        porcentagem = 0.1
    else:
        porcentagem = 0.15
    return salario_novo