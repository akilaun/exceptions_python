"""
Exemplo de criação de arquivo com Python

MODO        OPERAÇÃO

r           Leitura
w           Escrita
a           Escrita, mas preserva o conteudo

"""

nome_arquivo = "numeros.txt"
arquivo = open(nome_arquivo, "w")


for numero in range(1, 101 ):
    num = f"{str(numero)}\n"
    print = arquivo.write(num)
    

arquivo.close()