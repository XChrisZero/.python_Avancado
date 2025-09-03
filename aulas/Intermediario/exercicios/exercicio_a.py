"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]

lista_soma1 = [x + y for x, y in zip(lista_a, lista_b)] # Usando list comprehension


lista_soma2 = [] # Usando loop for com range
for i in range(len(lista_b)):
    lista_soma2.append(lista_a[i] + lista_b[i])


lista_soma3 = [] # Usando loop for com enumerate
for i, _ in enumerate(lista_b): # _ é usado quando não precisamos do valor, apenas do índice
    lista_soma3.append(lista_a[i] + lista_b[i])
