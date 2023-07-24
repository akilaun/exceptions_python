# Calculo Média

def media (n1, n2):
    return (n1 + n2) / 2



def calcula_media_varias_notas(*notas):
    contador = 0
    total_notas = 0.0
    n = 0

    for nota in notas:
        contador += 1
        total_notas += nota
        while n < 5:
            n += total_notas
        # print(f"Passando pela nota: {nota}")


    media = total_notas / contador
    return (media)
