import pandas as pd
import json 
from random import randint #biblioteca que gera aleatoriamente numeros inteiros

temperaturas = { }
total = ( 43200 * 12 ) + 1

for dia in range( 1,31 ): # || percorre por todas as linhas ----- e coloca um indice com os numeros do 1 ao 30
    chave = "dia_" + str( dia ) # a variavel chave recebe o valor string "dia_" e concatena com o simbolo "+" o valor da variavel dia que foi escrita nas linhas 1 a 30, resultado = dia_1, dia_2, dia_3, ..., dia_30
    temperaturas[ chave ] = [ ] #temperatura é uma biblioteca e recebera uma lista [vetor] com os valores de chave
    for periodo in range ( 1, total ): # || percorre as 30 linhas e adicionará o valor de 1 até a o valor da varialve "total"
        valor_temp = randint( 5, 38 )
        temperaturas[ chave ].append( valor_temp )
    print( chave )

tabela = pd.DataFrame( temperaturas )
tabela.to_csv( "bibliotecas/temperaturas.csv" )


#print( json.dumps( temperaturas, sort_keys=False, indent=4 ) )





