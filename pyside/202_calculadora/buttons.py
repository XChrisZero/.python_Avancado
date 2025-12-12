from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import SMALL_FONT_SIZE
from utils import is_NumOrDot, is_Empty, is_Valid_number
from display import Display

#button class
class Button(QPushButton):

    #button initialization
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure_style()

    #style configuration
    def configure_style(self):
        #self.setStyleSheet('font-size: 20px; font-weight: bold;') # estilo direto no botão
        font = self.font()
        font.setPixelSize(SMALL_FONT_SIZE)
        font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(50, 50) 
        
#grid buttons to calculator
class Grid_Button(QGridLayout):
    def __init__(self, display:Display, info, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self._equation = ''
        self.equatin_initial_value = 'Conta atual: Nenhuma'
        self._left = None
        self._right = None
        self._operator = None
        self._clear()
        self._make_grid()

        self._equation = self.equatin_initial_value


    #Getter and Setter for equation 
    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value: str):
        self._equation = value
        self.info.setText(f'Equação atual: {self._equation}', value)


    


    #grid maker
    def _make_grid(self):
        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)

                if  not is_NumOrDot(button_text) and not is_Empty(button_text):
                    button.setProperty('CssClass', 'specialButton')
                    self._configure_special_button(button)

                #adding button to grid
                self.addWidget(button, i, j)

                #button.clicked.connect(lambda checked, b=button: print(f'Botão "{b.text()}" clicado!'))
                b_slot = self._make_slot(
                    self._insert_button_text_to_display, 
                    button
                    )
                
                #connecting button clicked signal to slot
                #self._connect_buttons_clicked(button, b_slot)
                button.clicked.connect(b_slot) # type: ignore

    #button clicked connection
    def _connect_buttons_clicked(self, button, b_slot):
        b_slot = self._make_slot(b_slot)
        button.clicked.connect(b_slot)  # type: ignore

    def _configure_special_button(self, button: Button):
        text = button.text()
        print(f'Configurando botão especial: "{text}"')

        if text == 'C':
            button.clicked.connect(self._make_slot(self._clear))  
            self._connect_buttons_clicked(button, self._clear)

        if text in '-+/*':
            
            self._connect_buttons_clicked(
                button, self._make_slot(
                    self._operator_clicked, button) 
                    )


    #connection maker
    def _make_slot(self, method, *args, **kwargs):

        @ Slot(bool)
        def real_slot(_):
            method( *args, **kwargs)
        return real_slot

    #insert button text into display
    def _insert_button_text_to_display(self, button):
        button_text = button.text()
        new_display_value = self.display.text() + button_text

        if button_text == '=':
            print('Calculando resultado...')
        
        else:
            print(f'Botão "{button_text}" clicado!')
        
        #if not is_Valid_number(new_display_value):
        #    print(f'Entrada inválida: "{new_display_value}"')
        

        self.display.insert(button_text)

    #clear display method
    def _clear(self):
        self.display.clear()
        print('Limpando display e equação...')
        self._left = None
        self._right = None
        self._op = None
        

        self._equation = self.equatin_initial_value

    def _operator_clicked(self, button: Button):
        buttonText = button.text()  # +-/* (etc...)
        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # Limpa o display

        # Se a pessoa clicou no operador sem
        # configurar qualquer número
        if not is_Valid_number(displayText) and self._left is None:
            print('Não tem nada para colocar no valor da esquerda')
            return

        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = float(displayText)

        self._op = buttonText
        self.equation = f'{self._left} {self._op} ??'

