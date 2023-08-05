"""
Calcule o salario dos funcionários conforme tabela abaixo:

Cargo       Salário       INSS     Convenios
Gerente     R$ 5590,00     8%      R$ 289,00
Supervisor  R$ 4128,00     7%      R$ 239,00
Técnico     R$ 3789,00     4%      R$ 189,00
Auxiliar    R$ 2345,00     2%      R$ 156,00

Imprimir ao final as informações da tabela e o salario calculado
"""
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')

cargos = [
    {
    "cargo":"Gerente",
    "salario": 5590,
    "inss": 8,
    "convenios": 289
    },
    {
    "cargo":"Supervisor",
    "salario": 4128,
    "inss": 7,
    "convenios": 239
    },
    {
    "cargo":"Técnico",
    "salario": 3789,
    "inss": 4,
    "convenios": 189
    },
    {
    "cargo":"Auxiliar",
    "salario": 2345,
    "inss": 2,
    "convenios": 156
    }
]

for c in cargos:
    cargo = c.get("cargo")
    salario = c.get("salario")
    convenio = c.get("convenios")
    inss = c.get("inss")

    desconto_inss = salario*(inss/100)
    total_de_descontos = convenio+desconto_inss
    salario_c_desconto = salario-desconto_inss-convenio

    print(f"O {cargo} possui o salario de {locale.currency(salario)}."
          f"\nO total de desconto é igual a {locale.currency(total_de_descontos)}, sendo {locale.currency(desconto_inss)} ({inss}%) de INSS e {locale.currency(convenio)} de Convenios."
          f"\nO salario final do {cargo} é de {locale.currency(salario_c_desconto)}.\n")