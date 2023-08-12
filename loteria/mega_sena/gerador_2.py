from func_mega import encontrar_numeros_mais_repetem, encontrar_numeros_menos_repetem, encontrar_numeros_nao_repetem
import csv
import random

base_mega_sena = []

with open('resultados_mega_sena.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        try:
            vector = [int(num) for num in row]
            base_mega_sena.append(vector)
        except ValueError:
            print("Erro ao ler vetor:", row)

quantidade_numeros = 6
quantidade_apostas = 1
mais_repetem = encontrar_numeros_mais_repetem(base_mega_sena,quantidade_numeros)
menos_repetem = encontrar_numeros_menos_repetem(base_mega_sena,quantidade_numeros)
nao_repetem = encontrar_numeros_nao_repetem(base_mega_sena)

#Gerar apostas 
aposta1 = [mais_repetem]
while len(aposta1) < quantidade_apostas:
    numeros_par = random.sample(range(2, 61, 2), 4)
    numeros_impar = random.sample(range(1, 61, 1), 2)
    novas_apostas = numeros_par + numeros_impar
    if novas_apostas not in base_mega_sena and novas_apostas not in aposta1:
        aposta1.append(novas_apostas)

aposta2 = [menos_repetem]
while len(aposta2) < quantidade_apostas:
    numeros_par = random.sample(range(2, 61, 2), 3)
    numeros_impar = random.sample(range(1, 61, 1), 3)
    novas_apostas = numeros_par + numeros_impar
    if novas_apostas not in base_mega_sena and novas_apostas not in aposta2:
        aposta2.append(novas_apostas)  


#Printa as apostas
print(f"\n\n{quantidade_apostas+1} Apostas para ganhar:\n")
for vector in aposta1:
    print(vector)
for vector in aposta2:
    print(vector)
print("\n")

