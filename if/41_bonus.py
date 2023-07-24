"""
Crie o algoritimo para exibir o bonus do usuário conforme a recarga de celular, utilize a seguinte tabela:
VALOR           BONUS
R$15,00         200MB
R$25,00         300MB
R$40,00         450MB
Acima R$40,00   600MB

"""

recarga = int(input("Insira o valor da recarga: "))
bonus = 0

if recarga == 15:
    bonus = 200
if recarga == 25:
    bonus = 300
if recarga == 45:
    bonus = 450
if recarga >= 40:
    bonus = 600

print(f"Sua recarga foi de R$ {recarga},00 e bonus igual {bonus} MB")