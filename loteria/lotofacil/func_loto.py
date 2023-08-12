#Numeros que mais se repetem
def encontrar_numeros_mais_repetem(vetores, quantidade):
    contagem_numeros = [0] * 26  # Inicializa uma lista de contagem para cada número de 1 a 25
    
    for vetor in vetores:
        for numero in vetor:
            contagem_numeros[numero] += 1
    numeros_mais_repetem = sorted(range(1, 25), key=lambda num: contagem_numeros[num], reverse=True)[:quantidade]
    return numeros_mais_repetem


#Numeros que menos se repetem
def encontrar_numeros_menos_repetem(vetores, quantidade):
    contagem_numeros = [0] * 26  # Inicializa uma lista de contagem para cada número de 1 a 25
    
    for vetor in vetores:
        for numero in vetor:
            contagem_numeros[numero] += 1
    numeros_menos_repetem = sorted(range(1, 25), key=lambda num: contagem_numeros[num], reverse=False)[:quantidade]
    return numeros_menos_repetem


#Numeros que não se repetem
def encontrar_numeros_nao_repetem(vetores):
    contagem_numeros = [0] * 26
    
    for vetor in vetores:
        for numero in vetor:
            contagem_numeros[numero] += 1
    
    numeros_nao_repetem = [num for num, contagem in enumerate(contagem_numeros) if contagem == 1]
    return numeros_nao_repetem


