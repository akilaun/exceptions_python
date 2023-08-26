nome_arquivo = "numeros.txt"
arquivo = open(nome_arquivo, "r")

for linha in arquivo.readlines():
    print(linha)

arquivo.close()