"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append( 'Chris' )
contador = 0

indices = range( len( lista ) )

for nomes in lista:
    print ( nomes )
    contador += 1
    for indice in indices:
        print (f' está na posição {contador} na lista')
        
