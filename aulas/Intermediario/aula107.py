# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')
from exercicios.exercicio_107 import list1, list2, zipping
import itertools

print(list1)
print(list2)
print(zipping(list1, list2))

print(list(zip(list1, list2)))# Função nativa do Python que faz a mesma coisa

print(list(itertools.zip_longest(list1, list2)))  # Une as listas, mas preenche com None os valores faltantes
print(list(itertools.zip_longest(list1, list2, fillvalue='Vazio')))  # Une as listas, mas preenche com 'Vazio' os valores faltantes
