# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os

caminho = os.path.join('Desktop', 'curso', 'arquivo.txt') # Cria um caminho
# print(caminho)
diretorio, arquivo = os.path.split(caminho) # Divide o caminho em diretório e arquivo
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo) # Divide o arquivo em nome e extensão

# print(nome_arquivo, extensao_arquivo) # Pega o nome e a extensão do arquivo
# print(os.path.exists('/Users//Desktop/')) # Verifica se o caminho existe
# print(os.path.abspath('.')) # Pega o caminho absoluto do diretório atual
# print(os.path.abspath('..')) # Pega o caminho absoluto do diretório pai

print(caminho)
print(os.path.basename(caminho)) # Pega o nome do arquivo
print(os.path.basename(diretorio)) # Pega o nome do diretório
print(os.path.dirname(diretorio)) # Pega o nome do diretório pai
print(os.path.dirname(caminho)) # Pega o nome do diretório pai
print(os.path.splitdrive(caminho)) # Divide o caminho em drive e resto do caminho