nome = str(input("Insira o nome do produto: "))
preco = float(input("Insira o preço do produto:R$"))
desconto = float(input("Insira o valor do desconto em porcentagem: "))

valor_do_desconto = float((preco * desconto) / 100)
total_com_desconto = float(preco - valor_do_desconto)
parcela = float(total_com_desconto/10)

print(f"\nProduto: {nome}\n"
      f"Preço:R$ {preco:.2f}\n"
      f"Desconto: {desconto:.2f}%\n\n"
      f"Valor do desconto:R$ {valor_do_desconto:.2f}\n"
      f"Total com desconto:R$ {total_com_desconto:.2f}"
      f"\nParcela em 10x: R${parcela:.2f}"
      )



