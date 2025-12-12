from PySide6.QtWidgets import QLineEdit, QTextEdit
from PySide6.QtCore import Qt

from variables import BIG_FONT_SIZE, MEDIUM_FONT_SIZE, TEXT_MARGIN

class Display(QLineEdit):
    ## Display for calculator
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # type: ignore
        self.confg_style()
        
    ## Configuration and styling of the display   
    def confg_style(self):
        margin = [TEXT_MARGIN for _ in range(4)]

        self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px;') # Define o tamanho da fonte do display
        #self.setReadOnly(True) # Torna o QLineEdit somente leitura
        self.setFixedHeight(MEDIUM_FONT_SIZE * 2) # Define uma altura fixa para o display
        self.setAlignment(Qt.AlignmentFlag.AlignAbsolute) # Alinha o texto à direita
        self.setPlaceholderText('Digite aqui!!!') # Texto placeholder quando o display está vazio
        self.setText('') # Inicializa o display com texto vazio
        self.setTextMargins(*margin) # Margens internas do display


    