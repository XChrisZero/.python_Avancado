# Dictionary Comprehension e Set Comprehension
#Dicionários e Conjuntos
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

'''
for chave, valor in produto.items():
    print(f'{chave} = {valor}')

'''

dict1 = {
    chave: valor.upper() 
    if isinstance(valor, str) else valor # isinstance para verificar o tipo
    for chave, valor 
    in produto.items() # for para iterar sobre o dicionário
    if chave != 'categoria' # if para filtrar chaves
}
print(dict1)

list1 = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
# List comprehension para criar uma lista de tuplas
dict2 = {
    chave: valor
    for chave, valor in list1
}
print(dict2)

set1 = {2 ** i for i in range(10)} # Set comprehension para criar um conjunto com potências de 2
print(set1)
#print(set(range(10))) # Conjunto de números de 0 a 9