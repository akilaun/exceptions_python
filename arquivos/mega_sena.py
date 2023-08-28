import requests
import json
import csv
from time import sleep

url_base = "https://loteriascaixa-api.herokuapp.com/api/megasena"


concursos = [2624,2623,2622,2621]

todas_dezenas = []

for concurso in concursos:
    url = f"{url_base}/{concurso}"
    resultado = requests.get(url).json() #facilitador transaforma em dicionario
    dezenas = resultado.get("dezenas")
    data = resultado.get("data")
    info = {
        "data": data,
        "dezenas_sorteadas": dezenas
    }
    
    todas_dezenas.append(info)
    sleep(3)
    
cabecalho = ["DATA","D1","D2","D3","D4","D5","D6"]
with open("arquivos/mega_sena.csv","w",newline="") as arq:
    escritor = csv.writer(arq)
    escritor.writerow(cabecalho)
    print(cabecalho)    
    
    for linha in todas_dezenas:
        data = linha.get("data")
        dezenas_sorteadas = linha.get("dezenas_sorteadas")
        d1 = dezenas_sorteadas[0]
        d2 = dezenas_sorteadas[1]
        d3 = dezenas_sorteadas[2]
        d4 = dezenas_sorteadas[3]
        d5 = dezenas_sorteadas[4]
        d6 = dezenas_sorteadas[5]
        escritor.writerow([data,d1,d2,d3,d4,d5,d6])
        print([data,d1,d2,d3,d4,d5,d6])