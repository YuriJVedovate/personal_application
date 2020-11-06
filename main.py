#importa bibliotecas
import sys
from PyQt5 import QtWidgets
import sqlite3
import datetime
from datetime import date


# from datetime import datetime, timedelta
# from sys import stdout
# from time import sleep


#arquivos das telas
import login
import cadastro
import treino
import treinoatual


 # cria classe chamada Controller
class Controller: 
    
    # configurações para importação de telas 
    login_Window = QtWidgets.QMainWindow()
    login_ui = login.Ui_MainWindow()
    login_ui.setupUi(login_Window)
    
    cadastro_Window = QtWidgets.QMainWindow()
    cadastro_ui = cadastro.Ui_MainWindow()
    cadastro_ui.setupUi(cadastro_Window)
    
    treino_Window = QtWidgets.QMainWindow()
    treino_ui = treino.Ui_MainWindow()
    treino_ui.setupUi(treino_Window)
    
    treinoatual_Window = QtWidgets.QMainWindow()
    treinoatual_ui = treinoatual.Ui_MainWindow()
    treinoatual_ui.setupUi(treinoatual_Window)
    
    
    
    
    """
    função show_login:
        mostra tela login
        ao clicar no botão "btnLogin" leva para função verificar_login
        ao clicar no botão "btnCadastrar" leva para função show_cadastrar e fecha tela de login
        
    """
    
    def show_login(self):
        # mostra tela login
        self.login_Window.show()
        # ao clicar no botão "btnLogin" leva para função verificar_login
        self.login_ui.btnLogin.clicked.connect(self.verificar_login)
        # ao clicar no botão "btnCadastrar" leva para função show_cadastrar
        self.login_ui.btnCadastrar.clicked.connect(self.show_cadastrar)
        self.login_ui.btnCadastrar.clicked.connect(self.login_Window.close)
         
    
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
        # adiciona a variavel nomeLogin o valor digitado na LineEdit
        nomeLogin = self.login_ui.leNomeLogin.text()
        # adiciona a variavel senhaLogin o valor digitado na LineEdit
        senhaLogin = self.login_ui.leSenhaLogin.text()
        
        
        banco = sqlite3.connect('Banco.db')
        cursor = banco.cursor()
        
        try:
            cursor.execute("SELECT senha FROM Usuario WHERE nome = '{}'".format(nomeLogin))
            senha_bd = cursor.fetchall()
            banco.close() 
        except:
            print("Erro para encontrar login")
            
            
        if senhaLogin == senha_bd[0][0]:
            self.login_Window.close()
            self.show_treino()
            
            self.treino_ui.lblNomeUser.setText(nomeLogin)
            
        else:
            self.login_ui.lblErroLogin.setText("login ou senha incorreto")
        
            
        
    """
    função show_cadastrar:
        mostra tela de cadastro
        ao clicar no botão "btnCadastrar" leva para função cadastrar
        ao clicar no botão "btnVoltar" leva para função show_login (volta para tela de login e fecha a tela de cadastro)
    """
        
    def show_cadastrar(self):
        self.cadastro_Window.show()
        
        self.cadastro_ui.btnCadastrar.clicked.connect(self.cadastrar)
        self.cadastro_ui.btnVoltar.clicked.connect(self.show_login)
        self.cadastro_ui.btnVoltar.clicked.connect(self.cadastro_Window.close)
        
    
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
        
        if(senha == c_senha):
            try:
                banco = sqlite3.connect('Banco.db')
                cursor = banco.cursor()
                cursor.execute("INSERT INTO Usuario VALUES ('"+nome+"','"+email+"','"+senha+"')")
                
                banco.commit()
                banco.close()
                self.cadastro_ui.lblErroCadastro.setText("Usuario cadastrado com sucesso")
                self.login_Window.show()
                self.cadastro_Window.close()
                
            except sqlite3.Error as erro:
                print("Erro ao inserir os dados: ", erro)
        else:
            self.cadastro_ui.lblErroCadastro.setText("As senhas digitadas estão diferentes")
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
        
        self.treino_ui.btnComecar.clicked.connect(self.show_treinoAtual)
        self.treino_ui.btnComecar.clicked.connect(self.treino_Window.close)
        
    
    """
    função show_treinoAtual:
        mostra tela de treinoatual
        
        ao clicar no botão "pushButton" leva para função show_treino e fecha tela de treino atual
        
        pega data atual e subistitui na label dia
        
        criando cronometro 
    """
    def show_treinoAtual(self):
        self.treinoatual_Window.show()
        
        self.treinoatual_ui.pushButton.clicked.connect(self.show_treino)
        self.treinoatual_ui.pushButton.clicked.connect(self.treinoatual_Window.close)
        
        
        data_atual = date.today()
        data_em_texto = data_atual.strftime('%d/%m/%Y')
        self.treinoatual_ui.lbTituloTreinoAtual.setText(str(data_em_texto))
        
        # segundos = 120 
        
        # tempo = timedelta(seconds=segundos)
        
        # while (str(tempo) != '0:00:00'):
        #     self.treinoatual_ui.timeEdit.setTime("\r%s"%tempo)
        #     stdout.flush()
        #     tempo = tempo - timedelta(seconds=1)
        #     sleep(1)
            
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())
