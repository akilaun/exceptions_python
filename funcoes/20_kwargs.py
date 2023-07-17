def calcula_salario(**kwargs):
 
    salario = kwargs.get("salario")
    desconto_inss = kwargs.get("inss")/100
    desconto_plano_de_saude = kwargs.get("plano")
    total_descontos = desconto_inss + desconto_plano_de_saude
    desconto_inss_salario = desconto_inss * salario
    sal_liquido = salario - total_descontos
    print(f"\nSalario bruto R${salario:.2f}")
    print(f"Desonto INSS: R${desconto_inss_salario}")
    print(f"Desconto Plano de Saúde: R${desconto_plano_de_saude}")
    print(f"Total de descontos R${total_descontos:.2f}")
    print(f"Salario liquido R${sal_liquido:.2f}\n")


calcula_salario(
    salario=float(input("Insira o valor do salario BRUTO: ")), 
    inss=float(input("Insira o valor do desconto do INSS em porcentagem: ")), 
    plano=float(input("Insira o valor do desconto do plano de saúde: "))
) 




