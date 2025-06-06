from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
class PyQt5Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("리스트 박스 사용 데모")
        self.resize(1000,800)
        self.lbox = QListWidget(self)
        self.lbox.resize(400,600)
        self.te=QTextEdit(self)
        self.te.move(420,0)
        self.te.resize(400,80)
        self.btn = QPushButton("추가",self)
        self.btn.move(840,0)
        self.btn.resize(180,80)
        self.btn.clicked.connect(self.AddItem)
        self.lb_sel = QLabel("[테스트]",self)
        self.lb_sel.move(420,100)
        self.lbox.currentItemChanged.connect(self.OnLBoxSelectChange)
        self.btn_remove = QPushButton("선택 항목 삭제",self)
        self.btn_remove.move(420,200)
        self.btn_remove.clicked.connect(self.RemoveItem)
        self.btn_clear = QPushButton("모두 지우기",self)
        self.btn_clear.move(420,300)
        self.btn_clear.clicked.connect(self.ClearAll)
    def ClearAll(self):
        self.lbox.clear()
    def RemoveItem(self):
        index = self.lbox.currentRow()
        self.lbox.takeItem(index)
    def AddItem(self):
        data = self.te.toPlainText()
        self.lbox.addItem(data)
        self.te.setText("")
    def OnLBoxSelectChange(self):
        item = self.lbox.currentItem()
        self.lb_sel.setText(item.text())