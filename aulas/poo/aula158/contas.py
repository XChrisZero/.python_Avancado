import abc

#Class Abstract
class Conta(abc.ABC): 
    #Constructor
    def __init__( self, agencia: int, conta: int, saldo: float =0 ) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
 
    @abc.abstractmethod 
    def sacar( self, valor: float ) -> float: # Abstract method
        self.saldo -= valor
        self.detalhes(f'Saque de {valor} realizado com sucesso!!!')
        pass

    def depositar( self, valor: float ) -> float: # Concrete method
       self.saldo += valor
       self.detalhes( f'Depósito de {valor} realizado com sucesso!!!' )
       return self.saldo

    def detalhes( self, msg: str ='' ) -> None:
        print( f'Agência: {self.agencia} Conta: {self.conta}' )
        print( msg )
        print( f'O seu saldo é:{self.saldo:.2f}R$' )
        print( '----------------------------------------' )

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'agencia:{self.agencia!r}, conta:{self.conta!r},'\
            f' saldo:{self.saldo!r}'
        return f'{class_name!r} criada com sucesso! \n({attrs})'
        

class ContaPoupanca(Conta): # Inheritance
    def sacar(self, valor): # Polymorphism
        if valor > self.saldo:
            print( f'Não foi possível sacar {valor} da conta {self.conta}.'\
                  f' Saldo insuficiente.' )
            print( '___' )
            self.detalhes()
            return
        self.saldo -= valor
        self.detalhes( f'Saque de {valor} realizado com sucesso!!!' )
        return self.saldo # Retorna o saldo atual da conta


class ContaCorrente(Conta):
    def __init__(self, agencia:int, conta:int, saldo:float =0, limite:float=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar( self, valor: float ) -> float: # Polymorphism
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'Saque de {valor} realizado com sucesso!!!')
            return self.saldo
        
        print(f'Não foi possível sacar {valor} da conta {self.conta}.'\
              ' Saldo insuficiente.')
        self.detalhes(f'Seu limite é: -{self.limite}')
        return self.saldo
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'agencia:{self.agencia!r}, conta:{self.conta!r},'\
            f'Saldo:{self.saldo!r}, Limite:{self.limite!r}'
        
        return f'{class_name!r}({attrs})'


# Test account poupança
if __name__ == '__main__': 
    cp1 = ContaPoupanca(1, 123456, 1000)
    cp1.detalhes()
    cp1.depositar(500)
    cp1.sacar(2000)
    cp1.sacar(200)

print('\n\n\n')

# Test account corrente
if __name__ == '__main__': 
    cc1 = ContaCorrente(1, 123456, 1000)
    cc1.detalhes()
    cc1.depositar(500)
    cc1.sacar(1600)
    cc1.sacar(200)


    