def calcular_media():
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))
    media = (nota1+nota2+nota3+nota4)/4
    print(f"\nNota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")
    print(f"Nota 4: {nota4}")
    print(f"\nA media do aluno é: {media} ")
    if media >= 7:
        print("\n***Aprovado***")
    else:
        print("\n***Reprovado***")

calcular_media()

