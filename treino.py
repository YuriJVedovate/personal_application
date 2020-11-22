# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'treino.ui'
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
        self.TelaTreinos = QtWidgets.QWidget(MainWindow)
        self.TelaTreinos.setObjectName("TelaTreinos")
        self.lblTituloTreinos = QtWidgets.QLabel(self.TelaTreinos)
        self.lblTituloTreinos.setGeometry(QtCore.QRect(330, 120, 138, 45))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lblTituloTreinos.setFont(font)
        self.lblTituloTreinos.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.lblTituloTreinos.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTituloTreinos.setObjectName("lblTituloTreinos")
        self.lblDataAtual = QtWidgets.QLabel(self.TelaTreinos)
        self.lblDataAtual.setGeometry(QtCore.QRect(330, 260, 138, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblDataAtual.setFont(font)
        self.lblDataAtual.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.lblDataAtual.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDataAtual.setObjectName("lblDataAtual")
        self.btnComecar = QtWidgets.QPushButton(self.TelaTreinos)
        self.btnComecar.setGeometry(QtCore.QRect(130, 320, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btnComecar.setFont(font)
        self.btnComecar.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.btnComecar.setObjectName("btnComecar")
        self.lblDiaAnterior = QtWidgets.QLabel(self.TelaTreinos)
        self.lblDiaAnterior.setGeometry(QtCore.QRect(330, 500, 138, 45))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lblDiaAnterior.setFont(font)
        self.lblDiaAnterior.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.lblDiaAnterior.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDiaAnterior.setObjectName("lblDiaAnterior")
        self.btnVisualizar = QtWidgets.QPushButton(self.TelaTreinos)
        self.btnVisualizar.setGeometry(QtCore.QRect(130, 560, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btnVisualizar.setFont(font)
        self.btnVisualizar.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.btnVisualizar.setObjectName("btnVisualizar")
        self.label_3 = QtWidgets.QLabel(self.TelaTreinos)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("UserIcon.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.lblNomeUser = QtWidgets.QLabel(self.TelaTreinos)
        self.lblNomeUser.setGeometry(QtCore.QRect(60, 16, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblNomeUser.setFont(font)
        self.lblNomeUser.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.lblNomeUser.setObjectName("lblNomeUser")
        self.btnLogout = QtWidgets.QPushButton(self.TelaTreinos)
        self.btnLogout.setGeometry(QtCore.QRect(650, 10, 141, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btnLogout.setFont(font)
        self.btnLogout.setStyleSheet("\n"
"border-style: outset;\n"
"border-width: 0px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sair.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogout.setIcon(icon)
        self.btnLogout.setIconSize(QtCore.QSize(40, 40))
        self.btnLogout.setObjectName("btnLogout")
        MainWindow.setCentralWidget(self.TelaTreinos)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblTituloTreinos.setText(_translate("MainWindow", "Treinos"))
        self.lblDataAtual.setText(_translate("MainWindow", "Hoje"))
        self.btnComecar.setText(_translate("MainWindow", "Começar"))
        self.lblDiaAnterior.setText(_translate("MainWindow", "Anteriores"))
        self.btnVisualizar.setText(_translate("MainWindow", "Visualizar"))
        self.lblNomeUser.setText(_translate("MainWindow", "User"))
        self.btnLogout.setText(_translate("MainWindow", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
