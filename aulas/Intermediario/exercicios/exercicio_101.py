def soma(x, y): 
    return x + y 


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def funcao_interna(y):
        return funcao(x, y)
    return funcao_interna
