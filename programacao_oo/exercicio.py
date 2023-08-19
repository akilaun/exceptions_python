class Estacionamento:
    
    def __init__ (self,nome,qtde_vagas):
        self.nome = nome
        self.qtde_vagas = qtde_vagas
        qtde_vagas = 5

    def __str__(self):
        return  f"Nome {self.nome}, "\
                f"Nome {self.qtde_vagas}, " \

class Veiculo:

    def __init__ (self,placa,modelo):
        self.placa = placa
        self.modelo = modelo
        
