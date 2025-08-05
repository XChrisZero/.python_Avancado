#EXERCICIO!
#Crie funcoes que duplicam, triplica e quadruplicam um numero recebido com parametro.
def criar_multiplic( multiplicador ): #funcao que cria outras funcoes
    def multiplicar( num ):
        return num * multiplicador
    return multiplicar

duplicar = criar_multiplic(2) #criando a variavel duplicar que recebe a funcao criar_multiplic
triplicar = criar_multiplic(3) #criando a variavel triplicar que recebe a funcao criar_multiplic
quadruplicar = criar_multiplic(4) #criando a variavel quadruplicar que recebe a funcao criar_multiplic

print ( duplicar(2) )
print ( triplicar(2) )
print ( quadruplicar(2) )

