from PySide6.QtWidgets import QMainWindow,QVBoxLayout, QWidget

class MainWindow(QMainWindow):

    def __init__ (self, *args, **kwargs): 
        super().__init__(*args, **kwargs) #type: ignore

        #titulo da janela
        self.setWindowTitle('Calculadora!!!')

        #configurações do layout
        self.central_widget = QWidget()
        self.vertical_layout = QVBoxLayout()
        self.central_widget.setLayout(self.vertical_layout)
        self.setCentralWidget(self.central_widget)

    def adjust_fixedSize(self):
        #ultiima linha do layout
        self.adjustSize()
        self.setFixedSize(self.size()) # Impede redimensionamento da janela
        #self.setFixedSize(self.width(), self.height()) # Define um tamanho fixo para a janela

    #método de boas praticas para adicionar widgets ao layout
    def add_widget_to_layout(self, widget: QWidget):
        self.vertical_layout.addWidget(widget)
        