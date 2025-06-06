import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

def main():
    app = QApplication(sys.argv)
    widgets = QWidget()
    widgets.resize(200,50)
    widgets.setWindowTitle("PyQt5 GUI")
    # 푸시 버튼
    btn1 = QPushButton('O', widgets)
    btn1.resize(100,30)
    btn1.move(0,20)
    btn2 = QPushButton('X', widgets)
    btn2.resize(100,30)
    btn2.move(100,20)
    # 푸시 버튼 클릭
    btn1.clicked.connect(lambda: print("O 클릭"))
    btn2.clicked.connect(lambda: print("X 클릭"))
    widgets.show()
    sys.exit(app.exec_())
main()