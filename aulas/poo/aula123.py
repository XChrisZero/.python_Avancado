# Escopo da classe e de métodos da classe
class Animal:
    # nome = 'Leão'

    def __init__(self, nome): # Construtor
        self.nome = nome # Atributo

        variavel = 'valor' # Escopo do construtor
        print(variavel) # Acessível

    def comendo(self, alimento): # Método
        return f'{self.nome} está comando {alimento}' # Ação

    def executar(self, *args, **kwargs): # Método
        return self.comendo(*args, **kwargs) # Ação


leao = Animal(nome='Leão') # Instância
print(leao.nome) # Atributo
print(leao.executar('maçã')) # Método
# print(leao.variavel) # Erro, escopo do construtor