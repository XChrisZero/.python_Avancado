"""
Retorno de valores das funções (return), E a cada escopo de função ela deve ser a ultima coisa a ser executada. após fechar o escopo da função, podera chamar outro return, mas não dentro do escopo da função.
"""


def soma(x, y):
    if x > 10:
        return [10, 20] # Retorna uma lista se x for maior que 10
    return x + y # Retorna a soma de x e y se x não for maior que 10
    # return x + y # Retorna a soma de x e y 

# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(11, 55))