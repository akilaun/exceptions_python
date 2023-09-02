import pandas as pd
from datetime import datetime
import json
import matplotlib.pyplot as plt

nome =  "matplotlib/brasilia.CSV"
dados = pd.read_csv(nome, delimiter=";", on_bad_lines="skip", encoding="latin-1", skiprows=8 )




meses = [
    {"mes_numero":1, "mes_nome": "Jan", "total_chuva":0.0},
    {"mes_numero":2, "mes_nome": "Fev", "total_chuva":0.0},
    {"mes_numero":3, "mes_nome": "Mar", "total_chuva":0.0},
    {"mes_numero":4, "mes_nome": "Abr", "total_chuva":0.0},
    {"mes_numero":5, "mes_nome": "Mai", "total_chuva":0.0},
    {"mes_numero":6, "mes_nome": "Jun", "total_chuva":0.0},
    {"mes_numero":7, "mes_nome": "Jul", "total_chuva":0.0},
    {"mes_numero":8, "mes_nome": "Ago", "total_chuva":0.0},
    {"mes_numero":9, "mes_nome": "Set", "total_chuva":0.0},
    {"mes_numero":10, "mes_nome": "Out", "total_chuva":0.0},
    {"mes_numero":11, "mes_nome": "Nov", "total_chuva":0.0},
    {"mes_numero":12, "mes_nome": "Dez", "total_chuva":0.0}
]

for indice,linha in dados.iterrows():#iterar/passar pelas linhas
    data=datetime.strptime(linha["Data"],'%Y/%m/%d').date() 
    mes = data.month

    #tratando a chava, esta com ',' ao inves de '.'
    chuva=str(linha["PRECIPITAÇÃO TOTAL, HORÁRIO (mm)"])
    chuva = float(chuva.replace(",","."))
    
    for mes_dict in meses:
        if mes_dict["mes_numero"] == mes:
            mes_dict["total_chuva"] += chuva

for mes_d in meses:
    mes_d["total_chuva"] = round(mes_d["total_chuva"], 3)


print(json.dumps(meses, indent=4))
    
dados_grafico = [ [],[] ]

for mes_d in meses:
    dados_grafico[0].append(mes_d["mes_numero"])
    dados_grafico[1].append(mes_d["total_chuva"])

plt.figure(figsize=(10,5))
#plt.plot(dados_grafico[0], dados_grafico[1])
plt.bar(dados_grafico[0], dados_grafico[1]) #para gerar grafico com barras
plt.title("Informações Chuvas 2022")
plt.xlabel("Meses")
plt.ylabel("Valores")
plt.xticks(dados_grafico[0])
plt.savefig("matplotlib/chuvas2022_bar.png")
plt.close(all)