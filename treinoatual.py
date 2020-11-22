# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treinoatual.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(800, 800))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setStyleSheet("background-color: rgba(39, 78, 118, 200);\n"
"")
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
        self.lbExAtual.setGeometry(QtCore.QRect(370, 160, 31, 21))
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
        self.lbQuantEx.setGeometry(QtCore.QRect(410, 160, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbQuantEx.setFont(font)
        self.lbQuantEx.setStyleSheet("color: rgb(255, 85, 0);")
        self.lbQuantEx.setAlignment(QtCore.Qt.AlignCenter)
        self.lbQuantEx.setObjectName("lbQuantEx")
        self.lbNomeExe = QtWidgets.QLabel(self.centralwidget)
        self.lbNomeExe.setGeometry(QtCore.QRect(210, 210, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbNomeExe.setFont(font)
        self.lbNomeExe.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.lbNomeExe.setAlignment(QtCore.Qt.AlignCenter)
        self.lbNomeExe.setObjectName("lbNomeExe")
        self.btnPause = QtWidgets.QPushButton(self.centralwidget)
        self.btnPause.setGeometry(QtCore.QRect(360, 629, 100, 50))
        self.btnPause.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.btnPause.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("playPause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPause.setIcon(icon)
        self.btnPause.setIconSize(QtCore.QSize(20, 20))
        self.btnPause.setObjectName("btnPause")
        self.btnProximo = QtWidgets.QPushButton(self.centralwidget)
        self.btnProximo.setGeometry(QtCore.QRect(490, 630, 100, 50))
        self.btnProximo.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.btnProximo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnProximo.setIcon(icon1)
        self.btnProximo.setIconSize(QtCore.QSize(20, 20))
        self.btnProximo.setObjectName("btnProximo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 260, 381, 271))
        self.label.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Login_imagem.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 61, 51))
        self.pushButton.setStyleSheet("border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 0px;")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("voltarIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(60, 60))
        self.pushButton.setObjectName("pushButton")
        self.lblCronometro = QtWidgets.QLabel(self.centralwidget)
        self.lblCronometro.setGeometry(QtCore.QRect(310, 560, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblCronometro.setFont(font)
        self.lblCronometro.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(86, 116, 148);\n"
"color: rgb(255, 85, 0);\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.lblCronometro.setText("")
        self.lblCronometro.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCronometro.setObjectName("lblCronometro")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 630, 100, 50))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.pushButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("voltar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.btnLogout = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogout.setGeometry(QtCore.QRect(650, 10, 141, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnLogout.setFont(font)
        self.btnLogout.setStyleSheet("\n"
"border-style: outset;\n"
"border-width: 0px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("sair.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogout.setIcon(icon4)
        self.btnLogout.setIconSize(QtCore.QSize(40, 40))
        self.btnLogout.setObjectName("btnLogout")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbTituloTreinoAtual.setText(_translate("MainWindow", "Dia"))
        self.lbExAtual.setText(_translate("MainWindow", "99"))
        self.label_3.setText(_translate("MainWindow", "/"))
        self.lbQuantEx.setText(_translate("MainWindow", "99"))
        self.lbNomeExe.setText(_translate("MainWindow", "Nome"))
        self.btnLogout.setText(_translate("MainWindow", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
