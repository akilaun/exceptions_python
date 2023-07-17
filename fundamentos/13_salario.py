salario = float(input("Insira o salario: "))
percentual_aumento = float(input("Insira o aumento: "))

valor_aumento = salario * (percentual_aumento / 100)
novo_salario = salario + valor_aumento


print(f"O valor do aumento será: R$ {valor_aumento:.2f}\n"f"O novo salario será: R$ {novo_salario:.2f}")



