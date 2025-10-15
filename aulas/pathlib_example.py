from pathlib import Path

caminho_projeto = Path()
print(caminho_projeto.absolute())  # caminho absoluto do projeto

caminho_arquivo = Path(__file__)
print(caminho_arquivo)  # caminho do arquivo atual, e só o caminho, não cria ele no sistema
print(caminho_arquivo.name)  # nome do arquivo atual
print(caminho_arquivo.parent)  # diretório pai do arquivo atual podendo usar .parents[0], .parents[1], etc para acessar diretórios mais acima

ideias = caminho_arquivo.parent.parent / 'ideias.txt'  # criando um novo caminho para o arquivo ideias.txt
print(ideias / 'arquivo.txt') # juntando caminhos

arquivo = Path.home() / 'arquivo.txt'  # criando um novo caminho para o arquivo arquivo.txt na pasta home do usuário
arquivo.touch()  # cria o arquivo se não existir
print(arquivo.exists())  # verifica se o arquivo existe

print(arquivo.stat())  # informações do arquivo
print(arquivo.stat().st_size)  # tamanho do arquivo em bytes

arquivo.write_text('Olá mundo!')  # escreve no arquivo
print(arquivo.read_text())  # lê o conteúdo do arquivo

# para escrever no arvivo sem apagar o conteúdo existente
with arquivo.open('a', encoding='utf8') as file:
    file.write('\r\nLinha 2\r\nLinha 3')

arquivo.rename(arquivo.with_name('arquivo_renomeado.txt'))  # renomeia o arquivo
arquivo = arquivo.with_name('arquivo_renomeado.txt')  # atualiza o objeto arquivo com o novo nome
print(arquivo)

arquivo.unlink()  # apaga o arquivo
print(arquivo.exists())  # verifica se o arquivo existe

print(list(caminho_arquivo.parent.glob('*.py')))  # lista todos os arquivos .py no diretório atual


#para criar diretórios(pastas)
novo_dir = caminho_arquivo.parent / 'novo_dir' / 'sub_dir'
novo_dir.mkdir(parents=True, exist_ok=True)  # cria o diretório novo_dir e sub_dir, se já existir não dá erro
print(novo_dir)

novo_dir.rmdir()  # remove o diretório sub_dir
novo_dir.parent.rmdir()  # remove o diretório novo_dir

print(list(caminho_arquivo.parent.iterdir()))  # lista todos os arquivos e diretórios no diretório atual

files = caminho_arquivo.parent / 'files'
files.mkdir(exist_ok=True)  # cria o diretório files se não existir

for i in range(10 ):
    file = files / f'file_{i}.txt'

    if file.exists():
        file.unlink()  # apaga o arquivo se já existir
    else:
        file.touch()  # cria o arquivo se não existir

    with file.open('a+') as text_file:
        text_file.write(f'Linha {i}\r\n')  # escreve no arquivo
        text_file.seek(0)  # move o cursor para o início do arquivo
    
def rmtree(root, remove_root=True): # remove uma árvore de diretórios
    for file in root.glob('*'):
        if file.is_dir():
            rmtree(file, remove_root=True)
        else:
            file.unlink()
    if remove_root:
        root.rmdir()

rmtree(files)  # remove o diretório files e todo o seu conteúdo