# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
try:
    print('ABRIR ARQUIVO') # Simula a abertura de um arquivo
    8/0
except ZeroDivisionError as e: # Trata a exceção de divisão por zero
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError as error: # Trata a exceção de índice fora do intervalo
    print('IndexError')
except (NameError, ImportError): # Trata múltiplas exceções
    print('NameError, ImportError')

else: # Executa se não houver exceção
    print('Não deu erro')

finally: # Sempre executa, mesmo se houver exceção ou erro
    print('FECHAR ARQUIVO')

