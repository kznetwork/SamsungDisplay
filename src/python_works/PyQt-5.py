import sys
from PyQt5.QtWidgets import QApplication
from PyQt5Widget  import PyQt5Widget 
app = QApplication(sys.argv)
myw = PyQt5Widget ()
myw.show()
sys.exit(app.exec_())
