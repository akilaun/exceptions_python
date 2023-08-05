"""
Você foi ao supermercado e comprou os seguintes itens:

itens = [
{"produto": "café", "valor": 16.99, "qtde": 1, "categoria": "alimentação"},
{"produto": "leite", "valor": 3.99, "qtde": 1, "categoria": "alimentação"},
{"produto": "pão", "valor": 0.99, "qtde": 8, "categoria": "alimentação"},
{"produto": "detergente", "valor": 1.99, "qtde": 5, "categoria": "limpeza"},
{"produto": "bombril", "valor": 2.99, "qtde": 2, "categoria": "limpeza"},
{"produto": "desinfetante", "valor": 6.99, "qtde": 3, "categoria": "limpeza"},
{"produto": "papel higienico", "valor": 36.99, "qtde": 2, "categoria": "limpeza"},
{"produto": "sabão em pó", "valor": 21.99, "qtde": 2, "categoria": "limpeza"},
{"produto": "carne seca", "valor": 26.99, "qtde": 1, "categoria": "açougue"},
{"produto": "coxa frango", "valor": 23.99, "qtde": 2, "categoria": "açougue"},
]

1) calcule o total por categoria
2) calcule o total da compra
"""

import locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

itens = [
{"produto": "café", "valor": 16.99, "qtde": 1, "categoria": "alimentação"},
{"produto": "leite", "valor": 3.99, "qtde": 1, "categoria": "alimentação"},
{"produto": "pão", "valor": 0.99, "qtde": 8, "categoria": "alimentação"},
{"produto": "detergente", "valor": 1.99, "qtde": 5, "categoria": "limpeza"},
{"produto": "bombril", "valor": 2.99, "qtde": 2, "categoria": "limpeza"},
{"produto": "desinfetante", "valor": 6.99, "qtde": 3, "categoria": "limpeza"},
{"produto": "papel higienico", "valor": 36.99, "qtde": 2, "categoria": "limpeza"},
{"produto": "sabão em pó", "valor": 21.99, "qtde": 2, "categoria": "limpeza"},
{"produto": "carne seca", "valor": 26.99, "qtde": 1, "categoria": "açougue"},
{"produto": "coxa frango", "valor": 23.99, "qtde": 2, "categoria": "açougue"},
]

total_alimentacao = 0
total_acougue = 0
total_limpeza = 0


for i in itens:
    valor = i.get("valor")
    qtde = i.get("qtde")
    categoria = i.get("categoria")
    total = valor * qtde

    if categoria == 'alimentação':
        total_acougue += total
    if categoria == 'limpeza':
        total_alimentacao += total
    if categoria == 'açougue':
        total_limpeza += total
        
    total_da_compra = total_acougue + total_alimentacao + total_limpeza

print(f"\nTotal açougue = {locale.currency(total_acougue)}")
print(f"Total limpeza = {locale.currency(total_limpeza)}")
print(f"Total alimentação = {locale.currency(total_alimentacao)}")
print(f"\nTotal da compra = {locale.currency(total_da_compra)}\n")