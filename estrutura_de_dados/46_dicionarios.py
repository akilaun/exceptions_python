"""
Exemplos de dicionarios com python
"""
from datetime import datetime
import json 

aluno = dict(nome="Sergio", idade=22, cidade="Santos")
print(f"O aluno tem as propriedades: {aluno}")


aluno2 = {
    "nome": "Sergio",
    "idade": 22,
    "cidade": "Santos"
}
print(f"O aluno tem as propriedades: {aluno2}")



aluno_eletrica = {
    "nome": "Elias Silva Santos",
    "idade": 19,
    "cidade": "Piracicaba",
    "aluno_senai": True,
    "disciplinas": ["CLP","Comandos Eletricos"],
    "matriculado": True,
    "data da matricula": str(datetime.now()),
    "endereco":{
        "logradouro":"Rua 10, 560",
        "bairro": "Jardim das Flores",
        "cidade": "Santos",
        "cep": 12247305,
        "uf": "SP"
    }
}

print(f"Dados do aluno: {aluno_eletrica}")

#Verificando o tipo da variavel
print(type(aluno_eletrica))

#Acessando propriedades
nome = aluno_eletrica.get("nome")
cidade = aluno_eletrica.get("cidade")
matriculado = aluno_eletrica["matriculado"]
print(f"Nome aluno: {nome}\n"
      f"cidade: {cidade}\n"
      f"matriculado: {matriculado}\n"
    )

# endereco = aluno_eletrica["end"]
# print(f"1-O endereço do aluno é: {endereco}")

endereco2 = aluno_eletrica.get("end", "rua 10")
print(f"2-O endereço do aluno é: {endereco2}")

# Imprimindo dicionario formatado

print(json.dumps(aluno_eletrica, 
                 sort_keys=False, 
                 indent=4))


disciplinas = aluno_eletrica.get("disciplinas")
disciplina_2 = disciplinas[1]
print(disciplinas)
print(f"A disciplina é: {disciplina_2}")

endereco = aluno_eletrica.get("endereco")
print(type(endereco))
print(endereco)

bairro = aluno_eletrica.get("bairro")
print(f"Bairro: {bairro}")


cidade = aluno_eletrica.get("endereco").get("cidade")
print(f"Cidade {cidade}")

#Remover propriedade do dicionario
del aluno_eletrica["matriculado"]
print(json.dumps(aluno_eletrica, indent = 4))


#Alteração de item do dicionario
aluno_eletrica["cidade"] = "Rio das Pedras"
print(json.dumps(aluno_eletrica,indent=4))

# Alteração de item dentro de outro item
aluno_eletrica["endereco"]["cep"] = ""
print(json.dumps(aluno_eletrica, indent=4))

#Alteração da disciplina que esstá dentro de uma lista
aluno_eletrica["disciplinas"][1] = "Eletronica Digital"
print(json.dumps(aluno_eletrica,indent=4))

#Adicionar um item na lista do dicionario
aluno_eletrica["disciplinas"].append("Eletronica Analogica")
print(json.dumps(aluno_eletrica,indent=4))


