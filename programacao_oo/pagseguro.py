class PagSeguro:

    def __init__(self, valor, operacao):
        self.valor = valor
        self.operacao = operacao

    def calcular_valor_parcela(self, qtde_parcelas):
        valor_parcela = self.valor / qtde_parcelas
        return valor_parcela
    
    def comprovante(self, qtde_parcelas, valor_parcelas):
        print("\n")

        if self.operacao == "D":
            print(f"Comprovante de venda \n"
                  f"Operação Débito\n"
                  f"R$ {self.valor:.2f}")
        elif self.operacao == "C":
            print(f"Comprovante de venda\n"
                  f"Operação Crédito\n"
                  f"R$ {self.valor:.2f}\n"
                  f"{qtde_parcelas} X sem juros de R$ {valor_parcelas:.2f}")
    