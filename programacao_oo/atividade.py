class Atividade:

    def __init__(self, descricao, nota_maxima=10.0):
        self.descricao = descricao
        self.nota_maxima = nota_maxima

    def __str__(self):
        return f"A atividade {self.descricao} tem a nota maxima {self.nota_maxima}"