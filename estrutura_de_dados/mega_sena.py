import requests
import json
import csv

url = f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/latest"

resultado = requests.get(url).json()
#print(json.dumps(resultado, indent=4))
#print(resultado.keys())
dezenas = resultado.get("dezenas")
#print(f'\n\n{dezenas}\n\n')

# Nome do arquivo CSV onde os resultados serão salvos
arquivo_csv = 'resultados_mega_sena.csv'

# Abrindo o arquivo CSV em modo de escrita
with open(arquivo_csv, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Escrevendo o cabeçalho (opcional)
    writer.writerow(['Dezena 1', 'Dezena 2', 'Dezena 3', 'Dezena 4', 'Dezena 5', 'Dezena 6'])

    # Escrevendo os dados das dezenas
    writer.writerow(dezenas)

print(f"Os resultados das dezenas foram salvos no arquivo: {arquivo_csv}")