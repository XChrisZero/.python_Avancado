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