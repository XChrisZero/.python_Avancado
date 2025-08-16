# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))
#generator que sabe quando parar de gerar valores

'''
def generator(n=0):
    yield 1 #pausa
    print ( 'Gerando o segundo valor')
    yield 2 #pausa
    print ( 'Gerando o terceiro valor')
    return 3 # encerra a função

gen = generator()
print(next(gen)) # chama a função até o yield com o valor 1
print(next(gen)) # chama a função até o yield com o valor 2
print(next(gen)) # chama a função até o return, que encerra a função
 #print(next(gen)) # gera um erro porque a função foi encerrada

for n in gen:
    print(n)  # não imprime nada porque a função já foi encerrada
'''

def generator(n=0, maximum=10):
    while True:
        yield n # pausa a função e retorna o valor de n
        #yield serve para transformar a função em um generator
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000000)
for n in gen:
    print(n)