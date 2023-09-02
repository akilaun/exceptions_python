import matplotlib.pyplot as plt 
import pandas as pd


try:
    dados = pd.read_csv("matplotlib/chuvas_jan_2023.csv", delimiter = ";")
    #print(dados)

    # define o tamanho do gráfico
    plt.figure(figsize=(10,5))

    # passa as informações dos eixos x, y
    plt.plot(dados["DIA"], dados["VALOR"])

    plt.title("Informações de chuva de Janeiro de 2023")
    plt.xlabel("Dias")
    plt.ylabel("Valores")

    #exibe otodos os valores do eixo
    plt.xticks(dados["DIA"])

    plt.savefig("matplotlib/chuvas_jan_2023.png")
    plt.close("all")
except TypeError as r:
    print(r)
