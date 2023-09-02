import pandas as pd

tabela = pd.read_csv( "bibliotecas/temperaturas.csv" )

print( f"Informações com head \n{tabela.head}\n" )
print( f"Informações com tail \n{tabela.tail(50)}")
print( f"Informações com describe \n{tabela.describe()}")
