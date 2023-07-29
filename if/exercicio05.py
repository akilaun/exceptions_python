"""
Calcule o preco a pagar pelo fornecimento de energia elétrica, pergunte a quantidade de KW/h consumido e o tipo de instalação elétrica, 
considere R para residência, I para indústria e C para comércio, utilize a tabela abaixo para as faixas de consumo.
"""
# Definindo as funções para calculo do consumo

def residencia(consumo_r):
    preco_r = 0
    if consumo_r > 500:
        preco_r = 0.65
    else:
        preco_r = 0.40
    valor_a_pagar_r = consumo_r * preco_r
    return valor_a_pagar_r

def comercio(consumo_c):
    preco_c = 0
    if consumo_c > 1000:
        preco_c = 0.60
    else:
        preco_c = 0.55
    valor_a_pagar_c = consumo_c * preco_c
    return valor_a_pagar_c

def industria(consumo_i):
    preco_i = 0
    if consumo_i > 5000:
        preco_i = 0.65
    else:
        preco_i = 0.40
    valor_a_pagar_i = consumo_i * preco_i
    return valor_a_pagar_i

#Entrada dos dados:
tipo_de_instalacao = input("\nInsira o tipo de instalação "
                           "\nR - Residencia"
                           "\nC - Comercio"
                           "\nI - Industria:\n"
                        )
kwh_consumido = float(input("Insira o consumdo mensal de energia em Kw/h: "))

#Lógica para calculo do tipo de instalação:
if tipo_de_instalacao == 'R' or tipo_de_instalacao == 'r':
    valor_a_pagar = residencia(kwh_consumido)
    print(
        f"\nSua instalação foi identificada como {tipo_de_instalacao} - RESIDENCIA.\n"
        f"O Valor a ser pago será de R${valor_a_pagar:.2f}\n"
        )

elif tipo_de_instalacao == 'C' or tipo_de_instalacao == 'c':
    valor_a_pagar = comercio(kwh_consumido)
    print(
        f"\nSua instalação foi identificada como {tipo_de_instalacao} - COMERCIO.\n"
        f"O Valor a ser pago será de R${valor_a_pagar:.2f}\n"
        )

elif tipo_de_instalacao == 'I' or tipo_de_instalacao == 'i' :
    valor_a_pagar = industria(kwh_consumido)
    print(
        f"\nSua instalação foi identificada como {tipo_de_instalacao} - IDUSTRIA.\n"
        f"O Valor a ser pago será de R${valor_a_pagar:.2f}\n"
        )
else:
    print("Tipo de instalação não mapeadas")