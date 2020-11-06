from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 800))
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgba(39, 78, 118, 200);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.lblErroLogin = QtWidgets.QLabel(self.centralwidget)
        self.lblErroLogin.setGeometry(QtCore.QRect(135, 430, 531, 29))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblErroLogin.setFont(font)
        self.lblErroLogin.setStyleSheet("color: rgb(255, 85, 0);")
        self.lblErroLogin.setAlignment(QtCore.Qt.AlignCenter)
        self.lblErroLogin.setObjectName("lblErroLogin")
        self.lblCadastrar = QtWidgets.QLabel(self.centralwidget)
        self.lblCadastrar.setGeometry(QtCore.QRect(150, 630, 228, 29))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblCadastrar.setFont(font)
        self.lblCadastrar.setStyleSheet("color: rgb(0, 0, 0);")
        self.lblCadastrar.setObjectName("lblCadastrar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 246, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("UserIcon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 366, 41, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("PasswordIcon.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.btnCadastrar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCadastrar.setGeometry(QtCore.QRect(400, 623, 221, 41))
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
        self.lblSenhaLogin = QtWidgets.QLabel(self.centralwidget)
        self.lblSenhaLogin.setGeometry(QtCore.QRect(220, 340, 60, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.lblSenhaLogin.setFont(font)
        self.lblSenhaLogin.setStyleSheet("color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(0, 0, 0);")
        self.lblSenhaLogin.setObjectName("lblSenhaLogin")
        self.leNomeLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.leNomeLogin.setGeometry(QtCore.QRect(210, 250, 381, 35))
        self.leNomeLogin.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 85, 0);\n"
"gridline-color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(255, 85, 0); \n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.leNomeLogin.setObjectName("leNomeLogin")
        self.lblTituloLogin = QtWidgets.QLabel(self.centralwidget)
        self.lblTituloLogin.setGeometry(QtCore.QRect(340, 130, 124, 45))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lblTituloLogin.setFont(font)
        self.lblTituloLogin.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"color: rgb(255, 85, 0);")
        self.lblTituloLogin.setObjectName("lblTituloLogin")
        self.lblNomeLogin = QtWidgets.QLabel(self.centralwidget)
        self.lblNomeLogin.setGeometry(QtCore.QRect(220, 220, 56, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblNomeLogin.setFont(font)
        self.lblNomeLogin.setStyleSheet("color: rgb(255, 85, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.lblNomeLogin.setObjectName("lblNomeLogin")
        self.leSenhaLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.leSenhaLogin.setGeometry(QtCore.QRect(210, 370, 381, 35))
        self.leSenhaLogin.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 85, 0);\n"
"gridline-color: rgb(255, 85, 0);\n"
"selection-background-color: rgb(255, 85, 0); \n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.leSenhaLogin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leSenhaLogin.setObjectName("leSenhaLogin")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(200, 470, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.btnLogin.setObjectName("btnLogin")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "login"))
        MainWindow.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><br/></p><p><br/></p></body></html>"))
        self.lblErroLogin.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lblCadastrar.setText(_translate("MainWindow", "não tem cadastro?"))
        self.btnCadastrar.setText(_translate("MainWindow", "Cadastrar?"))
        self.lblSenhaLogin.setText(_translate("MainWindow", "Senha:"))
        self.lblTituloLogin.setText(_translate("MainWindow", "LOGIN"))
        self.lblNomeLogin.setText(_translate("MainWindow", "Nome:"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

