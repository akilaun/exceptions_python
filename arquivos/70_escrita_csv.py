import csv

nome_arquivo = "arquivos/temperaturas.csv"
cabeçalho = ["DIA DA SEMANA", "TEMPERATURA"]
dados = [
    {"dia": "segunda-feira", "temperatura": 29.6},
    {"dia": "terça-feira", "temperatura": 27.6},
    {"dia": "quarta-feira", "temperatura": 21.6},
    {"dia": "quinta-feira", "temperatura": 28},
    {"dia": "sexta-feira", "temperatura": 26},
    {"dia": "sabado", "temperatura": 21},
    {"dia": "domingo", "temperatura": 27.8}
]

with open(nome_arquivo,"w",encoding="UTF8", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(cabeçalho)

    for info in dados:
        dia_semana = info.get("dia")
        temperatura = info.get("temperatura")
        escritor.writerow([dia_semana,temperatura])