from escritor_csv import EscritorCsv

#Lista + Listas

arquivo_comb = "arquivos/combustiveis2.csv"
cabecalho_comb = ["DIA", "GASOLINA", "ETANOL"]
dados_combustivel = [
    ["segunda", 5.09, 3.39],
    ["terça", 5.29, 3.19],
    ["quarta", 5.19, 3.39],
    ["quinta", 5.19, 3.09],
    ["sexta", 5.59, 3.59],
    ["sábado", 5.39, 3.89],
    ["domingo", 5.19, 3.09]
]

escritor_comb = EscritorCsv(nome_arq=arquivo_comb,
                       cabecalho=cabecalho_comb,
                       dados=dados_combustivel)


escritor_comb.escrever()

#Lista + Dicionário

arquivo_temp = "arquivos/temperaturas2.csv"
cabecalho_temp = ["DIA DA SEMANA", "TEMPERATURA"]
dados_temperatura = [
    {"dia": "segunda-feira", "temperatura": 29.6},
    {"dia": "terça-feira", "temperatura": 27.6},
    {"dia": "quarta-feira", "temperatura": 21.6},
    {"dia": "quinta-feira", "temperatura": 28},
    {"dia": "sexta-feira", "temperatura": 26},
    {"dia": "sabado", "temperatura": 21},
    {"dia": "domingo", "temperatura": 27.8}
]

escritor_temp = EscritorCsv(nome_arq=arquivo_temp,
                       cabecalho=cabecalho_temp,
                       dados=dados_temperatura)

escritor_temp.escrever()
