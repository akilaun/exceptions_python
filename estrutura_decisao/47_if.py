"""
Exemplo de uso de if-elseif-else em python
"""

idade = int(input("Digite sua idade "))

if idade < 18:
    print("Você é menor de idade")
elif idade > 18:
    print("Você é maior de idade")

nota = float(input("Digite sua nota "))

if nota >= 9.0:
    print(f"Está de parabéns sua nota foi {nota}")
elif nota >= 6.5 and nota < 9.0:
    print(f"Você está aprovado")
elif nota >= 4.0 and nota < 6.5:
    print(f"Você está de recuperação")
else:
    print(f"Você está reprovado")