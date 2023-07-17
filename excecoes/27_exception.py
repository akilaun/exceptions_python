def calcular_media(n1,n2):
    return (n1+n2)/2

try:
    nota1 = 5.5
    nota2 = "AKILA"
    rs = calcular_media(nota1,nota2)
except Exception as ex:
    print(f"\nOcorreu um erro {ex}")
finally:
    print("Terminei\n")