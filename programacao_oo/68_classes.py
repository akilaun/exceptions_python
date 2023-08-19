from bombacombustivel import BombaCombustivel

#valor_gasolina = float(input("Qual o valor da gasolina: "))
#valor_etanol = float(input("Qual o valor do etanol: "))

bomba_comb = BombaCombustivel()

print("Seja bem vindo!")

combustivel = input("Qual combustivel (G-Gasolina, E-Etanol) ?\n")
qtde_litros = int(input("Qtd de litros: "))
bomba_comb.abastecer_litros(combustivel, qtde_litros)
qtde_parcelas = 1

if bomba_comb.valor_total < 150:
    bomba_comb.comprovante(combustivel, qtde_litros, qtde_parcelas, bomba_comb.valor_total)
elif bomba_comb.valor_total >= 150:
    deseja_parcelar = input("Deseja Parcelar (S ou N) ?\n")
    if deseja_parcelar == "N":
        bomba_comb.comprovante(combustivel,qtde_litros, qtde_parcelas, bomba_comb.valor_total)
    elif deseja_parcelar == "S":
        qtde_parcelas = int("Quantidade de parcelas: ")
        valor_das_parcelas = bomba_comb.calcular_valor_parcela(qtde_parcelas)
        bomba_comb.comprovante(combustivel,qtde_litros)