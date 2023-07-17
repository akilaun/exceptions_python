#Definindo Função
def calculo_do_desconto(preco,desconto):
    valor_do_desconto = float((preco * desconto) / 100)
    total_com_desconto = float(preco - valor_do_desconto)
    return valor_do_desconto, total_com_desconto

def exibir_info_produto(nome_p,preco_p,desconto_p,valor_do_desconto_p,total_com_descontos_p):
    print(f"\nProduto: {nome_p}\n"
      f"Preço:R$ {preco_p:.2f}\n"
      f"Desconto: {desconto_p:.2f}%\n\n"
      f"Valor do desconto:R$ {valor_do_desconto_p:.2f}\n"
      f"Total com desconto:R$ {total_com_descontos_p:.2f}\n"
)


#Inserindo Dados
nome_p = str(input("Insira o nome do produto: "))
preco_p = float(input("Insira o preço do produto:R$"))
desconto_p = float(input("Insira o valor do desconto em porcentagem: "))

valor_do_desconto_p, total_com_descontos_p = calculo_do_desconto(preco,desconto)

#Printando resultado

exibir_info_produto()

