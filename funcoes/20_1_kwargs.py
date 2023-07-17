def calcula_media(**dados):
    n1 = dados.get("nota1")
    n2 = dados.get("nota2")
    media = (n1 + n2) / 2
    return media

media = calcula_media(nota1=10, nota2=5)
print(f"A media e: {media}")


