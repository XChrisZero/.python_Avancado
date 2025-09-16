# Métodos em instâncias de classes Python
# metodo = ação = função = verbo
# atributo = dado = variável = substantivo
# Hard coded - É algo que foi escrito diretamente no código
class Carro:
    def __init__(self, nome): # método construtor
        self.nome = nome

    def acelerar(self): # método
        print(f'{self.nome} está acelerando...')


string = 'Luiz'
print(string.upper()) # upper() é um método da classe str

fusca = Carro('Fusca') # argumento posicional
print(fusca.nome) # acessei o atributo
fusca.acelerar() # chamei o método

celta = Carro(nome='Celta') # argumento nomeado
print(celta.nome) 
celta.acelerar()