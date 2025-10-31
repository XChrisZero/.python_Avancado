# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

"""
#AQUI ESTAVA O CÓDIGO INICIAL PARA CRIAR O NAVEGADOR COM SELENIUM

ROOT_FOLDER = Path(__file__).parent # pasta onde está o main.py
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe' # coloque a extensão .exe no Windows

# Configurações do ChromeDriver
chrome_options = webdriver.ChromeOptions()
chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC)) 
chrome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options,
)

#chrome_options.add_argument('--headless')  # Executa o navegador em modo headless (sem interface gráfica)

chrome_browser.get('http://localhost:8000/#home')
time.sleep(10)  # Aguarda 10 segundos para garantir que a página carregue completamente
"""


# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent

# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'  # Coloque a extensão .exe no Windows

# Função para criar o navegador Chrome com opções personalizadas
def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    # Configuração do serviço do ChromeDriver
    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    # Criação do navegador Chrome
    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser 

# Exemplo de uso da função make_chrome_browser
if __name__ == '__main__':
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('http://localhost:8000') # Acessa a URL desejada

    # Dorme por 10 segundos
    sleep(10)