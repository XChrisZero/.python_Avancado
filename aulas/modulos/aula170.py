# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

caminho = os.path.join('/Users', 'luizotavio', 'Desktop', 'EXEMPLO') # join monta o caminho correto para o sistema operacional
# caminho = os.path.join('C:\\', '

for pasta in os.listdir(caminho): # lista todas as pastas e arquivos do caminho
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta): # se não for um diretório,
        continue

    for imagem in os.listdir(caminho_completo_pasta): # lista todas as pastas e arquivos do caminho
        print('  ', imagem)