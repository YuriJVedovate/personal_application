
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setStyleSheet("background-color: rgb(42, 79, 120);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblCadastrar = QtWidgets.QLabel(self.centralwidget)
        self.lblCadastrar.setGeometry(QtCore.QRect(315, 90, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lblCadastrar.setFont(font)
        self.lblCadastrar.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.lblCadastrar.setObjectName("lblCadastrar")
        self.lblNomeCadastro = QtWidgets.QLabel(self.centralwidget)
        self.lblNomeCadastro.setGeometry(QtCore.QRect(220, 160, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblNomeCadastro.setFont(font)
        self.lblNomeCadastro.setStyleSheet("color: rgb(255, 85, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.lblNomeCadastro.setObjectName("lblNomeCadastro")
        self.leNomeCadastro = QtWidgets.QLineEdit(self.centralwidget)
        self.leNomeCadastro.setGeometry(QtCore.QRect(210, 200, 381, 35))
        self.leNomeCadastro.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 85, 0);\n"
"gridline-color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(255, 85, 0); \n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.leNomeCadastro.setObjectName("leNomeCadastro")
        self.lblEmailCadastro = QtWidgets.QLabel(self.centralwidget)
        self.lblEmailCadastro.setGeometry(QtCore.QRect(220, 260, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblEmailCadastro.setFont(font)
        self.lblEmailCadastro.setStyleSheet("color: rgb(255, 85, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.lblEmailCadastro.setObjectName("lblEmailCadastro")
        self.leEmailCadastro = QtWidgets.QLineEdit(self.centralwidget)
        self.leEmailCadastro.setGeometry(QtCore.QRect(210, 300, 381, 35))
        self.leEmailCadastro.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 85, 0);\n"
"gridline-color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(255, 85, 0); \n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.leEmailCadastro.setObjectName("leEmailCadastro")
        self.lblSenhaCadastro = QtWidgets.QLabel(self.centralwidget)
        self.lblSenhaCadastro.setGeometry(QtCore.QRect(220, 370, 60, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblSenhaCadastro.setFont(font)
        self.lblSenhaCadastro.setStyleSheet("color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(0, 0, 0);")
        self.lblSenhaCadastro.setObjectName("lblSenhaCadastro")
        self.leSenhaCadastro = QtWidgets.QLineEdit(self.centralwidget)
        self.leSenhaCadastro.setGeometry(QtCore.QRect(210, 400, 381, 35))
        self.leSenhaCadastro.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 85, 0);\n"
"gridline-color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(255, 85, 0); \n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.leSenhaCadastro.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leSenhaCadastro.setObjectName("leSenhaCadastro")
        self.leConfirmarSenhaCadastro = QtWidgets.QLineEdit(self.centralwidget)
        self.leConfirmarSenhaCadastro.setGeometry(QtCore.QRect(210, 490, 381, 35))
        self.leConfirmarSenhaCadastro.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 85, 0);\n"
"gridline-color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(255, 85, 0); \n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.leConfirmarSenhaCadastro.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leConfirmarSenhaCadastro.setObjectName("leConfirmarSenhaCadastro")
        self.lblSenhaLogin = QtWidgets.QLabel(self.centralwidget)
        self.lblSenhaLogin.setGeometry(QtCore.QRect(220, 460, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblSenhaLogin.setFont(font)
        self.lblSenhaLogin.setStyleSheet("color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(0, 0, 0);")
        self.lblSenhaLogin.setObjectName("lblSenhaLogin")
        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(210, 600, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.btnCadastrar.setFont(font)
        self.btnCadastrar.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.lblErroCadastro = QtWidgets.QLabel(self.centralwidget)
        self.lblErroCadastro.setGeometry(QtCore.QRect(160, 550, 471, 29))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblErroCadastro.setFont(font)
        self.lblErroCadastro.setStyleSheet("color: rgb(255, 85, 0);")
        self.lblErroCadastro.setAlignment(QtCore.Qt.AlignCenter)
        self.lblErroCadastro.setObjectName("lblErroCadastro")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 196, 41, 41))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("UserIcon.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 295, 41, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("EmailIcon.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 397, 41, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("PasswordIcon.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 487, 41, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("PasswordIcon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.btnVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.btnVoltar.setGeometry(QtCore.QRect(0, 3, 61, 51))
        self.btnVoltar.setStyleSheet("\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 0px;")
        self.btnVoltar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("voltarIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVoltar.setIcon(icon)
        self.btnVoltar.setIconSize(QtCore.QSize(60, 60))
        self.btnVoltar.setDefault(True)
        self.btnVoltar.setFlat(True)
        self.btnVoltar.setObjectName("btnVoltar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblCadastrar.setText(_translate("MainWindow", "Cadastro"))
        self.lblNomeCadastro.setText(_translate("MainWindow", "Nome:"))
        self.lblEmailCadastro.setText(_translate("MainWindow", "Email:"))
        self.lblSenhaCadastro.setText(_translate("MainWindow", "Senha:"))
        self.lblSenhaLogin.setText(_translate("MainWindow", "Confirmar senha:"))
        self.btnCadastrar.setText(_translate("MainWindow", "Cadastrar"))
        self.lblErroCadastro.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

