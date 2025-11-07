# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.

# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual: nome_do_ambiente\Scripts\Activate.ps1
# pip install pypdf2

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# Definir pastas
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

# Arquivo PDF do Banco Central do Brasil
RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20251031.pdf'

# Criar pasta para salvar arquivos novos
PASTA_NOVA.mkdir(exist_ok=True)

# Ler arquivo PDF
reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages)) # número de páginas
# for page in reader.pages: # todas as páginas
#     print(page)
#     print()

# Extrair texto e imagens da primeira página
page0 = reader.pages[0] # primeira página
imagem0 = page0.images[0] # primeira imagem da página

# print(page0.extract_text()) # extrai o texto da página
# print(imagem0) # informações da imagem
# with open(PASTA_NOVA / imagem0.name, 'wb') as fp: # salva a imagem em um arquivo
#    fp.write(imagem0.data) # grava os dados da imagem no arquivo 

writer = PdfWriter() # criar um novo arquivo PDF
writer.add_page(page0) # adicionar a página extraída ao novo arquivo PDF

# Salvar novo arquivo PDF com a primeira página
with open(PASTA_NOVA / 'primeira_pagina.pdf', 'wb') as fp:
    writer.write(fp) # grava o novo arquivo PDF no disco    

# Unir vários arquivos PDF em um único arquivo
merger = PdfMerger() # criar um objeto PdfMerger

files = [
    PASTA_NOVA / 'page0.pdf',
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'R20250831.pdf'
]

for file in files:
    merger.append(file) # adicionar cada arquivo PDF ao objeto PdfMerger

merger.write(PASTA_NOVA / 'arquivo_unido.pdf') # salvar o arquivo PDF unido
merger.close() # fechar o objeto PdfMerger

# --- IGNORE ---

