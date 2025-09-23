# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Cliente:
    def __init__(self, nome): # Classe Cliente
        self.nome = nome 
        self.enderecos = []

    def inserir_endereco(self, rua, numero): # Composição
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco): # Agregação
        self.enderecos.append(endereco)

    def listar_enderecos(self): # Lista todos os endereços
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self): # Apaga o cliente e todos os endereços
        print('APAGANDO,', self.nome) 


class Endereco: # Classe Endereco não faz sentido existir
    def __init__(self, rua, numero): # sozinha
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente('Maria') # Cliente "tem um" ou "possui um" Endereço
cliente1.inserir_endereco('Av Brasil', 54) # Composição
cliente1.inserir_endereco('Rua B', 6745) # Composição
endereco_externo = Endereco('Av Saudade', 123213) # Associação
cliente1.inserir_endereco_externo(endereco_externo) # Agregação
cliente1.listar_enderecos() # Av Brasil 54

del cliente1 # Apaga o cliente1 e todos os endereços
# Mas o endereço_externo não é apagado, pois não
# foi criado dentro da classe Cliente


print(endereco_externo.rua, endereco_externo.numero)
print('######################## AQUI TERMINA MEU CÓDIGO')