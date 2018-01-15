# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fds.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(397, 260)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.x_value_input = QtWidgets.QTextEdit(self.centralwidget)
        self.x_value_input.setGeometry(QtCore.QRect(190, 60, 31, 31))
        self.x_value_input.setObjectName("x_value_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.xy_calc_button = QtWidgets.QPushButton(self.centralwidget)
        self.xy_calc_button.setGeometry(QtCore.QRect(280, 60, 75, 23))
        self.xy_calc_button.setObjectName("xy_calc_button")
        self.results_window = QtWidgets.QTextEdit(self.centralwidget)
        self.results_window.setGeometry(QtCore.QRect(10, 100, 371, 111))
        self.results_window.setObjectName("results_window")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.y_value_input = QtWidgets.QTextEdit(self.centralwidget)
        self.y_value_input.setGeometry(QtCore.QRect(240, 60, 31, 31))
        self.y_value_input.setObjectName("y_value_input")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(220, 80, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.file_select = QtWidgets.QPushButton(self.centralwidget)
        self.file_select.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.file_select.setObjectName("file_select")
        self.success_fail = QtWidgets.QLabel(self.centralwidget)
        self.success_fail.setGeometry(QtCore.QRect(90, 40, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.success_fail.setFont(font)
        self.success_fail.setText("")
        self.success_fail.setObjectName("success_fail")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter X,Y Coordinate:"))
        self.xy_calc_button.setText(_translate("MainWindow", "Calculate"))
        self.label_3.setText(_translate("MainWindow", "FDS Results Calculator"))
        self.label_4.setText(_translate("MainWindow", ","))
        self.file_select.setText(_translate("MainWindow", "Open File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

