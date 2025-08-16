# (Parte1) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

try: # Começa o bloco de código a ser testado
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError: # Bloco de código que irá tratar a exceção
    print('Dividiu por zero.')

except NameError: # Bloco de código que irá tratar a exceção
    print('Nome b não está definido')

except (TypeError, IndexError) as error: # as é um alias para a exceção
    print('TypeError + IndexError')
    print (f'mensagem:{error}, do tipo {error.__class__.__name__}') # Exibe a mensagem de erro e o tipo da exceção

except Exception: # Bloco de código que irá tratar a qualquer exceção
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')

'''


'''

