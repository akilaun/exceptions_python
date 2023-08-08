import csv
import random

base_vectors = []

with open('resultados_mega_sena.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        try:
            vector = [int(num) for num in row]
            base_vectors.append(vector)
        except ValueError:
            print("Erro ao ler vetor:", row)

vectors_4_even_2_odd = []

while len(vectors_4_even_2_odd) < 6:
    even_numbers = random.sample(range(2, 61, 2), 4)
    odd_numbers = random.sample(range(1, 61, 2), 2)
    new_vector = even_numbers + odd_numbers
    if new_vector not in base_vectors and new_vector not in vectors_4_even_2_odd:
        vectors_4_even_2_odd.append(new_vector)
vectors_4_odd_2_even = []

while len(vectors_4_odd_2_even) < 6:
    odd_numbers = random.sample(range(1, 61, 2), 4)
    even_numbers = random.sample(range(2, 61, 2), 2)
    new_vector = odd_numbers + even_numbers
    if new_vector not in base_vectors and new_vector not in vectors_4_odd_2_even:
        vectors_4_odd_2_even.append(new_vector)
vectors_3_odd_3_even = []

while len(vectors_3_odd_3_even) < 6:
    odd_numbers = random.sample(range(1, 61, 2), 3)
    even_numbers = random.sample(range(2, 61, 2), 3)
    new_vector = odd_numbers + even_numbers
    if new_vector not in base_vectors and new_vector not in vectors_3_odd_3_even:
        vectors_3_odd_3_even.append(new_vector)
vectors_only_even = []

while len(vectors_only_even) < 6:
    even_numbers = random.sample(range(2, 61, 2), 6)
    new_vector = even_numbers
    if new_vector not in base_vectors and new_vector not in vectors_only_even:
        vectors_only_even.append(new_vector)
vectors_only_odd = []

while len(vectors_only_odd) < 6:
    odd_numbers = random.sample(range(1, 61, 2), 6)
    new_vector = odd_numbers
    if new_vector not in base_vectors and new_vector not in vectors_only_odd:
        vectors_only_odd.append(new_vector)

print("\n\n6 - Apostas com 4 números pares e 2 ímpares:\n")
for vector in vectors_4_even_2_odd:
    print(vector)

print("\n6 - Apostas com 4 números ímpares e 2 pares:\n")
for vector in vectors_4_odd_2_even:
    print(vector)

print("\n6 - Apostas com 3 números ímpares e 3 pares:\n")
for vector in vectors_3_odd_3_even:
    print(vector)

print("\n6 - Apostas com apenas números pares:\n")
for vector in vectors_only_even:
    print(vector)

print("\n6 - Apostas com apenas números ímpares:\n")
for vector in vectors_only_odd:
    print(vector)

print("\n\n")
