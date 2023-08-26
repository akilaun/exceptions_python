import csv



"""
nome_arquivo = "arquivos/combustiveis2.csv"

with open(nome_arquivo,"r", encoding="UTF8", newline="") as arq:
    leitor = csv.reader(arq)
    
    for linha in leitor:
        print(linha)
"""
"""
#remover cabeçalho:
nome_arquivo = "arquivos/combustiveis2.csv"

with open(nome_arquivo,"r", encoding="UTF8", newline="") as arq:
    leitor = csv.reader(arq)
    
    for indice, linha in enumerate(leitor):
        if indice > 0:
            print(linha)
"""

#imprimir linhas que eu quero que imprima

nome_arquivo = "arquivos/combustiveis2.csv"

with open(nome_arquivo,"r", encoding="UTF8", newline="") as arq:
    leitor = csv.reader(arq)
    
    for indice, linha in enumerate(leitor):
        if indice > 0:
            dia = linha[0]
            valor_g = linha[1]
            valor_e = linha[2]
            print(f"Dia: {dia}, Gasolina: {valor_g}, Etanol: {valor_e}")

