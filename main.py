import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

main_window = QtWidgets.QMainWindow()
main_window.show()

sys.exit(app.exec_())
