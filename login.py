# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 321, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblTituloLogin = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lblTituloLogin.setFont(font)
        self.lblTituloLogin.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.lblTituloLogin.setObjectName("lblTituloLogin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblTituloLogin)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.lblNomeLogin = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblNomeLogin.setFont(font)
        self.lblNomeLogin.setStyleSheet("color: rgb(255, 85, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.lblNomeLogin.setObjectName("lblNomeLogin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblNomeLogin)
        self.leNomeLogin = QtWidgets.QLineEdit(self.layoutWidget)
        self.leNomeLogin.setStyleSheet("border-color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(255, 85, 0);")
        self.leNomeLogin.setObjectName("leNomeLogin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.leNomeLogin)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole, spacerItem1)
        self.lblSenhaLogin = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblSenhaLogin.setFont(font)
        self.lblSenhaLogin.setStyleSheet("color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(0, 0, 0);")
        self.lblSenhaLogin.setObjectName("lblSenhaLogin")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblSenhaLogin)
        self.leSenhaLogin = QtWidgets.QLineEdit(self.layoutWidget)
        self.leSenhaLogin.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 85, 0);\n"
"gridline-color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(255, 85, 0);")
        self.leSenhaLogin.setObjectName("leSenhaLogin")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.leSenhaLogin)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.btnLogin = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.btnLogin.setObjectName("btnLogin")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.btnLogin)
        self.btnCadastrar = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnCadastrar.setFont(font)
        self.btnCadastrar.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.btnCadastrar)
        self.lbImagemFundo = QtWidgets.QLabel(self.centralwidget)
        self.lbImagemFundo.setGeometry(QtCore.QRect(0, 0, 605, 601))
        self.lbImagemFundo.setText("")
        self.lbImagemFundo.setPixmap(QtGui.QPixmap("Login_imagem.png"))
        self.lbImagemFundo.setScaledContents(True)
        self.lbImagemFundo.setObjectName("lbImagemFundo")
        self.lbImagemFundo.raise_()
        self.layoutWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "login"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.lblTituloLogin.setText(_translate("MainWindow", "LOGIN"))
        self.lblNomeLogin.setText(_translate("MainWindow", "Nome:"))
        self.lblSenhaLogin.setText(_translate("MainWindow", "Senha:"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
        self.btnCadastrar.setText(_translate("MainWindow", "Cadastrar?"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

