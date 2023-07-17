def somar(n1, n2):
    return n1 + n2

try:
    numero1 = 10
    numero2 = "20"
    somar(numero1, numero2)
except Exception as erro:
    print("\nOcorreu um erro, tente mais tarde :)")
    print(f"ERRO: {erro}\n")