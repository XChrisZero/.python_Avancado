# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> genérico
# QLayout -> Um widget de layout que recebe outros widgets
import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication(sys.argv) # Cria a aplicação

# Cria os botões
botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

central_widget = QWidget() # Cria um widget genérico para ser o widget central da aplicação

layout = QGridLayout() # Cria um layout do tipo grid (grade) tipo tabela
central_widget.setLayout(layout) # Define o layout do widget central como sendo o layout grid

# Adiciona os botões ao layout grid nas posições desejadas
layout.addWidget(botao, 1, 1, 1, 1) # Ocupa 1 linha e 1 coluna
layout.addWidget(botao2, 1, 2, 1, 1) # Ocupa 1 linha e 1 coluna
layout.addWidget(botao3, 3, 1, 1, 2) # Ocupa 1 linha e 2 colunas (os dois ultiimos digiiitos são o rowspan e colspan)

central_widget.show()  # Central widget entre na hierarquia e mostre sua janela
app.exec()  # O loop da aplicação