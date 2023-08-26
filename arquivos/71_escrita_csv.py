import csv

nome_arquivo = "arquivos/combustiveis.csv"
cabeçalho = ["DIA", "GASOLINA", "ETANOL"]
dados = [
    ["segunda", 5.09, 3.39],
    ["terça", 5.29, 3.19],
    ["quarta", 5.19, 3.39],
    ["quinta", 5.19, 3.09],
    ["sexta", 5.59, 3.59],
    ["sábado", 5.39, 3.89],
    ["domingo", 5.19, 3.09]
]

with open(nome_arquivo, "w", encoding="UTF-8", newline="") as file:
    wrt = csv.writer(file) 
    wrt.writerow(cabeçalho)
    wrt.writerows(dados)

