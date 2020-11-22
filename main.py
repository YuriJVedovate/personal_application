#importa bibliotecas
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3

from datetime import date
import datetime



#arquivos das telas
import login
import cadastro
import treino
import treinoatual


 # cria classe chamada Controller
class Controller: 
    
    contador = 0
    contadorplayStop = 0
    quantidade_Exercicio = 0
    exercicios = ""

    def __init__(self):
        # configurações para importação de telas 
        self.login_Window = QtWidgets.QMainWindow()
        self.login_ui = login.Ui_MainWindow()
        self.login_ui.setupUi(self.login_Window)
        # ao clicar no botão "btnLogin" leva para função verificar_login
        self.login_ui.btnLogin.clicked.connect(self.verificar_login)
        # ao clicar no botão "btnCadastrar" leva para função show_cadastrar
        self.login_ui.btnCadastrar.clicked.connect(self.show_cadastrar)
        self.login_ui.btnCadastrar.clicked.connect(self.login_Window.close)
        
    
        self.cadastro_Window = QtWidgets.QMainWindow()
        self.cadastro_ui = cadastro.Ui_MainWindow()
        self.cadastro_ui.setupUi(self.cadastro_Window)
        self.cadastro_ui.btnCadastrar.clicked.connect(self.cadastrar)
        self.cadastro_ui.btnVoltar.clicked.connect(self.show_login)
        self.cadastro_ui.btnVoltar.clicked.connect(self.cadastro_Window.close)
        
    
        self.treino_Window = QtWidgets.QMainWindow()
        self.treino_ui = treino.Ui_MainWindow()
        self.treino_ui.setupUi(self.treino_Window)
        self.treino_ui.btnComecar.clicked.connect(self.show_treinoAtual)
        self.treino_ui.btnComecar.clicked.connect(self.treino_Window.close)
        self.treino_ui.btnLogout.clicked.connect(self.Logout)
        self.treino_ui.btnLogout.clicked.connect(self.treino_Window.close)
        
    
        self.treinoatual_Window = QtWidgets.QMainWindow()
        self.treinoatual_ui = treinoatual.Ui_MainWindow()
        self.treinoatual_ui.setupUi(self.treinoatual_Window)
        self.treinoatual_ui.pushButton.clicked.connect(self.show_treino)
        self.treinoatual_ui.pushButton.clicked.connect(self.treinoatual_Window.close)
        self.treinoatual_ui.btnProximo.clicked.connect(self.ProxExercicio)
        self.treinoatual_ui.pushButton_2.clicked.connect(self.VoltaExercicio)
        self.treinoatual_ui.btnPause.clicked.connect(self.playStop)
        self.treinoatual_ui.btnLogout.clicked.connect(self.Logout)
        self.treinoatual_ui.btnLogout.clicked.connect(self.treinoatual_Window.close)
        
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.showTime)
    
    
    
    def Logout(self):
        self.login_ui.leNomeLogin.setText("")
        self.login_ui.leSenhaLogin.setText("")
        self.login_ui.lblErroLogin.setText("")
        
        self.contador = 0
        self.contadorplayStop = 0
        self.quantidade_Exercicio = 0
        self.exercicios = ""
        
        self.show_login()
        
        
    
    
    """
    função show_login:
        mostra tela login
        ao clicar no botão "btnLogin" leva para função verificar_login
        ao clicar no botão "btnCadastrar" leva para função show_cadastrar e fecha tela de login
        
    """
    
    def show_login(self):
        self.login_Window.show()
        
    """
    função verificar_login:
        adiciona a variavel nomeLogin o valor digitado na LineEdit
        adiciona a variavel senhaLogin o valor digitado na LineEdit
        
        banco recebe a conexão com um banco chamado Banco.db
        
        tente:
            buscar no banco uma senha da tabela Usuario quando o nome for igual o nome digitado
            cria variavel senha_bd que recebe a senha retornada do banco
            fecho a conecção com o banco
        se der errado:
            envia uma mensagem de erro para o terminal 
            
        verifica se a senha digitada é a mesma senha do usuario recebida pelo banco:
            fechar a tela de login
            abrir a tela de treino
            define o campo User da tela de treino para o usuario logado
        se não:
            mostra mensagem de eero para o usuario
           
    """
        
    def verificar_login(self):
        nomeLogin = self.login_ui.leNomeLogin.text()
        senhaLogin = self.login_ui.leSenhaLogin.text()
        
        banco = sqlite3.connect('Banco.db')
        cursor = banco.cursor()
        
        cursor.execute("SELECT senha FROM Usuario WHERE nome = '{}'".format(nomeLogin))
        senha_bd = cursor.fetchall()
        banco.close() 
       
        if senha_bd != []:
            if senhaLogin == senha_bd[0][0]:
                self.login_ui.leNomeLogin.setText("")
                self.login_ui.leSenhaLogin.setText("")
                
                self.login_Window.close()
                self.show_treino()
            
                self.treino_ui.lblNomeUser.setText(nomeLogin)
            
            else:
                self.login_ui.lblErroLogin.setText("login ou senha incorreto")
                
        else:
            self.login_ui.lblErroLogin.setText("login não existe")
            
        
        
            
        
    """
    função show_cadastrar:
        mostra tela de cadastro
        ao clicar no botão "btnCadastrar" leva para função cadastrar
        ao clicar no botão "btnVoltar" leva para função show_login (volta para tela de login e fecha a tela de cadastro)
    """
        
    def show_cadastrar(self):
        self.cadastro_Window.show()
        
    
    """
    função cadastrar:
        adiciona a variavel nome o valor digitado na LineEdit leNomeCadastro
        adiciona a variavel email o valor digitado na LineEdit leEmailCadastro
        adiciona a variavel senha o valor digitado na LineEdit leSenhaCadastro
        adiciona a variavel c_senha o valor digitado na LineEdit leConfirmarSenhaCadastro
        
        verifica se senha é igual a confirmar senha:
            tentar:
                conectar com o banco
                insitir na tabela Usuario os valores digitados
                fecha conexão com o banco
                mostra mensagem de sucesso para usuario com settext
                abre tela de login e fecha tela de cadastro
            se der errado:
                envia uma mensagem de erro para o terminal 
                
        se as senhas forem diferentes:
            
            mostra mensagem de erro para usuario 
            limpa todos valores dos campos
            
    """
     
    def cadastrar(self):
        
        nome = self.cadastro_ui.leNomeCadastro.text()
        email = self.cadastro_ui.leEmailCadastro.text()
        senha = self.cadastro_ui.leSenhaCadastro.text()
        c_senha = self.cadastro_ui.leConfirmarSenhaCadastro.text()
        
        
        if( (nome.strip() and len(nome) >= 5) and (email.strip() and len(email) >= 10) and (senha.strip() and len(senha) >= 8 ) and senha == c_senha):
            try:
                banco = sqlite3.connect('Banco.db')
                cursor = banco.cursor()
                cursor.execute("INSERT INTO usuario VALUES (null,'{}', '{}', '{}')".format(nome, email, senha))
                
                banco.commit()
                banco.close()
                self.cadastro_ui.lblErroCadastro.setText("Usuario cadastrado com sucesso")
                self.cadastro_ui.lblErroCadastro.setText("")
                
                self.login_Window.show()
                self.cadastro_Window.close()
                
            except sqlite3.Error as erro:
                print("Erro ao inserir os dados: ", erro)
                
        else:
            self.cadastro_ui.lblErroCadastro.setText("Campos Invalidos")
            self.cadastro_ui.leNomeCadastro.setText("")
            self.cadastro_ui.leEmailCadastro.setText("")
            self.cadastro_ui.leSenhaCadastro.setText("")
            self.cadastro_ui.leConfirmarSenhaCadastro.setText("")
            
    """
    função show_treino:
        mostra tela de treino
        
        pega dia atual e diua anterior e substitui nas labels de dia e dia anterior
        
        ao clicar no botão "btnComecar" leva para função show_treinoAtual
        ao clicar no botão "btnComecar" fecha tela de treino
    """
    
    def show_treino(self):
        self.treino_Window.show()
        
        date_now = datetime.datetime.now()
        yesterday = date_now - datetime.timedelta(days=1)
        self.treino_ui.lblDataAtual.setText(date_now.strftime("%d/%m/%y"))
        self.treino_ui.lblDiaAnterior.setText(yesterday.strftime("%d/%m/%y"))
        
        
    
    """
    função show_treinoAtual:
        mostra tela de treinoatual
        
        ao clicar no botão "pushButton" leva para função show_treino e fecha tela de treino atual
        
        pega data atual e subistitui na label dia
        
        criando cronometro 
    """
    def show_treinoAtual(self):
        self.treinoatual_Window.show()
        
        data_atual = date.today()
        data_em_texto = str(data_atual.strftime('%d/%m/%Y'))
        self.treinoatual_ui.lbTituloTreinoAtual.setText(data_em_texto)
        
        banco = sqlite3.connect('Banco.db')
        cursor = banco.cursor()
        
        cursor.execute("select count(IdEx) from exercicio")
        self.quantidade_Exercicio = cursor.fetchall()
        
        self.treinoatual_ui.lbQuantEx.setText(str(self.quantidade_Exercicio[0][0]))
        
        cursor.execute("select * from exercicio")
        self.exercicios = cursor.fetchall()
        
        self.treinoatual_ui.lbExAtual.setText(str(self.exercicios[self.contador][4]))
        self.treinoatual_ui.lbNomeExe.setText(str(self.exercicios[self.contador][2]))
        
        self.treinoatual_ui.label.setPixmap(QtGui.QPixmap( str(self.exercicios[self.contador][3])))
        self.treinoatual_ui.label.setScaledContents(True)
        
        self.segundos = self.exercicios[self.contador][5]
    
        self.treinoatual_ui.lblCronometro.setText("00:00:" + str(self.segundos))
        
        
        
        
        if (self.contador == 0 ):
            self.treinoatual_ui.pushButton_2.setStyleSheet("background-color: rgb(86, 116, 148);\n"
                                                           "border-radius: 15px;\n"
                                                           "border-style: outset;\n"
                                                           "border-width: 2px;")
        else:
            self.treinoatual_ui.pushButton_2.setStyleSheet("background-color: rgb(255, 85, 0);\n"
                                                           "border-radius: 15px;\n"
                                                           "border-style: outset;\n"
                                                           "border-width: 2px;")
        
        
        if ((self.contador + 1) == self.quantidade_Exercicio[0][0]):
            self.treinoatual_ui.btnProximo.setStyleSheet("background-color: rgb(86, 116, 148);\n"
                                                         "border-radius: 15px;\n"
                                                         "border-style: outset;\n"
                                                         "border-width: 2px;")
            
        else:
            self.treinoatual_ui.btnProximo.setStyleSheet("background-color: rgb(255, 85, 0);\n"
                                                         "border-radius: 15px;\n"
                                                         "border-style: outset;\n"
                                                         "border-width: 2px;")
        
        
            
        
        
        
    def ProxExercicio(self):
        
        if ((self.contador + 1) == self.quantidade_Exercicio[0][0]):
            pass
        
        else:
            self.contador += 1
            self.timer.stop()
            self.treinoatual_ui.btnPause.setStyleSheet("background-color: rgb(255, 85, 0);\n"
                                                         "border-radius: 15px;\n"
                                                         "border-style: outset;\n"
                                                         "border-width: 2px;")  
            
        self.show_treinoAtual()
    
    def VoltaExercicio(self):
        
        if (self.contador == 0 ):
            pass
            
        else:
            self.contador -= 1
            self.timer.stop()
            self.treinoatual_ui.btnPause.setStyleSheet("background-color: rgb(255, 85, 0);\n"
                                                         "border-radius: 15px;\n"
                                                         "border-style: outset;\n"
                                                         "border-width: 2px;")            
            
        self.show_treinoAtual()
        
        
        
    def playStop(self):
        
        self.contadorplayStop += 1
        if (self.contadorplayStop % 2 == 1):
            self.treinoatual_ui.btnPause.setStyleSheet("background-color: rgb(86, 116, 148);\n"
                                                         "border-radius: 15px;\n"
                                                         "border-style: outset;\n"
                                                         "border-width: 2px;")
            self.timer.start(1000)
        else:
            self.treinoatual_ui.btnPause.setStyleSheet("background-color: rgb(255, 85, 0);\n"
                                                         "border-radius: 15px;\n"
                                                         "border-style: outset;\n"
                                                         "border-width: 2px;")
            self.timer.stop()
        
        
    def showTime(self):
        hora = self.segundos // 3600
        minuto = (self.segundos % 3600) // 60
        segundo = (self.segundos % 3600) % 60
        
        timeDisplay = "%02i:%02i:%02i"%(hora,minuto,segundo)
        self.treinoatual_ui.lblCronometro.setText(timeDisplay)
        self.segundos = self.segundos - 1
        
        if self.segundos < 0:
            self.timer.stop()
            print("\a")
        
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())
