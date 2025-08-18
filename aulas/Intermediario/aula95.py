# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def nao_aceito_zero(d): # Verifica se o divisor é zero
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero') #raise é usado para lançar uma exceção
    return True 


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)): # Verifica se n é int ou float, instance é usado para verificar o tipo
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True 


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(8, '0')) # Testa a função divide com um divisor inválido
print(divide(8, 0)) # Testa a função divide com divisor zero

'''
def divide(n, d):
    try:
        return n / d  # Função divide que não verifica tipos ou zero, apenas para fins de exemplo
    except ZeroDivisionError:  # Trata a exceção de divisão por zero
        return n # Retorna o numerador se houver divisão por zero 
        raise # Re-lança a exceção para ser tratada fora da função, mas não é necessário aqui por que o Py ja trata isso

print(divide(8, 0)) # Testa a função divide com divisor zero
'''