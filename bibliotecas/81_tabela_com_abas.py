import pandas as pd
from random import randint 
from xlsxwriter import Workbook

temperaturas = { }
total = ( 43200 * 12 ) + 1
writer = pd.ExcelWriter("bibliotecas/temp.xlsx", engine='openpyxl')


for dia in range( 1,31 ): 
    chave = "dia_" + str( dia ) 
    temperaturas[ chave ] = [ ] 
    
    for periodo in range ( 1, total ): 
        valor_temp = randint( 5, 38 )
        temperaturas[ chave ].append( valor_temp )


meses = [ 
    "Janeiro","Fevereiro","Março","Abril"
]

for mes in meses:
    nome = mes = ".xlsx"
    with pd.ExcelWriter( "bibliotecas/temp.xlsx",
                        engine="xlsxwriter" ) as writer:
        for chave, dados in temperaturas.items( ):
            df = pd.DataFrame( { chave:dados } )
            df.to_excel( writer, sheet_name=chave, index=False )