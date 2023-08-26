import csv

class EscritorCsv:
    #Aqui eu estou criando uma classe que criara um csv dando nome ao arquivo, registrando o cabeçalho e os dados abaixo do cabeçalho
    def __init__ (self, nome_arq, cabecalho, dados):
        self.nome_arq = nome_arq #salvar o nome do arquivo
        self.cabecalho = cabecalho #escrever no cabeçalho
        self.dados = dados #escrever dados

    
    def converterDicemList(self):
        lista = []
        for info in self.dados:
            dia_semana = info.get("dia")
            temperatura = info.get("temperatura")
            linha = [dia_semana, temperatura]
            lista.append(linha)
        
        return lista

    def escrever(self):

        p_linha = self.dados[0]
        if isinstance(p_linha, dict):
            dados = self.converterDicemList()
            self.salvar(dados)
            print("É um dicionario.")
        elif isinstance(p_linha, list):
            self.salvar(self.dados)
            print("É uma lista.")

    def salvar(self, dados):
        with open(self.nome_arq, "w", encoding="UTF8", newline="") as arq:
            wrt = csv.writer(arq)
            wrt.writerow(self.cabecalho)
            wrt.writerows(dados)