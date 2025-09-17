# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
CAMINHO_ARQUIVO = 'exercicio127.json' # arquivo onde os dados serão salvos


class Pessoa: # criando a classe Pessoa
    def __init__(self, nome, idade): # método construtor
        self.nome = nome # atributos nome e idade
        self.idade = idade 

# criando instâncias da classe Pessoa
p1 = Pessoa('João', 33)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)] # lista de dicionários com os dados das pessoas


def fazer_dump(): # função para salvar os dados em um arquivo JSON
    with open(CAMINHO_ARQUIVO, 'w') as arquivo: # abrindo o arquivo em modo escrita ([W]rite)
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2) # salvando os dados no arquivo JSON

# Testando se o arquivo está sendo executado diretamente
if __name__ == '__main__':
    print('ELE É O __main__')
    fazer_dump()

