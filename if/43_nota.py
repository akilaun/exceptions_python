media = float(input("Digite a média do aluno: "))

if media >= 9.0:
    print(f"Você está de parabéns, APROVADO :)")
elif media >= 5.5 and media < 9.0:
    print(f'="Você está aprovado, ok')
elif media >= 4.0 and media < 5.5:
    print(f"Você está de recuperação.")
elif media < 4.0:
    print(f"REPROVADO")