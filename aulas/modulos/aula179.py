# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula179.csv'

with open(CAMINHO_CSV, 'r') as arquivo: # abre o arquivo
    # leitor = csv.reader(arquivo) # lê o arquivo em formato de lista
    leitor = csv.DictReader(arquivo)
    # next(leitor)  # Pula o cabeçalho

    for linha in leitor: # lê cada linha do arquivo
        # print(linha) # imprime a linha
        print(linha['Nome'], linha['Idade'], linha['Endereço']) # podendo acessar os valores individualmente

# with open(CAMINHO_CSV, 'r') as arquivo:
#     leitor = csv.reader(arquivo)

#     for linha in leitor:
#         print(linha)