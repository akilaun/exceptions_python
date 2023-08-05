"""
Lendo dicionários com for
"""

aluno = {
    "nome": "Akila V. Bindilatti",
    "idade": 36,
    "aluno_senai": True,
    "curso": "Programação em Python"
}

for chave, valor in aluno.items():
    print(f"Chave {chave}, Valor {valor}")
