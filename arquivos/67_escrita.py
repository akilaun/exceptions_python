
alunos = ["João", "Maria", "Silvia", "Akilera"]

# WITH = Operador de contexto

nome_alunos = "alunos.txt"
with open(nome_alunos, "w", encoding="UTF8") as arq:
    for aluno in alunos:
        arq.write(f"{aluno}\n")
