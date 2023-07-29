"""
Buscar os dados de endereço do usuário conforme o cep informado via input de dados
"""
import requests
import json

cep = int(input("Digit o seu CEP, somente numeros: "))
url = f"https://viacep.com.br/ws/{cep}/json"

endereco = requests.get(url).json()
print(json.dumps(endereco, indent=4))


