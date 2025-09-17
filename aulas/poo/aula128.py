# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade): # método construtor
        self.nome = nome # atributo de instância
        self.idade = idade # atributo de instância

    @classmethod # método de classe
    def metodo_de_classe(cls): # cls é a própria classe
        print('Hey')

    @classmethod # factory
    def criar_com_50_anos(cls, nome): 
        return cls(nome, 50) # retorna uma instância de Pessoa com 50 anos

    @classmethod # factory
    def criar_sem_nome(cls, idade): # retorna uma instância de Pessoa anônima
        return cls('Anônima', idade)

# Testes
p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena') # factory
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25) # factory
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()