import sys
from PyQt5.QtWidgets import QApplication
from PyQt3Widget  import PyQt3Widget 
app = QApplication(sys.argv)
myw = PyQt3Widget ()
myw.show()
sys.exit(app.exec_())