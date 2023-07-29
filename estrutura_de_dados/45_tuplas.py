"""
Exemplo de tuplas com python
"""


cidades = ("Piracicaba","Santos","Americana")

print(f"A cidade de {cidades[1]} é linda.")
print(f"A qtde de elementos é {len(cidades)}")

#Alterações de elementos na tupla não é possivel pois os elementos de uma tupla são imutaveis
# cidades[1] = "ITU"

#Adicionar item na tupla
cidades += ("Itu","Santa Barbara D'Oeste")
print(f"1- Cidades:{cidades}")

