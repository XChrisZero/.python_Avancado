# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.
class Carro: # Classe
    def __init__(self, nome): # Construtor
        self.nome = nome # Atributo

    def acelerar(self): # Método
        print(f'{self.nome} está acelerando...') # Ação


fusca = Carro('Fusca') # Instância
fusca.acelerar() # Método
Carro.acelerar(fusca) # Passando a instância como parâmetro
# print(fusca.nome)
# fusca.acelerar()

celta = Carro(nome='Celta') # Instância
celta.acelerar() # Método
Carro.acelerar(celta) # Passando a instância como parâmetro
# print(celta.nome)