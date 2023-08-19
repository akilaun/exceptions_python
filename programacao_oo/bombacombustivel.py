import locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

class BombaCombustivel:
    def __init__(self, valor_gasolina = 5.99, valor_etanol = 3.99):
        self.valor_gasolina = valor_gasolina
        self.valor_etanol = valor_etanol
        self.valor_total = 0.0

    def abastecer_litros(self, combustivel, qtde_litros):
        if combustivel == "G":
            self.valor_total = self.valor_gasolina * qtde_litros
        elif combustivel == "E":
            self.valor_total = self.valor_etanol * qtde_litros

    def calcular_valor_parcela(self, qtde_parcelas):
        valor_parcela = self.valor_total / qtde_parcelas
        return valor_parcela
    
    def comprovante(self, combustivel, qtde_litros, qtde_parcelas, valor_parcela):
        print("\n")
        combustivel_nome = ""
        if combustivel == "G":
            combustivel_nome = "Gasolina"
        elif combustivel == "E":
            combustivel_nome = "Etanol"

        if qtde_parcelas == 1:
            print(f"Comprovante de abastecimento\n\n"
                  f"Combustivel {combustivel_nome}\n"
                  f"{qtde_litros} Litros\n"
                  f"Valor {locale.currency(self.valor_total)}")
        elif qtde_parcelas > 1:
            print(f"Comprovante de abastecimento\n\n"
                  f"Combustivel {combustivel_nome}\n"
                  f"{qtde_litros} Litros\n"
                  f"Valor {locale.currency(self.valor_total)}"
                  f"{qtde_parcelas}x {valor_parcela}"
                  
                  )
        
