try: #Tratamento de excessão
    nome_alunos = "aluno.txt"

    with open(nome_alunos, "r", encoding="UTF8") as file:
        for aluno in file.readlines():
            print(f"\nAluno: {aluno}")
except FileNotFoundError:
    print(f"O arquivo aluno.txt não existe")