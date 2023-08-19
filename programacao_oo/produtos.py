"""
Utilizando a orientação a objetos 

Criar Produto (descrição, categoria, valor)

Criar loja ( nome, cidade, produtos), sendo que a lista de produtos deve receber os produtos via metodo

Criar Venda (produto, qtde, tipo_venda ("C" ou "D"), total)

"""
from random import randrange
import locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

class Produto:

    def __init__(self,descricao, categoria, valor):
        self.descricao = descricao
        self.categoria = categoria
        self.valor = valor
        self.codigo = randrange(1,10)

    def __str__(self):
        return  f"Codigo {self.codigo}, "\
                f"Nome {self.descricao}, " \
                f"valor {locale.currency(self.valor)}"

class Loja:

    def __init__(self,nome, cidade):
        self.nome = nome
        self.cidade = cidade
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def exibir_produtos(self):
        for produto in self.produtos:
            print(produto)

    def buscar_produto_pelo_cod(self, codigo):
        produto_procurado = None

        for produto in self.produtos:
            if produto.codigo == codigo:
                produto_procurado = produto
                break

        return produto_procurado

class Venda:

    def __init__(self,produto, qtde, tipo_venda):
        self.produto = produto
        self.qtde = qtde
        self.tipo_venda = tipo_venda
        self.total = 0.0
    
    def calcula_total(self):
        self.total = self.qtde * self.produto.valor
    


    