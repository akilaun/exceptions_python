cidade_saida = str(input("Insira a cidade de saida: "))
cidade_destino = str(input("Insira a cidade de destino: "))
distancia = float(input("Insira a distancia: "))
km_litro = float(input("Insira consumo do veículo: "))
gas = str(input("Insira o conbustivel: "))
preco = float(input("Insira o preço do combustivel: "))

litros = distancia / km_litro
consumo = preco * litros

print(  f"\n #####RESUMO#####"
        f"\n SAÍDA:{cidade_saida}\n",
        f"DESTINO:{cidade_destino}\n",
        f"Consumo do Veículo: {km_litro}\n",
        f"\nVocê irá gastar R${consumo:.2f} e {litros:.2f}L de {gas}"
    )