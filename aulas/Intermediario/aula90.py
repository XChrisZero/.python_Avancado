import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__'] # iterable é um objeto que pode ser iterado
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)] # lista é um objeto que contém todos os elementos de uma vez
generator = (n for n in range(1000000)) # generator é um objeto que gera os elementos sob demanda

print(sys.getsizeof(lista)) # lista ocupa mais memória porque é uma lista completa
print(sys.getsizeof(generator)) # generator ocupa menos memória porque é gerado sob demanda

print(generator) # generator é um objeto que pode ser iterado, mas não é uma lista completa

# for n in generator:
#     print(n)

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.nome):
            result = self.nome[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration