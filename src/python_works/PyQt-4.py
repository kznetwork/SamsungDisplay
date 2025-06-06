import sys
from PyQt5.QtWidgets import QApplication
from PyQt4Widget  import PyQt4Widget 
app = QApplication(sys.argv)
myw = PyQt4Widget ()
myw.show()
sys.exit(app.exec_())
