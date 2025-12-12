# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys

from PySide6.QtWidgets import QApplication, QPushButton

# Cria a aplicação
app = QApplication(sys.argv)

botao = QPushButton('Texto do botão') # Cria um botão com um texto
botao.setStyleSheet('font-size: 40px;') # Define o tamanho da fonte do texto do botão
botao.show()  # Adiciona o widget na hierarquia e exibe a janela

app.exec()  # O loop da aplicação