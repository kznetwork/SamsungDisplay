from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class PyQt3Widget (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("나의 창")
        pal = QPalette()
        pal.setColor(QPalette.Background,QColor(255,0,255))
        self.setAutoFillBackground(True)
        self.setPalette(pal)