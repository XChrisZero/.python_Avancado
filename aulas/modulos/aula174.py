# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil

HOME = os.path.expanduser('~') # Expande o caminho do usuário
PASTA_ORIGINAL = os.path.join(HOME, 'OneDrive', 'Documentos', 'Projetos', 'transacao_api' )
NOVA_PASTA = os.path.join(HOME, 'OneDrive', 'Documentos', 'Projetos', 'NOVA_PASTA')

print(NOVA_PASTA)
print(PASTA_ORIGINAL)

# os.unlink(NOVA_PASTA) # Apaga o arquivo NOVA_PASTA se for um arquivo e não uma pasta

# DELETE A PASTA NOVA_PASTA SE ELA JÁ EXISTIR
shutil.rmtree(NOVA_PASTA, ignore_errors=True) # ignore_errors=True faz não dar erro se a pasta não existir

shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA) # Copia a pasta inteira de um lugar para outro

# shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA') # Move ou renomeia a pasta
#shutil.move(NOVA_PASTA, NOVA_PASTA.replace('NOVA_PASTA', 'NOVA_PASTA_2')) # Move ou renomeia a pasta
#os.rename(NOVA_PASTA, NOVA_PASTA.replace('NOVA_PASTA', 'NOVA_PASTA_2')) # Move ou renomeia a pasta
