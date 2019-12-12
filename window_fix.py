# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_form.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(540, 389)
        icon = QtGui.QIcon.fromTheme("icon")
        Dialog.setWindowIcon(icon)
        Dialog.setAutoFillBackground(True)
        self.Till = QtWidgets.QDateEdit(Dialog)
        self.Till.setGeometry(QtCore.QRect(240, 230, 111, 31))
        self.Till.setObjectName("Till")
        self.Since = QtWidgets.QDateEdit(Dialog)
        self.Since.setGeometry(QtCore.QRect(240, 170, 111, 31))
        self.Since.setObjectName("Since")
        self.email_label = QtWidgets.QLabel(Dialog)
        self.email_label.setGeometry(QtCore.QRect(40, 50, 81, 31))
        self.email_label.setBaseSize(QtCore.QSize(13, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.email_label.setFont(font)
        self.email_label.setAlignment(QtCore.Qt.AlignCenter)
        self.email_label.setObjectName("email_label")
        self.password_label = QtWidgets.QLabel(Dialog)
        self.password_label.setGeometry(QtCore.QRect(40, 90, 81, 31))
        self.password_label.setBaseSize(QtCore.QSize(13, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.password_label.setFont(font)
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.DateSinceLAbel = QtWidgets.QLabel(Dialog)
        self.DateSinceLAbel.setGeometry(QtCore.QRect(40, 170, 136, 22))
        self.DateSinceLAbel.setBaseSize(QtCore.QSize(13, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.DateSinceLAbel.setFont(font)
        self.DateSinceLAbel.setAlignment(QtCore.Qt.AlignCenter)
        self.DateSinceLAbel.setObjectName("DateSinceLAbel")
        self.DateTillLabel = QtWidgets.QLabel(Dialog)
        self.DateTillLabel.setGeometry(QtCore.QRect(40, 230, 128, 22))
        self.DateTillLabel.setBaseSize(QtCore.QSize(13, 13))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.DateTillLabel.setFont(font)
        self.DateTillLabel.setAutoFillBackground(True)
        self.DateTillLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DateTillLabel.setObjectName("DateTillLabel")
        self.email_input = QtWidgets.QTextEdit(Dialog)
        self.email_input.setGeometry(QtCore.QRect(200, 50, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email_input.setFont(font)
        self.email_input.setObjectName("email_input")
        self.password_input = QtWidgets.QTextEdit(Dialog)
        self.password_input.setGeometry(QtCore.QRect(200, 90, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_input.setFont(font)
        self.password_input.setObjectName("password_input")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(390, 310, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.buttonclicked)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "main_window"))
        self.email_label.setText(_translate("Dialog", "E-mail"))
        self.password_label.setText(_translate("Dialog", "Password"))
        self.DateSinceLAbel.setText(_translate("Dialog", "Начало периода"))
        self.DateTillLabel.setText(_translate("Dialog", "Конец периода"))
        self.pushButton.setText(_translate("Dialog", "Get reciepts"))

    def keypressevent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def buttonclicked(self):
        print('test')
        # since = self.Since.text()
        print(self.Till.text())
        # till = self.Till.text()
        # email = self.email_input.text()
        # password = self.password_input.text()
