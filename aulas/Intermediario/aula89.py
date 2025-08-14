# dir, hasattr e getattr
# Esses são três métodos muito úteis em Python para trabalhar com objetos e suas propriedades.
# dir: lista os atributos e métodos de um objeto
# hasattr: verifica se um objeto tem um determinado atributo ou método
# getattr: obtém o valor de um atributo ou chama um método de um objeto


string = 'Luiz' # string é um objeto do tipo str
metodo = 'strip'# método que remove espaços em branco no início e no final da string

if hasattr(string, metodo): # verifica se o objeto string tem o método especificado
    print('Existe upper') # verifica se o método existe
    print(getattr(string, metodo)()) # chama o método usando getattr
else: # se o método não existe
    print('Não existe o método', metodo) # informa que o método não existe

# Exemplo de uso de dir para listar os atributos e métodos de um objeto
print(dir(string))  # lista todos os atributos e métodos do objeto string

# Exemplo de uso de hasattr para verificar a existência de um atributo ou método
if hasattr(string, 'lower'):
    print('O método lower existe na string')  # verifica se o método 'lower' existe
else:
    print('O método lower não existe na string')

# Exemplo de uso de getattr para acessar um atributo ou método
metodo = 'upper'  # método que converte a string para maiúsculas
if hasattr(string, metodo):
    resultado = getattr(string, metodo)()  # chama o método 'upper' se existir
    print('Resultado do método upper:', resultado)  # imprime o resultado
else:
    print('O método', metodo, 'não existe na string')

# Exemplo de uso de dir, hasattr e getattr com uma lista
lista = [1, 2, 3, 4, 5]  # lista é um objeto do tipo list
if hasattr(lista, 'append'):  # verifica se a lista tem o método 'append'
    print('O método append existe na lista')  # informa que o método existe
    getattr(lista, 'append')(6)  # chama o método 'append' para adicionar o número 6
    print('Lista após append:', lista)  # imprime a lista atualizada
else:
    print('O método append não existe na lista')

# Exemplo de uso de dir, hasattr e getattr com um dicionário
dicionario = {'a': 1, 'b': 2}  # dicionário é um objeto do tipo dict
if hasattr(dicionario, 'get'):  # verifica se o dicionário tem o
    print('O método get existe no dicionário')  # informa que o método existe
    valor = getattr(dicionario, 'get')('a')  # chama o método 'get' para obter o valor da chave 'a'
    print('Valor da chave "a":', valor)  # imprime o valor obtido
else:
    print('O método get não existe no dicionário')

# Exemplo de uso de dir, hasattr e getattr com um objeto personalizado
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return f'{self.nome} está falando.'
    
