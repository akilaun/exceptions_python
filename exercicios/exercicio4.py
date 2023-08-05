#4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais_mai = ("A","E","I","O","U")
vogais_min = ("a","e","i","o","u")
letra = str(print(input("Digite uma letra: ")))

if letra == vogais_mai:
    print (f"A letra {letra} é uma VOGAL.")
else:
    print(f"A letra {letra} é uma CONSOANTE.")