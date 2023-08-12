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

#Gerar apostas contendo 4 numeros pares e 2 impares que mais repetem
apostas_4_pares_2_impar_mais = [mais_repetem]
while len(apostas_4_pares_2_impar_mais) < quantidade_apostas:
    numeros_par = random.sample(range(2, 61, 2), 4)
    numeros_impar = random.sample(range(1, 61, 2), 2)
    novas_apostas = numeros_par + numeros_impar
    if novas_apostas not in base_mega_sena and novas_apostas not in apostas_4_pares_2_impar_mais:
        apostas_4_pares_2_impar_mais.append(novas_apostas)
#Gerar apostas contendo 4 numeros pares e 2 impares que menos repetem
apostas_4_pares_2_impar_menos = [menos_repetem]
while len(apostas_4_pares_2_impar_menos) < quantidade_apostas:
    numeros_par = random.sample(range(2, 61, 2), 4)
    numeros_impar = random.sample(range(1, 61, 2), 2)
    novas_apostas = numeros_par + numeros_impar
    if novas_apostas not in base_mega_sena and novas_apostas not in apostas_4_pares_2_impar_menos:
        apostas_4_pares_2_impar_menos.append(novas_apostas)       

#Gerar apostas contendo 4 numeros impares e 2 pares que mais repetem
apostas_4_impar_2_par_mais = [mais_repetem]
while len(apostas_4_impar_2_par_mais) < quantidade_apostas:
    numeros_impar = random.sample(range(1, 61, 2), 4)
    numeros_par = random.sample(range(2, 61, 2), 2)
    novas_apostas = numeros_impar + numeros_par
    if novas_apostas not in base_mega_sena and novas_apostas not in apostas_4_impar_2_par_mais:
        apostas_4_impar_2_par_mais.append(novas_apostas)
#Gerar apostas contendo 4 numeros impares e 2 pares que menos repetem
apostas_4_impar_2_par_menos = [menos_repetem]
while len(apostas_4_impar_2_par_menos) < quantidade_apostas:
    numeros_impar = random.sample(range(1, 61, 2), 4)
    numeros_par = random.sample(range(2, 61, 2), 2)
    novas_apostas = numeros_impar + numeros_par
    if novas_apostas not in base_mega_sena and novas_apostas not in apostas_4_impar_2_par_menos:
        apostas_4_impar_2_par_menos.append(novas_apostas)

#Gerar apostas contendo 3 impares e 3 pares que mais repetem
apostas_3_impar_3_par_mais = [mais_repetem]
while len(apostas_3_impar_3_par_mais) < quantidade_apostas:
    numeros_impar = random.sample(range(1, 61, 2), 3)
    numeros_par = random.sample(range(2, 61, 2), 3)
    novas_apostas = numeros_impar + numeros_par
    if novas_apostas not in base_mega_sena and novas_apostas not in apostas_3_impar_3_par_mais:
        apostas_3_impar_3_par_mais.append(novas_apostas)

#Gerar apostas contendo 3 impares e 3 pares que menos repetem
apostas_3_impar_3_par_menos = [menos_repetem]
while len(apostas_3_impar_3_par_menos) < quantidade_apostas:
    numeros_impar = random.sample(range(1, 61, 2), 3)
    numeros_par = random.sample(range(2, 61, 2), 3)
    novas_apostas = numeros_impar + numeros_par
    if novas_apostas not in base_mega_sena and novas_apostas not in apostas_3_impar_3_par_menos:
        apostas_3_impar_3_par_menos.append(novas_apostas)

#Gerar apostas apenas com numeros par que mais repetem
apostas_apenas_par_mais = [mais_repetem]
while len(apostas_apenas_par_mais) < quantidade_apostas:
    numeros_par = random.sample(range(2, 61, 2), 6)
    novas_apostas = numeros_par
    if novas_apostas not in base_mega_sena and novas_apostas not in apostas_apenas_par_mais:
        apostas_apenas_par_mais.append(novas_apostas)
#Gerar apostas apenas com numeros par que menos repetem
apostas_apenas_par_menos = [menos_repetem]
while len(apostas_apenas_par_menos) < quantidade_apostas:
    numeros_par = random.sample(range(2, 61, 2), 6)
    novas_apostas = numeros_par
    if novas_apostas not in base_mega_sena and novas_apostas not in apostas_apenas_par_menos:
        apostas_apenas_par_menos.append(novas_apostas)

#Gerar apostas apenas com numeros impar que mais repetem
apostas_apenas_impar_mais = [mais_repetem]
while len(apostas_apenas_impar_mais) < quantidade_apostas:
    numeros_impar = random.sample(range(1, 61, 2), 6)
    novas_apostas = numeros_impar
    if novas_apostas not in base_mega_sena and novas_apostas not in apostas_apenas_impar_mais:
        apostas_apenas_impar_mais.append(novas_apostas)
#Gerar apostas apenas com numeros impar que menos repetem
apostas_apenas_impar_menos = [menos_repetem]
while len(apostas_apenas_impar_menos) < quantidade_apostas:
    numeros_impar = random.sample(range(1, 61, 2), 6)
    novas_apostas = numeros_impar
    if novas_apostas not in base_mega_sena and novas_apostas not in apostas_apenas_impar_menos:
        apostas_apenas_impar_menos.append(novas_apostas)

aposta_nao_repete = [nao_repetem]
while len(aposta_nao_repete) < quantidade_apostas:
    numeros_impar = random.sample(range(1, 61, 2), 6)
    if novas_apostas not in base_mega_sena and novas_apostas not in aposta_nao_repete:
        aposta_nao_repete.append(novas_apostas)
#Printa os numeros identificados como mais repetidos, menos repetidos e que não se repetem

mais_repetem = encontrar_numeros_mais_repetem(base_mega_sena, quantidade_numeros)
print(f"Os {quantidade_numeros} números que mais se repetem são: {mais_repetem}")

menos_repetem = encontrar_numeros_mais_repetem(base_mega_sena, quantidade_numeros)
print(f"Os {quantidade_numeros} números que menos se repetem são: {menos_repetem}")

nao_repetem = encontrar_numeros_nao_repetem(base_mega_sena)
print(f"Os {quantidade_numeros} números que não se repetem são: {nao_repetem}")

#Printa as apostas
print(f"\n\n{quantidade_apostas+1} - Apostas com 4 números pares e 2 ímpares:\n")
for vector in apostas_4_pares_2_impar_mais:
    print(vector)
for vector in apostas_4_pares_2_impar_menos:
    print(vector)

print(f"\n{quantidade_apostas+1} - Apostas com 4 números ímpares e 2 pares:\n")
for vector in apostas_4_impar_2_par_mais:
    print(vector)
for vector in apostas_4_impar_2_par_menos:
    print(vector)

print(f"\n{quantidade_apostas+1} - Apostas com 3 números ímpares e 3 pares:\n")
for vector in apostas_3_impar_3_par_mais:
    print(vector)
for vector in apostas_3_impar_3_par_menos:
    print(vector)

print(f"\n{quantidade_apostas+1} - Apostas com apenas números pares:\n")
for vector in apostas_apenas_par_mais:
    print(vector)
for vector in apostas_apenas_par_menos:
    print(vector)

print(f"\n{quantidade_apostas+1} - Apostas com apenas números ímpares:\n")
for vector in apostas_apenas_impar_mais:
    print(vector)
for vector in apostas_apenas_impar_menos:
    print(vector)

print(f"\n{quantidade_apostas+1} - Apostas com apenas números que não repetem:\n")
for vector in aposta_nao_repete:
    print(vector)

print("\n")