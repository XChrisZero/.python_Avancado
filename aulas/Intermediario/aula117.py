import json

caminho_arquivo = r'C:\\Users\\chris\\OneDrive\\Documentos\\Projetos\\PY\\Udemy\\.py\\aulas\\Intermediario\\'
caminho_arquivo += 'aula117.json'
pessoa = {
    'nome': 'Christian',
    'sobrenome': 'Kuriak chung ferrari',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (7, 14, 69, 89, 100),
    'dev': True,
    'nada': None,
}

# Criando um arquivo JSON e como não foi passado o caminho completo, o arquivo será criado no diretório atual do script
with open(caminho_arquivo, 'w', encoding='utf8') as arquivo: # abre o arquivo 
    json.dump( #dump = despejar 
        pessoa,
        arquivo,
        ensure_ascii=False, # para manter os caracteres especiais
        indent=2, # para formatar o json com identação
    )

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])