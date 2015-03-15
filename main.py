import sys
from PyQt5 import QtWidgets, QtCore

class MyListModel(QtCore.QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(MyListModel, self).__init__(*args, **kwargs)
        self.data_ = ['Fluffy', 'Bunnies', 'Blue', 'purple']

    def rowCount(self, parent=QtCore.QModelIndex):
        return len(self.data_)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if not index.isValid():
            return QtCore.QVariant()

        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        return self.data_[index.row()]

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if not index.isValid() or role != QtCore.Qt.EditRole:
            return False
        self.data_[index.row()] = value
        self.dataChanged.emit(index, index)
        return True

    def flags(self, index):
        if index.isValid():
            return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    main_window = QtWidgets.QMainWindow()
    
    my_list_model = MyListModel()

    list_view = QtWidgets.QListView(parent=main_window)
    list_view.setModel(my_list_model)


    main_window.setCentralWidget(list_view)
    
    
    main_window.show()

    sys.exit(app.exec_())
