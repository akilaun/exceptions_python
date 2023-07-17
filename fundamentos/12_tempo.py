dias = int(input("Insira os dia: "))
horas = int(input("Insira as horas: "))
minutos = int(input("Insira os minutos: "))
segundos = int(input("Insira os segundos: "))

result = (((dias * 24) *3600) + (horas * 3600) + (minutos * 60) + segundos)

print(f"\nDIA(S):{dias}\n"
      f"HORA(S):{horas}\n"
      f"MINUTO(S):{minutos}\n"
      f"SEGUNDO(S):{segundos}\n"
      f"\nO total em segundo é:{result}")