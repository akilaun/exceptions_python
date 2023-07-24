from calculos import calcula_viagem

cidade_p = input("Digite a cidade de partida: ")
cidade_d = input("Digite a cidade de destino: ")
km = int(input("Digite o km: "))
valor_g = float(input("Digite o valor da gasolina: "))
valor_e = float(input("Digite o valor do etanol: "))
media_g = int(input("Digite a media da gasolina: "))
media_e = int(input("Digite a media do etanol: "))

total_g = calcula_viagem(km, valor_g, media_g)
total_e = calcula_viagem(km, valor_e, media_e)

if total_g < total_e:
    print(f"Recomendamos utilizar a gasolina pois o gasto será: {total_g}")
if total_e < total_g:
    print(f"Recomendamos utilizar o etanol pois o gasto com etanol será: {total_e}")
