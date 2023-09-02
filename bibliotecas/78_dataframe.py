from pandas import DataFrame, Series 

notas_alunos = {
    "alunos": Series( data=["aluno1","aluno2","aluno3"] ),
    "notas_p1": Series( data=[2.9, 1.2, 9.0]),
    "notas_p2": Series( data=[4.9, 2.2, 7.1]),
    "notas_p3": Series( data=[4.0, 2.9, 8.1])
}

tabela = DataFrame (notas_alunos )
print(tabela.info())
print("\n")
print(tabela.size)
print("\n")
print(tabela.memory_usage())
print("\n")
print( f"Exibindo tabela\n{tabela}\n" )

tabela_filtrada = DataFrame(notas_alunos, index=[0,2])
print( f"Exibindo tabela filtrada \n{tabela_filtrada}\n" )

tabela_coluna_filtrada = DataFrame(notas_alunos, columns=[0,2])
print( f"Exibindo tabela filtrada \n{tabela_coluna_filtrada}\n" )















