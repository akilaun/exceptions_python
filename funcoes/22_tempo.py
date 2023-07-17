#Definindo Função
def calcular_tempo(dias, horas, minutos, segundo):
    dias_para_segundos = (dias * 24)*3600
    horas_para_segundos = horas* 3600
    minutos_para_segundos = minutos * 60 
    total_em_segundos = dias_para_segundos+horas_para_segundos+minutos_para_segundos+segundos
    return total_em_segundos

#Inserindo Dados
dias = int(input("Insira os dia(s): "))
horas = int(input("Insira as hora(s): "))
minutos = int(input("Insira os minuto(s): "))
segundos = int(input("Insira os segundo(s): "))

calculo = calcular_tempo(dias, horas, minutos, segundos)

#Printando dados na tela
print(f"\nDIA(S):{dias}\n"
      f"HORA(S):{horas}\n"
      f"MINUTO(S):{minutos}\n"
      f"SEGUNDO(S):{segundos}\n"
      f"\nO total em segundo é:{calculo}\n"
)