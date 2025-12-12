# O básico sobre Signal e Slots (eventos e documentação)
import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)

app = QApplication(sys.argv) # Criar a aplicação
window = QMainWindow() # Criar a janela principal
central_widget = QWidget() # Criar o widget central
window.setCentralWidget(central_widget) # Definir o widget central
window.setWindowTitle('Minha janela bonita') # Definir o título da janela

# Botões
botao1 = QPushButton('Texto do botão')
botao1.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

layout = QGridLayout() # Layout em grade
central_widget.setLayout(layout) # Definir o layout do widget central

# Adicionar os botões ao layout
layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('O meu slot foi executado')
    return inner


@Slot()
def outro_slot(checked):
    print('Está marcado?', checked)


@Slot()
def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# menuBar
menu = window.menuBar()

# primeiiro menu e ações, triggered que é clicado ou acionado
#triggered é o evento de clique
primeiro_menu = menu.addMenu('Primeiro menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(slot_example(status_bar))  # type:ignore
#   lambda: slot_example(status_bar)())  # type:ignore # outra forma de fazer

# Segunda ação com checkbox e hover evento
#toggle é marcado ou desmarcado
# hover é quando o mouse passa por cima
segunda_action = primeiro_menu.addAction('Segunda ação')
segunda_action.setCheckable(True) # checkbox
segunda_action.toggled.connect(outro_slot)  # type:ignore
segunda_action.hovered.connect(terceiro_slot(segunda_action))  # type:ignore

# Conectar o clique do botão 1 com o terceiro slot
botao1.clicked.connect(terceiro_slot(segunda_action))  # type:ignore

# Mostrar a janela
window.show()
app.exec()  # O loop da aplicação