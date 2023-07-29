import requests
import json

url = f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/latest"

resultado = requests.get(url).json()
#print(json.dumps(resultado, indent=4))
#print(resultado.keys())
dezenas = resultado.get("dezenas")
print(f'\n\n{dezenas}\n\n')