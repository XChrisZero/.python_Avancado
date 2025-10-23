# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

argumentos = sys.argv # Lista com os argumentos passados no sistema
qtd_argumentos = len(argumentos) # Quantidade de argumentos passados

if qtd_argumentos <= 1: # Se não houver argumentos além do nome do arquivo
    print('Você não passou argumentos')
else: 
    try: # Tenta acessar os argumentos
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça outra coisa com {argumentos[2]}')
    except IndexError: # Se não houver argumentos suficientes
        print('Faltam argumentos')