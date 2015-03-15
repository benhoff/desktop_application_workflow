import sys
from PyQt5 import QtWidgets





if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    main_window = QtWidgets.QMainWindow()
    
    list_widget = QtWidgets.QListWidget(parent=main_window)
    simple_list = ['Butter', 'Blue', 'red', 'elephants']

    """
    for item in simple_list:
        list_widget.addItem(item)
    """
    list_widget.addItems(simple_list)
    main_window.setCentralWidget(list_widget)
    
    
    main_window.show()

    sys.exit(app.exec_())
