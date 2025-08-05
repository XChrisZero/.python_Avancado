# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args): 
    total = 1
    for num in args: 
        total *= num
    return total
    
mult = multiplica(1, 2, 3, 4, 5)
print(mult)


# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par' # Retorna se o número é par
    # else: aqui é opcional, pois se não for par, é ímpar e se torna redundante colocalo por que a função return finaliza o codigo por isso o segundo return está fora do if
    return f'{numero} é ímpar' # Retorna se o número é ímpar


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)