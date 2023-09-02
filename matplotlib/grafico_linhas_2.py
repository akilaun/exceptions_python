import pandas as pd

nome =  "matplotlib/brasilia.CSV"
dados = pd.read_csv(nome, delimiter=";", on_bad_lines="skip", encoding="latin-1", skiprows=8 )

print(dados)
print(dados.columns)
print(dados['Data'])
print(dados['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'])


