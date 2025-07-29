"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1


def escopo():
    global x # Declara x como global para modificar o valor fora da função
    x = 10

    def outra_funcao():
        global x # Declara x como global novamente para modificar o valor fora da função
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x) # Exibe o valor de x antes da chamada da função escopo
escopo() # Chama a função escopo que modifica o valor de x
print(x) # Exibe o valor de x antes e depois da chamada da função escopo