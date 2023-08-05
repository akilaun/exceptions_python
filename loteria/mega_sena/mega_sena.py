import requests
import json
import csv
from tqdm import tqdm  # Importando a biblioteca tqdm

url_base = f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/"
url_last = f"{url_base}latest"

resultado = requests.get(url_base).json()
#dezenas = resultado.get("dezenas")
#concurso = resultado.get("concurso")
resultado_last = requests.get(url_last).json()
ultimo_concurso = resultado_last.get("concurso")
#print(json.dumps(resultado, indent=4))
#print(resultado.keys())
#print(f'\n{concurso} , {dezenas}\n')


# Nome do arquivo CSV onde os resultados serão salvos
arquivo_csv = 'resultados_mega_sena.csv'

# Abrindo o arquivo CSV em modo de escrita
with open(arquivo_csv, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Escrevendo o cabeçalho (opcional)
    writer.writerow(['Dezena 1', 'Dezena 2', 'Dezena 3', 'Dezena 4', 'Dezena 5', 'Dezena 6'])

    # Loop para iterar pelos concursos
    for concurso in tqdm(range(1, ultimo_concurso + 1), desc='Buscando resultados'):
        url_concurso = f"{url_base}{concurso}"
        resultado_concurso = requests.get(url_concurso).json()
        dezenas = resultado_concurso.get("dezenas")

        # Escrevendo os dados das dezenas no arquivo CSV
        writer.writerow([concurso] + dezenas)

print(f"Os resultados das dezenas foram salvos no arquivo: {arquivo_csv}")
