"""
O supermercado esta com descontos 

VALOR COMPRA       DESCONTO
R$ 200,00           0,01
R$ 500,00           0,10
R$ 750,00           0,25
acima R$ 750,00     0,35

Ao final imprimir:
- total da compra original
- total da compra com desconto
- desconto que ganhou
"""
valor = int(input("Insira o valor total da compra: "))
desconto = 0

if valor == 200:
    desconto = .01

if valor == 500:
    desconto = .10

if valor == 750:
    desconto = .25
 
if valor > 750:
    desconto = .35

valor_com_desconto = valor - desconto

print(f"\n O valor total da compra é de R${valor}.00."
      f"\n Você ganho R${desconto:.2f} de desconto."
      f"\n O valor total a ser pago é: R${valor_com_desconto:.2f}\n"
      )