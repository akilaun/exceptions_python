#Definindo Função
def calcular_viagem(km, valor, media):
    qtde_litros = km/media
    custo_total = qtde_litros*valor
    return custo_total


kilometros = 200
total_gasolina = calcular_viagem(kilometros, 5.59,11)
print(f"\nGasolina: R${total_gasolina:.2f}")

total_etanol = calcular_viagem(kilometros, 3.89,9)
print(f"Etanol: R${total_etanol:.2f}")

total_diesel = calcular_viagem(kilometros, 6.59,15)
print(f"Diesel: R${total_diesel:.2f}")

total_diesel_s10 = calcular_viagem(kilometros, 7.59,17)
print(f"Diesel S10: R${total_diesel_s10:.2f}\n")