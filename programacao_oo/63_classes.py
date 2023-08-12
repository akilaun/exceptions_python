from carro import Carro

carro_gol = Carro() 
print (f"O carro {carro_gol.modelo} \n"
       f"é da marca: {carro_gol.marca} \n"
       f"com a cor: {carro_gol.cor} \n"
       f"ano de fabricação: {carro_gol.ano_fabricacao} \n"
       f"tem rodas: {carro_gol.tem_rodas} \n")


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