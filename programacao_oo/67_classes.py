from pagseguro import PagSeguro

def calcular():
    print("Seja bem vindo ao pag seguro, vamos calcular sua venda.")
    valor = float(input("Valor total do produto: "))
    operacao = input("Operação D para Débito, C para Crédito: ")

    pagseguro = PagSeguro(valor, operacao)

    if operacao == "D":
        pagseguro.comprovante(1, valor)

    elif operacao == "C":
        qtde_parcelas = int(input("Insira o numero de parcelas: "))
        valor_parcela = pagseguro.calcular_valor_parcela(qtde_parcelas)
        pagseguro.comprovante(qtde_parcelas, valor_parcela)

    pagseguro.gerar_qrcode()

    print("\n")
    continuar = input ("Deseja realizar outra venda? S ou N\n")
    if continuar == "S":
        calcular()

calcular()