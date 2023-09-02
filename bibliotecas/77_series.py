import pandas as pd

notas = [ 3.9, 2.0, 1.3, 7.8, 9.5 ]


serie = pd.Series( data=notas )

estatistica = serie.describe()
print( f"1- A informação da serie é\n{serie}\n" )
print( f"1- Estatisticas da serie é\n{estatistica}\n" )
print((estatistica.get('25%')))


serie_index = pd.Series( data=notas,
                        index=[10,11,12,13,14] )


print( f"2- A informação da serie é\n{serie_index}\n" )


notas_alunos = {
    "aluno01": 6.0,
    "aluno02": 9.3,
    "aluno03": 2.9,
    "aluno04": 5.9
}

print( f"3- A informação da serie é\n{notas_alunos}\n" )



serie_nomeada = pd.Series( data=["gol","palio","uno"],
                          name="Carros" )

print( f"4- A informação da serie é\n{serie_nomeada}\n" )