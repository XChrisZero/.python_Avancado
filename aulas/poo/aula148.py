# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A: # object
    def __new__(cls, *args, **kwargs): # sempre recebe cls
        instancia = super().__new__(cls) # object.__new__(cls)
        print('Sou o new') # deve retornar a instância
        return instancia # deve retornar a instância

    def __init__(self, x): # sempre recebe self
        self.x = x # inicializa a instância
        print('Sou o init') # não deve retornar nada

    def __repr__(self):
        return 'A()'

# Testando
a = A(123) # chama __new__ e __init__
print(a) # chama __repr__
print(a.x) # atributo x da instância
print(type(a)) # tipo da instância