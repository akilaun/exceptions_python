from produtos import Produto, Loja, Venda

pague_menos = Loja("Supermercado Pague Menos","Piracicaba")

for _ in range(1, 4):
    descricao = input("Digite o nome do produto: ")
    categoria = input ("Digite a categoria: ")
    valor = float(input("Digite o valor: "))

    produto = Produto(
        descricao=descricao,
        categoria=categoria,
        valor=valor              
        )

    pague_menos.adicionar_produto(produto)

for _ in range(1,4):
    print("---Selecione um produto para comprar---")
    produto_comprar = input("Selecione um produto: ")

print("---------------PRODUTOS DISPONIVEIS---------------")
pague_menos.exibir_produtos()
print("--------------------------------------------------")

qtde = int(input("Quantos produtos deseja comprar?\n"))

for _ in range (1, qtde + 1):
    codigo_p = int(input("Digite o código do produto: "))
    produto_procurado = pague_menos.buscar_produto_pelo_cod(codigo_p)
    print((f"Produto Procurado{produto_procurado}"))