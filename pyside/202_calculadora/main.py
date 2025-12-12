import sys

from display import Display
from info import Info
from variables import WINDOW_ICON_PATH
from main_window import MainWindow
from buttons import Button, Grid_Button

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import Qt


def temp_label(text: str) -> QLabel:
    label = QLabel(text)
    label.setStyleSheet('font-size: 25px; color: blue;')
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    return label


if __name__ == '__main__':

    #criando a aplicação
    app = QApplication(sys.argv)

    #criando a janela principal
    window = MainWindow()
 
    #adicionando widgets ao layout da janela principal
    window.add_widget_to_layout(temp_label('Calculadora do Chris aqui!!!'))
    
    #Icone da janela
    icone = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icone)
    app.setWindowIcon(icone)

    #info label
    info = Info('Calculadora com PySide6')
    window.add_widget_to_layout(info)

    #Display widget
    display = Display()
    window.add_widget_to_layout(display)

    #Grid de botões da calculadora
    grid_Buttons = Grid_Button(display, info)
    window.vertical_layout.addLayout(grid_Buttons)

    #botões da calculadora caso queira adicionar manualmente
    """
    grid_Buttons.addWidget(Button('1'), 0, 0)
    grid_Buttons.addWidget(Button('2'), 0, 1)
    grid_Buttons.addWidget(Button('3'), 0, 2)
    grid_Buttons.addWidget(Button('4'), 1, 0)
    grid_Buttons.addWidget(Button('5'), 1, 1)
    grid_Buttons.addWidget(Button('6'), 1, 2)
    grid_Buttons.addWidget(Button('7'), 2, 0)
    grid_Buttons.addWidget(Button('8'), 2, 1)
    grid_Buttons.addWidget(Button('9'), 2, 2)
    grid_Buttons.addWidget(Button('0'), 3, 1)
    """


      
    #ajustando tamanho fixo da janela após adicionar os widgets
    window.adjust_fixedSize()

    #executando a aplicação
    window.show()
    app.exec()

