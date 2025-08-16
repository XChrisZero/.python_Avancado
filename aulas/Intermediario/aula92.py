# Yield from
# https://docs.python.org/3/reference/expressions.html#yield-from

'''
def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    print('Gerador gen1 finalizado')

def gen2():
    print('COMECOU GEN2')
    yield from gen1()  # chama o gerador gen1 e retorna seus valores
    yield 3
    yield 4 
    print('Gerador gen2 finalizado')

def gen3(gen=None):
    print('COMECOU GEN3')
    yield from gen2()  # chama o gerador gen2 e retorna seus valores
    yield 5
    yield 6
    print('ACABOU GEN3')

g1 = gen3(gen1()) #pode passar um gerador como parâmetro
g2 = gen3(gen2())  # ou não passar nada, o que chama gen2 sem parâmetros
for numero in g:
    print(numero)


'''


def gen1(): 
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()