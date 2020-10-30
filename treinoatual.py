# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treinoatual.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbTituloTreinoAtual = QtWidgets.QLabel(self.centralwidget)
        self.lbTituloTreinoAtual.setGeometry(QtCore.QRect(10, 10, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lbTituloTreinoAtual.setFont(font)
        self.lbTituloTreinoAtual.setStyleSheet("color: rgb(255, 85, 0);")
        self.lbTituloTreinoAtual.setObjectName("lbTituloTreinoAtual")
        self.lbExAtual = QtWidgets.QLabel(self.centralwidget)
        self.lbExAtual.setGeometry(QtCore.QRect(250, 70, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbExAtual.setFont(font)
        self.lbExAtual.setStyleSheet("color: rgb(255, 85, 0);")
        self.lbExAtual.setObjectName("lbExAtual")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 60, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 127);")
        self.label_3.setObjectName("label_3")
        self.lbQuantEx = QtWidgets.QLabel(self.centralwidget)
        self.lbQuantEx.setGeometry(QtCore.QRect(300, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbQuantEx.setFont(font)
        self.lbQuantEx.setStyleSheet("color: rgb(255, 85, 0);")
        self.lbQuantEx.setObjectName("lbQuantEx")
        self.lbNomeExe = QtWidgets.QLabel(self.centralwidget)
        self.lbNomeExe.setGeometry(QtCore.QRect(250, 120, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbNomeExe.setFont(font)
        self.lbNomeExe.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.lbNomeExe.setObjectName("lbNomeExe")
        self.maExercicio = QtWidgets.QMdiArea(self.centralwidget)
        self.maExercicio.setGeometry(QtCore.QRect(100, 180, 391, 241))
        self.maExercicio.setObjectName("maExercicio")
        self.lcdTimer = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdTimer.setGeometry(QtCore.QRect(220, 430, 141, 41))
        self.lcdTimer.setStyleSheet("color: rgb(255, 85, 0);")
        self.lcdTimer.setObjectName("lcdTimer")
        self.btnPause = QtWidgets.QPushButton(self.centralwidget)
        self.btnPause.setGeometry(QtCore.QRect(140, 500, 151, 41))
        self.btnPause.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);")
        self.btnPause.setObjectName("btnPause")
        self.btnProximo = QtWidgets.QPushButton(self.centralwidget)
        self.btnProximo.setGeometry(QtCore.QRect(310, 500, 151, 41))
        self.btnProximo.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"color: rgb(0, 0, 0);")
        self.btnProximo.setObjectName("btnProximo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        data_atual = date.today()
        data_em_texto = data_atual.strftime('%d/%m/%Y')
        self.lbTituloTreinoAtual.setText(_translate("MainWindow", str(data_em_texto)))
        self.lbExAtual.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "/"))
        self.lbQuantEx.setText(_translate("MainWindow", ""))
        self.lbNomeExe.setText(_translate("MainWindow", "Nome"))
        self.btnPause.setText(_translate("MainWindow", "Pause"))
        self.btnProximo.setText(_translate("MainWindow", "Proximo"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

