# Ambientes virtuais em Python (venv) python -V
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env

"""
para entrar no ambiente virtual no windows:
use: .\venv\Scripts\activate

para sair do ambiente virtual:
use: deactivate

para instalar e desinstalar um modulo no ambiente virtual:
use: pip install nome_do_modulo
exemplo: pip install pymysql
use: pip uninstall pymysql

para ver as bibliotecas instaladas no ambiente virtual:
use: pip list

para criar um arquivo de requisitos:
pip freeze > requirements.txt
pip install -r requirements.txt

instalar todos arquivos do requirements.txt
use: pip install -r requirements.txt

"""

