# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treinos.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.TelaTreinos = QtWidgets.QWidget(MainWindow)
        self.TelaTreinos.setObjectName("TelaTreinos")
        self.lblTituloTreinos = QtWidgets.QLabel(self.TelaTreinos)
        self.lblTituloTreinos.setGeometry(QtCore.QRect(10, 10, 138, 45))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lblTituloTreinos.setFont(font)
        self.lblTituloTreinos.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.lblTituloTreinos.setObjectName("lblTituloTreinos")
        self.lnLinhaTitulo = QtWidgets.QFrame(self.TelaTreinos)
        self.lnLinhaTitulo.setGeometry(QtCore.QRect(10, 50, 551, 16))
        self.lnLinhaTitulo.setStyleSheet("color: rgb(0, 0, 0);")
        self.lnLinhaTitulo.setFrameShape(QtWidgets.QFrame.HLine)
        self.lnLinhaTitulo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lnLinhaTitulo.setObjectName("lnLinhaTitulo")
        self.lblDataAtual = QtWidgets.QLabel(self.TelaTreinos)
        self.lblDataAtual.setGeometry(QtCore.QRect(30, 100, 138, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblDataAtual.setFont(font)
        self.lblDataAtual.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.lblDataAtual.setObjectName("lblDataAtual")
        self.btnComecar = QtWidgets.QPushButton(self.TelaTreinos)
        self.btnComecar.setGeometry(QtCore.QRect(30, 140, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btnComecar.setFont(font)
        self.btnComecar.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.btnComecar.setObjectName("btnComecar")
        self.lblDiaAnterior = QtWidgets.QLabel(self.TelaTreinos)
        self.lblDiaAnterior.setGeometry(QtCore.QRect(30, 250, 138, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblDiaAnterior.setFont(font)
        self.lblDiaAnterior.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.lblDiaAnterior.setObjectName("lblDiaAnterior")
        self.btnVisualizar = QtWidgets.QPushButton(self.TelaTreinos)
        self.btnVisualizar.setGeometry(QtCore.QRect(30, 290, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btnVisualizar.setFont(font)
        self.btnVisualizar.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.btnVisualizar.setObjectName("btnVisualizar")
        self.scrollArea = QtWidgets.QScrollArea(self.TelaTreinos)
        self.scrollArea.setGeometry(QtCore.QRect(30, 426, 531, 151))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 529, 149))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.lbFeedBack = QtWidgets.QLabel(self.TelaTreinos)
        self.lbFeedBack.setGeometry(QtCore.QRect(30, 390, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lbFeedBack.setFont(font)
        self.lbFeedBack.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.lbFeedBack.setObjectName("lbFeedBack")
        MainWindow.setCentralWidget(self.TelaTreinos)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTituloTreinos.setText(_translate("MainWindow", "Treinos"))
        
        date_now = datetime.datetime.now()
        yesterday = date_now - datetime.timedelta(days=1)
        
        self.lblDataAtual.setText(_translate("MainWindow", date_now.strftime("%d/%m/%y")))
        self.lblDiaAnterior.setText(_translate("MainWindow", yesterday.strftime("%d/%m/%y")))
        
        self.btnComecar.setText(_translate("MainWindow", "Começar"))
        self.btnVisualizar.setText(_translate("MainWindow", "Visualizar"))
        self.lbFeedBack.setText(_translate("MainWindow", "FeedBack"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

