"""
Atividade
1) Criar um arquivo 74_notas.csv com as informações abaixo contidas no arquivo notas.png.
2) Fazer a leitura do arquivo 74_notas.csv calcular a média para todos os alunos e salvar todas as informações no arquivo 75_notas_e_medias.csv
3) Criar o arquivo 76_notas.zip dentro da pasta arquivos contendo os dois arquivos criados nos itens acima.

"""

import csv

with open("arquivos/74_notas.csv", "r", encoding="UTF8", newline="") as notas:
    leitor = csv.reader(notas)
    cabecalho = next(leitor)  # Lê a primeira linha como o cabeçalho

    with open("arquivos/75_notas_e_medias.csv", "w", encoding="UTF8", newline="") as media:
        escritor = csv.writer(media)
        escritor.writerow(cabecalho)  # Escreve o cabeçalho no arquivo de saída

        for linha in leitor:  # Itera pelas linhas restantes das notas
            disciplina = linha[0]
            aluno = linha[1]
            nota1 = float(linha[2])
            nota2 = float(linha[3])
            media = round(((nota1 + nota2) / 2),2)

            escritor
            escritor.writerow([disciplina, aluno, nota1, nota2, media])  # Escreve a linha no arquivo de saída
            print([disciplina, aluno, nota1, nota2, media])
