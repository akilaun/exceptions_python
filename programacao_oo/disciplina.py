class Disciplina:

    def __init__(self, nome, termo):
        self.nome = nome
        self.termo = termo
        self.aprovada = False
        self.curso = ""
    
    def aprovar(self):
        self.aprovada = True
    
    def atribuir_curso(self, nome_curso):
        self.curso = nome_curso

