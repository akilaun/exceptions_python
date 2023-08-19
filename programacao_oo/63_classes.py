"""
from carro import Carro

carro_gol = Carro() 
print (f"O carro {carro_gol.modelo} \n"
       f"é da marca: {carro_gol.marca} \n"
       f"com a cor: {carro_gol.cor} \n"
       f"ano de fabricação: {carro_gol.ano_fabricacao} \n"
       f"tem rodas: {carro_gol.tem_rodas} \n")
"""
"""
#Importar classe aluno

from aluno import Aluno
aluno_elias = Aluno("Elias da Silva", 18, "elias@gmail.com", "3a5h7q")

print (f"\nAluno {aluno_elias.nome} \n"
       f"Idade {aluno_elias.idade}\n"
       f"Email {aluno_elias.email}\n"
       f"Ra {aluno_elias.ra}\n"
       )

#importar classe aluno e inserir os dados

aluno_akila = Aluno(
    nome = str(input("Insira um nome: ")),
    idade = int(input("Insira a idade: ")),
    email = str(input("Insira o e-mail: ")),
    ra = str(input("Insira o RA: "))
)

print (
    f"\nAluno: {aluno_akila.nome}\n"
    f"Idade: {aluno_akila.idade}\n"
    f"e-mail: {aluno_akila.email}\n"
    f"RA: {aluno_akila.ra}\n"
)
"""
"""
#Importar disciplina

from disciplina import Disciplina

poo = Disciplina(
    nome = str(input("Insira o nome da disciplina: ")), 
    termo = int(input("Termo: ")),
    )
print(f"1 - A disciplina de {poo.nome}, termo: {poo.termo} está aprovada? {poo.aprovada}")
print(f"1 - Qual é o curso? {poo.curso}")
poo.aprovar()
print(f"2 - A disciplina de {poo.nome}, termo: {poo.termo} está aprovada? {poo.aprovada}")
poo.atribuir_curso(str(input("Digite o nome do curso: ")))
print(f"2 - Qual é o curos? {poo.curso}")
"""

#Importar classe Atividade

from atividade import Atividade

atividade_poo = Atividade("Criar classes com poo")
print(atividade_poo)

atividade_logica = Atividade("Criar algoritimos", 5)
print(atividade_logica)