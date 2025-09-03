# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def criar_funcao(func): # Função decoradora
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args: # Checa todos os argumentos
            e_string(arg)
        resultado = func(*args, **kwargs) # Chama a função original
        print(f'O seu resultado foi {resultado}.') 
        print('Ok, agora você foi decorada')
        return resultado
    return interna # Retorna a função interna


def inverte_string(string): # Função a ser decorada
    return string[::-1] # Inverte a string


def e_string(param): # Função que checa se o parâmetro é uma string
    if not isinstance(param, str): #isinstance checa o tipo do parâmetro
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string) # Decora a função
invertida = inverte_string_checando_parametro('123') # Chama a função decorada
print(invertida) # Mostra a string invertida