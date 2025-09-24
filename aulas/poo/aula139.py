# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno


# string = MinhaString('Luiz')
# print(string.upper())
 
class A(object): # Herda de object (padrão  do Python)
    atributo_a = 'valor a'

    def __init__(self, atributo): # Construtor
        self.atributo = atributo

    def metodo(self): # Método
        print('A')


class B(A): # Herda de A
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa): # Construtor
        super().__init__(atributo) # super() sem parâmetros chama a super classe imediata (A)
        self.outra_coisa = outra_coisa

    def metodo(self): # Método
        print('B')


class C(B): # Herda de B
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs): # Construtor
        # print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs) # super() sem parâmetros chama a super classe imediata (B)

    def metodo(self): # Método
        # super().metodo()  # B
        # super(B, self).metodo()  # A
        # super(A, self).metodo()  # object
        A.metodo(self)
        B.metodo(self)
        print('C')


# print(C.mro())
# print(B.mro())
# print(A.mro())
c = C('Atributo', 'Qualquer')
# print(c.atributo)
# print(c.outra_coisa)
c.metodo()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()