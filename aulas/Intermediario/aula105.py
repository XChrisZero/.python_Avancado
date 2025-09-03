# Decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None): # Parâmetros do decorador
    def fabrica_de_funcoes(func): # Função decoradora
        print('Decoradora 1')

        def aninhada(*args, **kwargs): # Parâmetros da função decorada
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res 
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3) # Parâmetros do decorador
def soma(x, y): # Parâmetros da função decorada
    return x + y


decoradora = fabrica_de_decoradores() # Sem parâmetros do decorador
multiplica = decoradora(lambda x, y: x * y) # Sem parâmetros da função decorada

dez_mais_cinco = soma(10, 5) # Parâmetros da função decorada
dez_vezes_cinco = multiplica(10, 5) # Parâmetros da função decorada
print(dez_mais_cinco)
print(dez_vezes_cinco)