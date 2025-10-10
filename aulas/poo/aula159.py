# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, field, asdict, astuple
#field - usado para criar campos com mais detalhes


#@dataclass(init=False) # detalhes para editar o comportamento do dataclass
@dataclass() #as dataclasses criam o init, repr, eq, entre outros e não são mutáveis por padrão
class Pessoa: 

    nome: str = field(
        default='MISSING', repr=False
    )
    sobrenome: str = 'Not sent'
    idade: int = 100
    enderecos: list[str] = field(default_factory=list) # default_factory para tipos mutáveis


   # def __init__(self, nome, sobrenome): # se init=False, precisa criar o init manualmente
   #     self.nome = nome
   #     self.sobrenome = sobrenome
   #     self.nome_completo = f'{self.nome} {self.sobrenome}'

    def __post_init__(self): # se init=False, pode criar o post_init manualmente
        print('POST INIT') # executa após o init

    @property # transforma o método em um atributo
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)

 #
if __name__ == '__main__': # apenas para testar o módulo
    p1 = Pessoa('Luiz', 'Otávio')
    print(p1)
    print(p1.nome_completo)
    lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
    ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
    print(ordenadas)