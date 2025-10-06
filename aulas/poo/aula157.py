# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
import enum

# Exemplo de Enum simples
def mover(direcao):
    print(f'Movendo para {direcao}')
# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

# Usando Enum sem type annotations
mover('esquerda')
mover('direita')
mover('acima')
mover('abaixo')
class Direcoes(enum.Enum):
    ESQUERDA = enum.auto() # auto() gera valores automaticamente
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()

# Acessando os dados do Enum
print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA) # formas de retorno
print()# para retornar o nome
print(Direcoes(1).name, Direcoes['ESQUERDA'].name, Direcoes.ESQUERDA.name)
print()
print(Direcoes.ESQUERDA.value, Direcoes.DIREITA.value) # para retornar o valor

# Usando Enum com type annotations
def mover(direcao: Direcoes): # os : indicam type annotations que adicionam
    # uma verificação de tipo na variável
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')

# Testando a função mover com Enum
mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)