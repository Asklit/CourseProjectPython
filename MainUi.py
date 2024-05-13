# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiMainFile.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Checker(object):
    def setupUi(self, Checker):
        Checker.setObjectName("Checker")
        Checker.resize(940, 680)
        Checker.setMaximumSize(QtCore.QSize(940, 680))
        Checker.setToolTip("")
        Checker.setStyleSheet("QWidget {\n"
"  background-color: #A0AECD;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Checker)
        self.centralwidget.setObjectName("centralwidget")
        self.labelSettings = QtWidgets.QLabel(self.centralwidget)
        self.labelSettings.setGeometry(QtCore.QRect(360, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.labelSettings.setFont(font)
        self.labelSettings.setMouseTracking(False)
        self.labelSettings.setStyleSheet("")
        self.labelSettings.setObjectName("labelSettings")
        self.btnChooseFile = QtWidgets.QPushButton(self.centralwidget)
        self.btnChooseFile.setGeometry(QtCore.QRect(50, 90, 180, 50))
        self.btnChooseFile.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnChooseFile.setFont(font)
        self.btnChooseFile.setStyleSheet("QPushButton {\n"
"  color: solid black;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid black;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #6E6E6E;\n"
"  border: 1px solid black;\n"
"}")
        self.btnChooseFile.setObjectName("btnChooseFile")
        self.LENameFile = QtWidgets.QLineEdit(self.centralwidget)
        self.LENameFile.setGeometry(QtCore.QRect(240, 90, 661, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.LENameFile.setFont(font)
        self.LENameFile.setStyleSheet("QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid black;\n"
"  padding: 5px 15px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border: 1px solid yellow;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.LENameFile.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.LENameFile.setReadOnly(True)
        self.LENameFile.setObjectName("LENameFile")
        self.btnRun = QtWidgets.QPushButton(self.centralwidget)
        self.btnRun.setGeometry(QtCore.QRect(360, 300, 180, 50))
        self.btnRun.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnRun.setFont(font)
        self.btnRun.setStyleSheet("QPushButton {\n"
"  color: solid black;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid black;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #6E6E6E;\n"
"  border: 1px solid black;\n"
"}")
        self.btnRun.setObjectName("btnRun")
        self.btnSettings = QtWidgets.QPushButton(self.centralwidget)
        self.btnSettings.setGeometry(QtCore.QRect(730, 600, 180, 50))
        self.btnSettings.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnSettings.setFont(font)
        self.btnSettings.setStyleSheet("QPushButton {\n"
"  color: solid black;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid black;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #6E6E6E;\n"
"  border: 1px solid black;\n"
"}")
        self.btnSettings.setObjectName("btnSettings")
        self.LEErrorLine = QtWidgets.QLineEdit(self.centralwidget)
        self.LEErrorLine.setGeometry(QtCore.QRect(340, 380, 221, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.LEErrorLine.setFont(font)
        self.LEErrorLine.setStyleSheet("QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid yellow;\n"
"  padding: 5px 15px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border: 1px solid yellow;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.LEErrorLine.setAlignment(QtCore.Qt.AlignCenter)
        self.LEErrorLine.setReadOnly(True)
        self.LEErrorLine.setObjectName("LEErrorLine")
        Checker.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Checker)
        self.statusbar.setObjectName("statusbar")
        Checker.setStatusBar(self.statusbar)

        self.retranslateUi(Checker)
        QtCore.QMetaObject.connectSlotsByName(Checker)

    def retranslateUi(self, Checker):
        _translate = QtCore.QCoreApplication.translate
        Checker.setWindowTitle(_translate("Checker", "Checker"))
        self.labelSettings.setText(_translate("Checker", "Проверка"))
        self.btnChooseFile.setText(_translate("Checker", "Выбрать файл"))
        self.LENameFile.setText(_translate("Checker", "Файл не выбран"))
        self.btnRun.setText(_translate("Checker", "Проверить"))
        self.btnSettings.setText(_translate("Checker", "Настройки"))
        self.LEErrorLine.setText(_translate("Checker", "Выберите файл"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Checker = QtWidgets.QMainWindow()
    ui = Ui_Checker()
    ui.setupUi(Checker)
    Checker.show()
    sys.exit(app.exec_())
