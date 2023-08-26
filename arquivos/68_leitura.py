nome_alunos = "alunos.txt"

with open(nome_alunos, "r", encoding="UTF8") as file:
    for aluno in file.readlines():
        print(f"\nAluno: {aluno}")
