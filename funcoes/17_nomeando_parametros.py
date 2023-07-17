def calcula_aumento_salario(salario, percentual_aumento):
    valor_aumento = salario * (percentual_aumento / 100)
    novo_salario = salario +valor_aumento
    return novo_salario

salario_atual = float(input("\nInsira o salario atual: "))
percentual = float(input("Insira o valor do aumento em porcentagem: "))
aumento = salario_atual*(percentual/100)
salario_ajustado = calcula_aumento_salario(percentual_aumento=percentual, salario=salario_atual)
print(f"\n-----------------------------------------------------------------------------\n")
print(f"O valor do ajuste será de: R${aumento:.2f}")
print(f"O valor do salário ajustado será: R${salario_ajustado:.2f}")
print(f"\n-----------------------------------------------------------------------------")
print(f"-----------------------------------------------------------------------------")