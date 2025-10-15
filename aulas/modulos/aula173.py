# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
import os
import shutil

HOME = os.path.expanduser('~') # Expande o caminho do usuário
API_ = os.path.join(HOME, 'OneDrive', 'Documentos', 'Projetos', 'api_' ) # join Junta os caminhos
PASTA_ORIGINAL = os.path.join(HOME, 'OneDrive', 'Documentos', 'Projetos', 'transacao_api' )
NOVA_PASTA = os.path.join(HOME, 'OneDrive', 'Documentos', 'Projetos', 'NOVA_PASTA')

print(NOVA_PASTA)
print(PASTA_ORIGINAL)

os.makedirs(NOVA_PASTA, exist_ok=True) #exist_ok=True faz não dar erro se a pasta já existir

for root, dirs, files, in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_) #replace substitui a parte do caminho antigo pelo novo
        os.makedirs(caminho_novo_diretorio, exist_ok=True) #cria o diretório novo 


    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file) #replace substitui a parte do caminho antigo pelo novo
        shutil.copy(caminho_arquivo, caminho_novo_arquivo) #copia o arquivo de um lugar para outro 