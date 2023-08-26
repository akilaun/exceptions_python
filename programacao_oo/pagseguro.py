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
    
    def comprovante(self, qtde_parcelas, valor_parcela):
        print("\n")

        if self.operacao == "D":
            self.info_comprovante = (f"Comprovante de venda\n"
                                     f"Operação Débito\n"
                                     f"R$ {self.valor:.2f}")
        elif self.operacao == "C":
            self.info_comprovante = (f"Comprovante de venda\n"
                                     f"Operação Crédito\n"
                                     f"R$ {self.valor}\n"
                                     f"{qtde_parcelas} X "
                                     f"sem juros de R$ {valor_parcela:.2f}")
        print(self.info_comprovante)

    def gerar_qrcode(self):
        nome_arquivo = self.transacao_id + ".png"
        img = qrcode.make(self.info_comprovante)
        img.save(nome_arquivo)
        
        imagem_opcv = cv2.imread(nome_arquivo)
        
        cv2.imshow("QR CODE", imagem_opcv)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
