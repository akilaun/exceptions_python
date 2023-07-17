def calcula_gasto_de_combustivel (km_percorrido, valor, media_km=9): # Valor default de media_km = 9
    qtde_litros = km_percorrido / media_km
    valor_total = qtde_litros * valor
    return valor_total

km = float(input("\nInsira o km: "))
valor_gasolina = float(input("Insira o preço do litro da gasolina: "))
km_litro = float(input("Insira o consumo do veículo: "))

rs01 = calcula_gasto_de_combustivel(km, km_litro)
rs02 = calcula_gasto_de_combustivel(km, valor_gasolina)

print(f"\nValor da consulta 01: R${rs01:.2f}")
print(f"Valor da consulta 02: R${rs02:.2f}\n")
