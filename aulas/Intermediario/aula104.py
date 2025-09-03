# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def criar_funcao(func): # Função decoradora
    def interna(*args, **kwargs): # Função interna
        print('Vou te decorar')
        for arg in args: # Checa todos os argumentos
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna 


@criar_funcao # Sintaxe açúcar para: inverte_string = criar_funcao(inverte_string)
def inverte_string(string): # Função a ser decorada
    print(f'{inverte_string.__name__}') # Mostra o nome da função que após a decoração será "interna"
    return string[::-1] # Inverte a string


def e_string(param): # Função que checa se o parâmetro é uma string
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('123') # Chama a função decorada
print(invertida)