"""
1) Escreve um programa que pergunte a velocidade do carro, caso ultrapasse 80km/h mostre uma mensagem dizendo que o motorista foi multado. 
Nesse caso mostrar o valor da multa cobrando R$ 5,00 por km acima de 80 km/h.
"""

limite_de_velocidade = 80
multa = 5
velocidade = int(input("Qual a sua velocidade?: "))

if velocidade <= 80:
    print("Parabens por obedecer as leis de transito!")
else:
    multa = (velocidade - limite_de_velocidade) * multa
    print(
        "\nVocê foi multado por ultrapassar o limite de velocidade!"
        f"\nO valor da multa é de: R${multa:.2f}"
          )
