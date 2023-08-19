#Objeto Estacionamento
class Estacionamento:
    
    def __init__ (self,nome="Catatau",qtde_vagas=2):
        self.nome = nome
        self.qtde_vagas = qtde_vagas
        self.qtde_vagas_disponiveis = qtde_vagas
        self.vagas = []
        self.abrir_estacionamento()

    def abrir_estacionamento(self):
         for numero in range(1, self.qtde_vagas +1):
              vaga_disponivel = Vaga(numero)
              self.vagas.append(vaga_disponivel) #puxa informação do objeto Vaga e add se a vaga está ocupada

    def imprimir_vagas(self):
         for vaga in self.vagas:
              print(vaga)
    
    def estacionar(self, veiculo):
         for indice, vaga in enumerate(self.vagas):
              if vaga.ocupado == False:
                    vaga.ocupado = True
                    vaga.veiculo = veiculo
                    self.qtde_vagas_disponiveis -= 1
                    return self.vagas[indice]

    def __str__(self):
         return (f"Estacionamento {self.nome}. \nQuantidade de vagas: {self.qtde_vagas} \nVagas Disponiveis {self.qtde_vagas_disponiveis}\n")


#Objeto Vaga
class Vaga:
    
    def __init__(self, numero, ocupado=False, veiculo=None):
        self.numero = numero 
        self.ocupado = ocupado
        self.veiculo = veiculo
    
    
    def __str__(self):
         return (f"Numero: {self.numero}, ocupado: {self.ocupado}, {self.veiculo}")



#objeto Veículo
class Veiculo:

    def __init__ (self,placa,modelo):
        self.placa = placa
        self.modelo = modelo 

    def __str__(self):
            return f"Carro: {self.modelo}, placa: {self.placa}"
        
