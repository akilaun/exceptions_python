"""
Utilizando a aorientação a objeto cie as classese abaixo:
10 Cliente (conme, cpf, rg, email, ativo)
o campo ativo deve ser modificado via metodo.
"""
import locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')


class Cliente:

    def __init__(self, nome, cpf, rg, email):
        self.nome = nome
        self.cpf = cpf
        self.rg  = rg
        self.email = email
        self.ativo = "Inativo"

    def ativado(self):
        self.ativo = "Ativo"

    def __str__(self):
        return f"O cliente {self.nome}, portador do CPF: {self.cpf}, RG: {self.rg}, email: {self.email} e que se encontra: {self.ativo}."

"""
Conta (banco, nome, descriçao, saldo, cliente, movimentação) 
o campo saldo deve ter dois metodos para trazer modificação, 
a cada operação no saldo salvar em movimentação o registro.
"""

class Conta:

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.saldo = 0.0
        self.movimentacao = []
    
    def sacar(self, valor):
        if valor > self.saldo:
            print("Operação não permitida.")
            print(f"Saldo atual: {locale.currency(self.saldo)}")
            print(self.movimentacao)
        else:
            self.saldo = self.saldo - valor
            mensagem = f"Sacou {locale.currency(valor)}"
            self.movimentacao.append(mensagem)
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        mensagem = f"Depositou {locale.currency(valor)}"
        self.movimentacao.append(mensagem)

    def exibir_extrato(self):
        for mv in self.movimentacao:
            print(mv)

    def __str__(self):
        return (f"Ele possui conta no banco {self.nome}, do tipo {self.descricao} e está com o saldo de {locale.currency(self.saldo)}.")