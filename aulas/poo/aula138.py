# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa) 
#   -> super class, base class, parent class 
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# Herança múltipla (não é o foco aqui)
#   -> class Filha(Classe1, Classe2)

##################################################################
# Exemplo de Herança
class Pessoa:
    cpf = '1234'

    def __init__(self, nome, sobrenome): # Construtor
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self): # Método
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa): # Cliente herda de Pessoa
    def falar_nome_classe(self):
        print('EITA, nem saí da classe CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Aluno(Pessoa): # Aluno herda de Pessoa
    ...


c1 = Cliente('Luiz', 'Otávio') # Cliente herda de Pessoa
c1.falar_nome_classe() # Busca primeiro na classe Cliente, depois na Pessoa
a1 = Aluno('Maria', 'Helena') # Aluno herda de Pessoa
a1.falar_nome_classe() # Busca primeiro na classe Aluno, depois na Pessoa
print(a1.cpf) # Busca primeiro na classe Aluno, depois na Pessoa
# help(Cliente) # Mostra a árvore de herança
print(Cliente.mro())  # Mostra a árvore de herança
print(Aluno.mro())  # Mostra a árvore de herança

