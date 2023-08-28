try: #Tratamento de excessão
    nome_alunos = "alunos.txt"

    with open(nome_alunos, "r", encoding="UTF8", newline="") as file:
        for aluno in file.readlines():
            print(f"Aluno: {aluno}")
except FileNotFoundError:
    print(f"O arquivo aluno.txt não existe")