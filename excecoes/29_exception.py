try:
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    fator = int(input("Digite o fator para dividir: "))
    media = (nota1 + nota2) / fator
    print(f"A media e {media}")
except ValueError as erro_valor:
    print (f"Erro de valor {erro_valor}")
except ZeroDivisionError as erro_zero:
    print (f"Erro de divisao {erro_zero}")
except Exception as erro:
    print (f"Erro {erro}")