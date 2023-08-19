from classes import Estacionamento, Veiculo, Vaga

estacionamento = Estacionamento()
print(estacionamento)
estacionamento.imprimir_vagas()
print("----------------------------------------------------------------")


#Veículos
for _ in range(1,4):
    if estacionamento.qtde_vagas_disponiveis == 0:
        print(f"{estacionamento}Lotado.")
        break
    placa = input("Qual a placa do veiculo: ")
    modelo = input("Qual o veículo: ")
    veiculo = Veiculo(placa, modelo)
#Adicionar Veículos
    vaga_ocupada = estacionamento.estacionar(veiculo)



#Conferir Vagas
print(f"\nVaga ocupada: {vaga_ocupada}\n")
estacionamento.estacionar(veiculo)

