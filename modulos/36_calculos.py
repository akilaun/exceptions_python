from calculadora import somar, subtrair

rs_soma = somar(
    int(input("Insira um numero inteiro: ")),
    int(input("Insira um numero inteiro: "))
    )
print(f"O resutlado da soma é: {rs_soma}")

import calculadora

rs_sub = calculadora.subtrair(
    int(input("Insira um numero inteiro: ")),
    int(input("Insira um numero inteiro: "))
    )
print(f"O resultado da subtração é: {rs_sub}")