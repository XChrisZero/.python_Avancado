# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

from exercicio.exercicio127 import Pessoa, fazer_dump, CAMINHO_ARQUIVO

# Lendo os dados do arquivo JSON e recriando as instâncias da classe Pessoa
with open(CAMINHO_ARQUIVO, 'r') as arquivo: # abrindo o arquivo em modo leitura ([R]ead)
    pessoas = json.load(arquivo)
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)