# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile
import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent # Diretório da aula
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula_186_diretorio_zip' # Diretório para criar os arquivos que serão compactados
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula186_compactado.zip' # Arquivo compactado
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula186_descompactado' # Diretório para descompactar os arquivos

shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True) # Remove o diretório de arquivos para zip
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True) # Remove o arquivo compactado
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True) # Remove o diretório descompactado
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True) # Remove o diretório descompactado

# raise Exception() # Descomente para testar a limpeza dos arquivos antes de criar novos

# Cria o diretório para a aula 
CAMINHO_ZIP_DIR.mkdir(exist_ok=True) # Cria o diretório onde os arquivos para zip serão criados


def criar_arquivos(qtd: int, zip_dir: Path): # Cria arquivos de texto para compactar
    for i in range(qtd):
        texto = 'arquivo_%s' % i # Nome do arquivo
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo: # Cria o arquivo
            arquivo.write(texto)


criar_arquivos(10, CAMINHO_ZIP_DIR) # Cria 10 arquivos de texto para compactar

# Criando um zip e adicionando arquivos
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            # print(file)
            zip.write(os.path.join(root, file), file)

# Lendo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)


# Extraindo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)
