# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html
from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values): # aceita um ou mais valores
        print('adicionando um único elemento ao final de uma lista existente...', values)
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int: # retorna o tamanho da lista
        print('comprimento da lista')
        return self._index

    def __getitem__(self, index): # retorna o item na posição index
        print('GET ITEM:', index)
        return self._data[index]

    def __setitem__(self, index, value): # define o item na posição index
        print('SET ITEM:', index, value)
        self._data[index] = value

    def __iter__(self): # retorna o iterador (ele mesmo)
        print('ITERANDO...')    
        return self

    def __next__(self): # retorna o próximo valor
        print('NEXT...')
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value

# Testando a classe MyList
if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria', 'Helena')
    lista[0] = 'João'
    lista.append('Luiz')
    # print(lista[0])
    # print(len(lista))
    for item in lista:
        print(item)
    print('---')
    for item in lista:
        print(item)
    print('---')