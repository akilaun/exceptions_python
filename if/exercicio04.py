"""
Escreva um programa para aprovar um empréstimo bancário para compra de uma casa, o programa vai perguntar o valor da casa a comprar, o salário da pessoa e a quantidade de anos a pagar. 
O valor da prestação mensal não pode ser superior a 30% do salário.
"""

nome  = input("Informe seu nome: ")
valor_da_casa = float(input("Informe o valor da casa: "))
salario_do_comprador = float(input("Informe o seu salário: "))
quantidade_de_anos_a_pagar = int(input("Informe o tempo, em anos, a pagar: "))
porcentagem = 0.3

parcela = quantidade_de_anos_a_pagar * 12
prestacao = valor_da_casa / parcela
margem_de_seguranca = salario_do_comprador * porcentagem
if prestacao > margem_de_seguranca:
   print("\n***eu emprestimo não foi aprovado.***\n\n"
         "O valor da prestação deve ser menor que 30% do seu salário"
        f"\nValor a pagar: R${prestacao:.2f} em {quantidade_de_anos_a_pagar} parcelas"
        f"\nMargem de segurança: R${margem_de_seguranca:.2f}\n"
        )
else:
   print("\n***Emprestimo aprovado!***\n\n"
         f"Você pagar o valor de R$ {prestacao:.2f} em {quantidade_de_anos_a_pagar} parcelas"
         f"\nMargem de segurança: R${margem_de_seguranca:.2f}\n"
         )