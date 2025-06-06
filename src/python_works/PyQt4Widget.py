from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class PyQt4Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("테스트 입력 및 설정")
        self.te = QTextEdit(self)
        self.te.resize(400,90)
        self.resize(1000,600)
        self.btn = QPushButton("확인",self)
        self.btn.move(430,0)
        self.btn.resize(200,90)
        self.lb = QLabel("[테스트]",self)
        self.lb.move(0,110)
        self.btn.clicked.connect(self.BtnClick)
    def BtnClick(self):
        txt = self.te.toPlainText()
        self.lb.setText(txt)
        self.te.setText("")