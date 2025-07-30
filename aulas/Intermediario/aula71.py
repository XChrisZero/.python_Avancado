"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args): # Define a função soma que aceita um número variável de argumentos
    total = 0
    for numero in args: # Itera sobre cada número em args
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros) # Desempacota a tupla numeros e passa seus elementos como argumentos para a função soma
print(outra_soma)

print(sum(numeros)) # Usando a função sum para somar os elementos da tupla numeros
# print(*numeros)