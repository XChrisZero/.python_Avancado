# groupby - agrupando valores (itertools)
from itertools import groupby

# lista de dicionários
alunos = [ 
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# função que retorna a chave de agrupamento
def ordena(aluno): 
    return aluno['nota'] # chave de ordenação e agrupamento


alunos_agrupados = sorted(alunos, key=ordena) # ordena a lista pela chave de agrupamento
grupos = groupby(alunos_agrupados, key=ordena) # agrupa os dados pela chave

# imprime os grupos
for chave, grupo in grupos:
    print(chave)
    for aluno in grupo: # grupo é um iterador
        print(aluno) 
