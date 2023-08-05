"""
Analise a tabela abaixo e responda as atividades 1 e 2:

ANIMAL                   IDADE          FATOR IDADE HUMANO      IDADE DE HUMANO
Cachorro Pastor            3                    12                    ?
Cachorro Fila              4                    10                    ?
Cachorro Golden            2                    8                     ?
Papagaio                   8                    5                     ?
Gato Siamês                4                    7                     ?
Cachorro Husky             3                    9                     ?

1) Crie o arquivo 62_animais.py.
2) Utilize uma estrutura de dados para representar a tabela acima.
3) Utilize a estrutura de repetição para iterar sobre os elementos da tabela.
4) Calcule a idade do animal como idade de humano na última coluna.
5) Utilize a estrutura de decisão e imprima as informações do cachorro caso a idade de humano seja maior que 30 anos.
"""



animais = [
    {
    "animal": "Cachorro Pastor",
    "idade": 3,
    "fator idade humano": 12
    },
    {
    "animal": "Cachorro Fila",
    "idade": 4,
    "fator idade humano": 10
    },
    {
    "animal": "Cachorro Golden",
    "idade": 2,
    "fator idade humano": 8
    },
    {
    "animal": "Papagaio",
    "idade": 8,
    "fator idade humano": 5
    },
    {
    "animal": "Gato Siamês",
    "idade": 4,
    "fator idade humano": 7
    },
    {
    "animal": "Cachorro Husky",
    "idade": 3,
    "fator idade humano": 9
    }
]


for a in animais:
    nome = a.get("animal")
    if "Cachorro" in nome:
        idade = a.get("idade")
        fator_h = a.get("fator idade humano")
        idade_de_humano = idade * fator_h
        #if idade_de_humano >= 30:
        print(f"O {nome} tem {idade} anos e a idade de humano é igual a {idade_de_humano}")