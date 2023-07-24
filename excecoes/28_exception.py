try:
    numeros = [1,60,50,23,56]
    print(f"O numero na posicao 5 é: {numeros[3]}")

except IndexError as erro_indice:
    print("\nOcorreu um erro ao acessar o numero")
    print(erro_indice)

finally:
    print("Terminei :)\n")