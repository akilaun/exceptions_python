import qrcode
import cv2
from uuid import uuid4
import locale 
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

class PagSeguro:

    def __init__(self, valor, operacao):
        self.valor = valor
        self.operacao = operacao
        self.info_comprovante = ""
        self.transacao_id = str(uuid4())

    def calcular_valor_parcela(self, qtde_parcelas):
        valor_parcela = self.valor / qtde_parcelas
        return valor_parcela
    
    def comprovante(self, qtde_parcelas, valor_parcelas):
        print("\n")

        if self.operacao == "D":
            print(f"Comprovante de venda \n"
                  f"Operação Débito\n"
                  f"{locale.currency(self.valor)}")
        elif self.operacao == "C":
            print(f"Comprovante de venda\n"
                  f"Operação Crédito\n"
                  f"{locale.currency(self.valor)}\n"
                  f"{qtde_parcelas} X sem juros de {locale.currency(valor_parcelas)}")

    def gerar_qrcode(self):
        nome_arquivo = self.transacao_id + ".png"
        img = qrcode.make(self.info_comprovante)
        img.save(nome_arquivo)
        
        imagem_opcv = cv2.imread(nome_arquivo)
        
        cv2.imshow("QR CODE", imagem_opcv)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
