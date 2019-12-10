import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import window_design


class Main(QtWidgets.QMainWindow, window_design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_w = Main()
    main_w.show()
    sys.exit(app.exec())
