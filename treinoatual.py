# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treinoatual.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setStyleSheet("background-color: rgba(39, 78, 118, 200);\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbTituloTreinoAtual = QtWidgets.QLabel(self.centralwidget)
        self.lbTituloTreinoAtual.setGeometry(QtCore.QRect(290, 40, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lbTituloTreinoAtual.setFont(font)
        self.lbTituloTreinoAtual.setStyleSheet("color: rgb(255, 85, 0);")
        self.lbTituloTreinoAtual.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTituloTreinoAtual.setObjectName("lbTituloTreinoAtual")
        self.lbExAtual = QtWidgets.QLabel(self.centralwidget)
        self.lbExAtual.setGeometry(QtCore.QRect(310, 160, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbExAtual.setFont(font)
        self.lbExAtual.setStyleSheet("color: rgb(255, 85, 0);")
        self.lbExAtual.setAlignment(QtCore.Qt.AlignCenter)
        self.lbExAtual.setObjectName("lbExAtual")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 150, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_3.setObjectName("label_3")
        self.lbQuantEx = QtWidgets.QLabel(self.centralwidget)
        self.lbQuantEx.setGeometry(QtCore.QRect(410, 160, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbQuantEx.setFont(font)
        self.lbQuantEx.setStyleSheet("color: rgb(255, 85, 0);")
        self.lbQuantEx.setAlignment(QtCore.Qt.AlignCenter)
        self.lbQuantEx.setObjectName("lbQuantEx")
        self.lbNomeExe = QtWidgets.QLabel(self.centralwidget)
        self.lbNomeExe.setGeometry(QtCore.QRect(365, 200, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbNomeExe.setFont(font)
        self.lbNomeExe.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.lbNomeExe.setAlignment(QtCore.Qt.AlignCenter)
        self.lbNomeExe.setObjectName("lbNomeExe")
        self.btnPause = QtWidgets.QPushButton(self.centralwidget)
        self.btnPause.setGeometry(QtCore.QRect(210, 640, 151, 41))
        self.btnPause.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.btnPause.setObjectName("btnPause")
        self.btnProximo = QtWidgets.QPushButton(self.centralwidget)
        self.btnProximo.setGeometry(QtCore.QRect(440, 640, 151, 41))
        self.btnProximo.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.btnProximo.setObjectName("btnProximo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 260, 381, 271))
        self.label.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(305, 568, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(True)
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setSpecialValueText("")
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 13), QtCore.QTime(0, 0, 0)))
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeEdit.setObjectName("timeEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.pushButton.setStyleSheet("border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 0px;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("voltarIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbTituloTreinoAtual.setText(_translate("MainWindow", "Dia"))
        self.lbExAtual.setText(_translate("MainWindow", "Ex. Atual"))
        self.label_3.setText(_translate("MainWindow", "/"))
        self.lbQuantEx.setText(_translate("MainWindow", "Quantidade"))
        self.lbNomeExe.setText(_translate("MainWindow", "Nome"))
        self.btnPause.setText(_translate("MainWindow", "Pause"))
        self.btnProximo.setText(_translate("MainWindow", "Proximo"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "mm:ss"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

