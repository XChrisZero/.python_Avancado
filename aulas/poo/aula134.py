# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.
class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property # getter
    def ferramenta(self): 
        return self._ferramenta

    @ferramenta.setter # setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever: # classe
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):# método
        return f'{self.nome} está escrevendo' 


escritor = Escritor('Luiz') # associação
caneta = FerramentaDeEscrever('Caneta Bic')  # associação
maquina_de_escrever = FerramentaDeEscrever('Máquina') # associação
escritor.ferramenta = maquina_de_escrever # associação

print(caneta.escrever()) # associação
print(maquina_de_escrever.escrever()) # associação
print(escritor.ferramenta.escrever()) # associação