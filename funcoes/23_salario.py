def calcula_aumento_salario(salario, percentual_aumento):
    valor_aumento = salario * (percentual_aumento / 100)
    novo_salario = salario + valor_aumento
    return novo_salario, valor_aumento

#Entrada
salario = float(input("\nInsira o salario atual: "))
percentual_aumento = float(input("Insira o valor do aumento em porcentagem: "))

#Processamento

sal_novo, aumento = calcula_aumento_salario(salario, percentual_aumento)


print(f"\n-----------------------------------------------------------------------------\n")
print(
    f"O valor do ajuste será de: R${aumento:.2f}"
    f"O valor do salário ajustado será: R${sal_novo:.2f}"
    )
print(f"\n-----------------------------------------------------------------------------")


