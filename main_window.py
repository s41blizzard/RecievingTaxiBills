import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main_form.ui', self)


