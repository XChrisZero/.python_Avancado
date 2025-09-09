import os
# x - Módulo JSON e Pickle - Criando, lendo, atualizando e deletando arquivos com Python
# usa duas barras invertidas no Windows ou uma barra normal no Linux e Mac
# raw string r'' ou r"" antes do caminho do arquivo para ignorar caracteres especiais como \n, \t, etc
# se não passar o caminho completo, o arquivo será criado no diretório atual do script
# exemplo de caminho completo no Windows:
caminho_arquivo = r'C:\\Users\\chris\\OneDrive\\Documentos\\Projetos\\PY\\Udemy\\.py\\aulas\\Intermediario\\'
# exemplo de caminho completo no Linux ou Mac:
# caminho_arquivo = '/home/usuario/projetos/py/udemy/.py/aulas/Intermediario/'
caminho_arquivo += 'aulax.txt'

print(caminho_arquivo)

# # Forma tradicional de abrir e fechar um arquivo
arquivo = open(caminho_arquivo, 'w') # 'w' = modo escrita - se o arquivo não existir, ele cria
# 'w' apaga o conteúdo do arquivo se ele já existir
# "a" = modo append - adiciona conteúdo ao final do arquivo
# 'r' = modo leitura - erro se o arquivo não existir
# 'b' = modo binário
# 't' = modo texto (padrão)
# '+' = leitura e escrita
arquivo.close() # fecha o arquivo

# Usando o context manager - with (abre e fecha o arquivo)
with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo: # encoding='utf8' para evitar problemas com caracteres especiais
    print('Arquivo aberto', type(arquivo)) # <class '_io.TextIOWrapper'>
    arquivo.write('Olá mundo! \r\n') # escreve no arquivo e adiciona uma nova linha usando \n
    arquivo.writelines(  # escreve várias linhas no arquivo
        ('Linha 1\r\n', 'Linha 2\r\n', 'Linha 3\r\n', 'Linha 4\r\n', 'Linha 5\r\n', 'Linha 6\r\n')
    )
    arquivo.seek(0)  # move o cursor para o início do arquivo
    print(arquivo.readline(), end='')  # lê o conteúdo do arquivo linha a linha
    arquivo.seek(0)  # move o cursor para o início do arquivo
    print(arquivo.readline().strip())  # lê o conteúdo do arquivo linha a linha e remove espaços em branco
    arquivo.seek(0)  # move o cursor para o início do arquivo
    print(arquivo.read())  # lê o conteúdo do arquivo


    print('Arquivo vai ser fechado')

# os.remove(caminho_arquivo)  # apaga o arquivo
# os.unlink(caminho_arquivo)  # apaga o arquivo
# os.rename(caminho_arquivo, 'aulax_renomeado.txt')  # renomeia o arquivo
# os.rename('aulax_renomeado.txt', caminho_arquivo)  # renomeia o arquivo de volta

