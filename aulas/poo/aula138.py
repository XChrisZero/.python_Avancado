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
class Pessoa: # Super class
    def __init__(self, nome, sobrenome): # Construtor
        self.__nome = nome
        self.__sobrenome = sobrenome

    @property # Getter
    def nome(self):
        return self.__nome

    @property # Getter
    def sobrenome(self):
        return self.__sobrenome

    @property # Getter
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
class Cliente(Pessoa): # Sub class (herda de Pessoa)
    def __init__(self, nome, sobrenome, cliente_id):
        super().__init__(nome, sobrenome)
        self.__cliente_id = cliente_id

    @property # Getter
    def cliente_id(self): 
        return self.__cliente_id

    def exibir_informacoes(self):
        return f'ID: {self.__cliente_id}, Nome: {self.nome_completo}'
    
# Testando as classes
cliente1 = Cliente('Chris', 'Ferrari', 123) # Instância da classe Cliente
print(cliente1.exibir_informacoes()) # ID: 123, Nome: Chris Ferrari
print(cliente1.nome) # Chris
print(cliente1.sobrenome) # Ferrari
print(cliente1.cliente_id) # 123
print(cliente1.nome_completo) # Chris Ferrari

##################################################################
# Exemplo de Composição
class Endereco:
    def __init__(self, rua, cidade, estado, cep):
        self.__rua = rua
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = cep

    @property
    def rua(self):
        return self.__rua

    @property
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

    @property
    def cep(self):
        return self.__cep

    def exibir_endereco(self):
        return f'{self.__rua}, {self.__cidade} - {self.__estado}, {self.__cep}'

