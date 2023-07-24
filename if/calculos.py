def calcula_viagem(km, valor, media):
    qtde_litros = km / media
    total = qtde_litros * valor
    return total


def calcular_valor_por_diarias(dias):
    valor_diaria = 0.0
    if dias >= 2 and dias <= 5:
        valor_diaria = 105.00
    elif dias > 5 and dias <= 15:
        valor_diaria = 95.00
    elif dias > 15 and dias <= 25:
        valor_diaria = 70.00
    elif dias > 25:
        valor_diaria = 60,00
    
    total_diaria = dias * valor_diaria
    return total_diaria


def calcular_kilometro(km_rodado):
    valor_por_km = 0.0
    if km_rodado >= 100 and km_rodado <= 1000:
        valor_por_km = 6.99
    elif km_rodado > 1000 and km_rodado <= 4000:
        valor_por_km = 4.99
    elif km_rodado > 4000 and km_rodado <= 6000:
        valor_por_km = 3.99
    elif km_rodado > 6000:
        valor_por_km = 2.99
    
    
    total_kilometros = km_rodado * valor_por_km
    return total_kilometros

