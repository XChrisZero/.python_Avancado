# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')
pessoa = {
    'nome': 'Chris',
    'sobrenome': 'Ferrari',
    'idade': 30,
    'altura': 1.8,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
}
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])


'''
Metodos úteis dos dicionários:
.clear() - limpa o dicionário
.copy() - retorna uma cópia do dicionário
.fromkeys() - cria chaves de um dicionário
.get() - obtém uma chave
.items() - retorna as chaves e valores
.keys() - retorna as chaves
.pop() - remove um item
.popitem() - remove o último item inserido
.update() - atualiza um dicionário
.values() - retorna os valores
.len() - tamanho do dicionário
.setdefault() - insere um valor se a chave não existir
'''
# Exemplo de uso da shalow copy e deep copy
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'c3': 3,
    'l1': [1, 2, 3],
}

d2 = d1

d2['c1'] = 1000
print(d1)
print(d2)

d2['l1'][0] = 1000 # Isso afeta d1 também porque a shallow copy copia apenas os dados de nível superior.

d3 = d1.copy() # a biblioteca copy faz uma cópia rasa (shallow copy) do dicionário. d3 = copy.copy(d1)
d3['c1'] = 5000
print(d1)
print(d3)

d4 = copy.deepcopy(d1) # Faz uma cópia profunda (deep copy) do dicionário.
d4['l1'][0] = 999 # Isso não afeta d1 porque d4 é uma cópia profunda.
print(d1)

#Exemplo do pop
p1 = {
    'nome': 'Chris',
    'sobrenome': 'Ferrari',
    'idade': 30,
}
print(p1)
print(p1.pop('nome'))  # Remove a chave 'nome' e retorna seu valor
print(p1)  # A chave 'nome' não está mais presente no dicionário
print(p1.popitem())  # Remove o último item inserido e retorna uma tupla (chave, valor)
print(p1)  # O último item foi removido do dicionário

# Exemplo do get
print(p1.get('nome'))  # Retorna None se a chave 'nome' não existir
print(p1.get('sobrenome', 'Chave não encontrada'))  # Retorna uma mensagem personalizada se a chave não existir

# Exemplo do update
p1.update({'altura': 1.8, 'cidade': 'São Paulo'})  # Adiciona novas chaves e valores
print(p1)  # O dicionário agora contém as novas chaves e valores

# Exemplo do fromkeys
novas_chaves = ['a', 'b', 'c']
d5 = dict.fromkeys(novas_chaves, 0)  # Cria um dicionário com chaves de novas_chaves e valor 0
print(d5)  # {'a': 0, 'b': 0, 'c': 0}

# Exemplo do setdefault
d5.setdefault('d', 4)  # Adiciona a chave 'd'
print(d5)  # {'a': 0, 'b': 0, 'c': 0, 'd': 4}
d5.setdefault('a', 10)  # Não altera o valor de 'a'
print(d5)  # {'a': 0, 'b': 0, 'c': 0, 'd': 4} (o valor de 'a' permanece 0)

# Exemplo do keys, values e items
print(d5.keys())   # Retorna as chaves do dicionário
print(d5.values())  # Retorna os valores do dicionário
print(d5.items())   # Retorna os pares (chave, valor) do dicionário

# Exemplo do len
print(len(d5))  # Retorna o número de chaves no dicionário

# Exemplo do clear
d5.clear()  # Limpa o dicionário
print(d5)  # O dicionário agora está vazio
# print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])
print()
for chave in pessoa:
    print(chave, pessoa[chave])
