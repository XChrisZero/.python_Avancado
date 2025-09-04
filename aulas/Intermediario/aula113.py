# reduce - faz a redução de um iterável em um valor
from functools import reduce

# Imagine que você tem uma lista de produtos e quer saber o total da compra
produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

# Como funciona o reduce sem usar o reduce
# def funcao_do_reduce(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     print()
#     return acumulador + produto['preco']


# Usando o reduce e uma função lambda
total = reduce( 
    lambda acumulador, produto: acumulador + produto['preco'], # funcao_do_reduce,
    produtos,
    0 # valor inicial do acumulador
)

print('Total é', total)


# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

# print(sum([p['preco'] for p in produtos]))