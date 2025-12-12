from PySide6.QtWidgets import QLabel, QWidget

from variables import SMALL_FONT_SIZE

class Info(QLabel):

    def __init__(self, text: str, parent: QWidget | None = None,) -> None:
        super().__init__( text, parent)  # type: ignore
        self.config_style()

    def config_style(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px; color: gray;')
        
      