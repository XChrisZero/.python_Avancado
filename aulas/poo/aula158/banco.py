import contas
import pessoas


class Banco:
    def __init__( self,
                 agencias: list[int] | None = None,
                 clientes: list[pessoas.Pessoa] | None= None,
                 contas: list[contas.Conta] | None = None, 
                 ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []


    def _check_agencia( self,
                       conta ) -> bool:
        if conta.agencia in self.agencias:
            print(f'Agência {conta.agencia} pertence ao banco.')
            return True
        print(f'Agência {conta.agencia} não pertence ao banco.')
        return False


    def _check_cliente( self,
                       cliente ) -> bool:
        if cliente in self.clientes:
            print(f'Cliente {cliente.nome} é cliente do banco.')
            return True
        print(f'Cliente {cliente.nome} não é cliente do banco.')
        return False


    def _check_conta( self,
                       conta ) -> bool:
        if conta in self.contas:
            print(f'Conta {conta.conta} pertence ao banco.')
            return True
        print(f'Conta {conta.conta} não pertence ao banco.')
        return False


    def _conta_e_do_cliente( self,
                        cliente, 
                       conta ) -> bool:
        cc1 = pessoas.Cliente
        if conta is cliente.conta:
            print(f'Conta {conta.conta} pertence ao cliente.')
            return True
        print(f'Conta {conta.conta} não pertence ao cliente.')
        return False


    def autenticar( self,
                   cliente: pessoas.Pessoa, 
                   conta: contas.Conta ) -> bool:
        return self._check_agencia(conta) and \
                self._check_cliente(cliente) and \
                self._check_conta(conta) and \
                self._conta_e_do_cliente(cliente, conta)    
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'Agencia:{self.agencias!r}, Cliente:{self.clientes!r}, Conta:{self.contas!r}'
        return f'{class_name!r}({attrs})'
    


if __name__ == '__main__':
    
    cc1 = pessoas.Cliente('Elaine', 31)
    cc1.conta = contas.ContaCorrente(123, 321, 0, 5000)
    class_c = type(cc1).__name__
    #print(f'{class_c} criada com sucesso!')
    #print(cc1.nome, cc1.idade, cc1.conta)

    cp1 = pessoas.Cliente('Christian', 30)
    cp1.conta = contas.ContaPoupanca(234, 432, 0)
    class_c = type(cp1).__name__
    #print(f'{class_c} criada com sucesso!')
    #print(cp1.nome, cp1.idade, cp1.conta)

    banco = Banco()
    banco.clientes.extend([cc1, cp1])
    banco.contas.extend([cc1.conta, cp1.conta])
    banco.agencias.extend([123, 234])

    print('---' * 10)
    print('Banco autenticando clientes e contas...')
    banco.autenticar(cp1, cp1.conta)
    print('---' * 10 )

    if banco.autenticar(cp1, cp1.conta):
        cp1.conta.depositar(1000)
        cp1.conta.sacar(500)
        cp1.conta.sacar(600)
        cp1.conta.sacar(200)