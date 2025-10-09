import contas

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None: # Constructor
        self.nome = nome
        self.idade = idade
    
    @property # Getter
    def nome(self) -> str:
        return self._nome
    
    @nome.setter # Setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    
    @property # Getter
    def idade(self) -> int:
        return self._idade
    
    @idade.setter # Setter
    def idade( self, idade: int ):
        if idade < 0:
            raise ValueError('Idade não pode ser negativa')
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'nome={self.nome!r}, idade={self.idade!r}'
        return f'{class_name!r}({attrs})'


    
class Cliente(Pessoa): # Inheritance
    def __init__( self, nome: str, idade: int ) -> None:
        super().__init__(nome, idade)
        self.conta: contas.ContaCorrente | contas.ContaPoupanca | None = None # Aggregation  



#Test person
if __name__ == '__main__':
    
    c1 = Cliente('Maria', 22)
    c1.conta = contas.ContaCorrente(123, 321, 0, 5000)
    class_c = type(c1).__name__
    print(f'{class_c} criada com sucesso!')
    print(c1.nome, c1.idade, c1.conta)

    c2 = Cliente('Chris', 30)
    c2.conta = contas.ContaPoupanca(123, 321, 0)
    class_c = type(c2).__name__
    print(f'{class_c} criada com sucesso!')
    print(c2.nome, c2.idade, c2.conta)