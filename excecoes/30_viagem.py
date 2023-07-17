#Definindo Função
def calcular_gasto(**kwargs):
    distancia = kwargs.get("distancia")
    media_km_veiculo = kwargs.get("media_km_veiculo")
    valor_combustivel = kwargs.get("valor_combustivel")
    qtd_litros = (distancia / media_km_veiculo)
    valor_gasto = (valor_combustivel * qtd_litros)
    tipo_de_combustivel = kwargs.get("tipo_de_combustivel")
    cidade_saida = kwargs.get("cidade_saida")
    cidade_destino = kwargs.get("cidade_destino")

    print(  
        f"\n ##### RESUMO DA VIAGEM #####"
        f"\n SAÍDA:{cidade_saida}\n",
        f"DESTINO:{cidade_destino}\n",
        f"Consumo do Veículo: {media_km_veiculo}\n",
        f"\nVocê irá gastar R${valor_gasto:.2f} e \n{qtd_litros:.2f}L de {tipo_de_combustivel}\n"
    )

#Insert de dados
try:
    calcular_gasto(
        cidade_saida = str(input("Insira a cidade de saida: ")),
        cidade_destino = str(input("Insira a cidade de destino: ")),
        tipo_de_combustivel = str(input("Insira o combustivel: ")),
        distancia = float(input("Insira o distancia: ")),
        media_km_veiculo = float(input("Insira o consumo médio do veículo: ")),
        valor_combustivel = float(input("Insira o valor do combustivel: "))
    )
except ValueError as erro_valor:
    print (f"Erro de valor {erro_valor}")
except ZeroDivisionError as erro_zero:
    print (f"Erro de divisao {erro_zero}")
except Exception as erro:
    print (f"Erro {erro}")








