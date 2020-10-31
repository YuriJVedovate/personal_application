import sys
from PyQt5 import QtWidgets

# QtCore, QtGui,

#arquivos das telas
import login
import treino
import treinoatual
import sqlite3

exercicioAtual = 1

msg = QtWidgets.QMessageBox() 
msg.setIcon(QtWidgets.QMessageBox.Critical) 
msg.setText("login incorreto") 
msg.setInformativeText('Este login não foi encontrado') 
msg.setWindowTitle("Error")  

# class Connect(object):

#     def __init__(self, Banco):
#         try:
#             # conectando...
#             self.conn = sqlite3.connect(Banco)
#             self.cursor = self.conn.cursor()
#             # imprimindo nome do banco
#             print("Banco:", Banco)
#             # lendo a versão do SQLite
#             self.cursor.execute('SELECT SQLITE_VERSION()')
#             self.data = self.cursor.fetchone()
#             # imprimindo a versão do SQLite
#             print("SQLite version: %s" % self.data)
#         except sqlite3.Error:
#             print("Erro ao abrir banco.")
#             return False

#         def close_db(self):
#             if self.conn:
#                 self.conn.close()
#                 print("Conexão fechada.")
                
# class BancoDb(object):

#     def __init__(self):
#         self.db = Connect('Banco.db')

#     def close_connection(self):
#         self.db.close_db()  
        
# if __name__ == '__main__':
#     Banco = BancoDb()
#     Banco.close_connection()


    
                  
class Controller:

    def show_login(self):
        self.login_Window = QtWidgets.QMainWindow()
        self.login_ui = login.Ui_MainWindow()
        self.login_ui.setupUi(self.login_Window)
        self.login_Window.show()
        self.login_ui.btnLogin.clicked.connect(self.verificar_login)
        
    def verificar_login(self):
        nomeLogin = self.login_ui.leNomeLogin.text()
        senhaLogin = self.login_ui.leSenhaLogin.text()  
        conn = sqlite3.connect('Banco.db')
        cursor = conn.cursor()
        resultado = cursor.execute("""SELECT * FROM Usuario WHERE nome = ? or senha=?""",(nomeLogin, senhaLogin))
        
        for Usuario in resultado.fetchall():
            print(Usuario)
        
        if cursor.fetchone is not None:
            self.show_treino()
        else:
            msg.exec_()  
        
        
        
    def show_treino(self): 
        self.treino_Window = QtWidgets.QMainWindow()
        self.treino_ui = treino.Ui_MainWindow()
        self.treino_ui.setupUi(self.treino_Window)
        self.treino_ui.btnComecar.clicked.connect(self.show_treinos)
        self.login_Window.close() 
        self.treino_Window.show()
    
    def show_treinos(self):
        self.treinoatual_Window = QtWidgets.QMainWindow()
        self.treinoatual_ui = treinoatual.Ui_MainWindow()
        self.treinoatual_ui.setupUi(self.treinoatual_Window)
        self.treino_Window.close()
        self.treinoatual_Window.show()
        self.treinoatual_ui.lbExAtual.setText(str(exercicioAtual))
        self.treinoatual_ui.lbQuantEx.setText(str(14))
        
        
       
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())
