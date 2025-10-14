# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO') # join monta o caminho correto para o sistema operacional
counter = count() # contador infinito

for root, dirs, files in os.walk(caminho): # percorre a árvore de diretórios
    the_counter = next(counter) # pega o próximo valor do contador
    print(the_counter, 'Pasta atual', root) # diretório atual

    for dir_ in dirs:   # percorre os subdiretórios
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files: # percorre os arquivos
        caminho_completo_arquivo = os.path.join(root, file_)
        print('  ', the_counter, 'FILE:', caminho_completo_arquivo)
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA) 
        # os.unlink(caminho_completo_arquivo) # apaga o arquivo