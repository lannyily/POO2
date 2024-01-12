import sys
import os
import socket
import threading
import hashlib
import mysql.connector as mysql

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import Qt, QUrl

from py.tela_login_adm import Ui_tela_login_adm
from py.tela_inicial_adm import Ui_tela_inicial_adm
from py.tela_login import Ui_tela_login_guia
from py.tela_conf_com_senha import Ui_tela_conf_com_senha

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()
        
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        
        self.tela_login_guia = Ui_tela_login_guia()
        self.tela_login_guia.setupUi(self.stack0)
        
        self.tela_login_admin = Ui_tela_login_adm()
        self.tela_login_admin.setupUi(self.stack1)
        
        self.tela_inicial_admin = Ui_tela_inicial_adm()
        self.tela_inicial_admin.setupUi(self.stack2)
        
        self.tela_conf_com_senha = Ui_tela_conf_com_senha()
        self.tela_conf_com_senha.setupUi(self.stack3)
        
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        
class Main(Ui_Main, QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        
        self.ip = '192.168.18.105'
        self.port = 1600
        self.addr = (self.ip, self.port)
        
        self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente_socket.connect(self.addr)
        
        tipo_usuario = 'funcionario'
        self.cliente_socket.send(tipo_usuario.encode())
        print(f'Tipo de usuário enviado para o sevidor: {tipo_usuario}')
        
        self.tela_login_guia.pushButton_entar_adm.clicked.connect(self.abrir_tela_login_admin)
        self.tela_login_guia.pushButton_2.clicked.connect(self.sair)
        
        self.tela_login_admin.pushButton_sair.clicked.connect(self.sair)
        self.tela_login_admin.pushButton.clicked.connect(self.entrar_no_sistema_admin)
        self.tela_login_admin.pushButton_sair_2.clicked.connect(self.abrir_tela_login_guia)
        
        self.tela_inicial_admin.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_inicial_admin.pushButton_redefinir_senha.clicked.connect(self.abrir_tela_conf_com_senha)
        
        self.tela_conf_com_senha.pushButton_sair_2.clicked.connect(self.abrir_tela_inicial)
    
    def sair(self):
        msg = 'sair'
        self.cliente_socket.send(msg.encode())
        
        resposta = self.cliente_socket.recv(1024).decode()
        if resposta.lower() == 'Desconectado pelo servidor':
            self.cliente_socket.close()     
        self.close()
        print('Saiu do sistema')  
        
    def sair_do_sistema(self):
        msg = f'sair'
        self.cliente_socket.send(msg.encode())
        resposta = self.cliente_socket.recv(1024).decode()
        print(f'Resposta recebida: {resposta}')
     
        if resposta.lower() == 'desconectado pelo servidor':
            self.cliente_socket.close() 
            self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.cliente_socket.connect(self.addr)
            self.abrir_tela_login()
        
    def entrar_no_sistema_admin(self):
        while True:
            print('Entrando no sistema...')
            senha = self.tela_login.lineEdit_senha.text()
            
            if senha:
                try:
                    print(f'Senha digitada: {senha}')
                    senha_md5 = hashlib.md5(senha.encode()).hexdigest()
                    mensagem = f'loginadmin;{senha_md5}'
                    self.cliente_socket.send(mensagem.encode())
                    print(f'Senha enviada para o servidor: {senha}')
                    
                    resposta = self.cliente_socket.recv(1024).decode()
                    print(f'Resposta do servidor: {resposta}')
                    
                    if resposta.lower() == 'login efetuado com sucesso':
                        self.tela_login.lineEdit_senha.setText('')
                        self.abrir_tela_inicial()
                        break
                    elif resposta.lower() == 'senha incorreta':
                        self.mostrar_mensagem_erro('Senha incorreta')
                        self.tela_login.lineEdit_senha.setText('')
                        break
                    else:
                        self.mostrar_mensagem_erro('Erro ao efetuar login')
                        self.tela_login.lineEdit_senha.setText('')
                        break
                except ConnectionResetError:
                    print("Conexão com o servidor foi perdida.")
                    self.mostrar_mensagem_erro("Conexão com o servidor foi perdida.")
                    self.sair()
                except Exception as e:
                    print(f"Erro ao conectar com o servidor: {e}")
                    self.mostrar_mensagem_erro("Erro ao conectar com o servidor. Verifique sua conexão.")
            else:
                self.mostrar_mensagem_erro('Senha não informada')
                break
        
    def abrir_tela_login_guia(self):
        self.QtStack.setCurrentIndex(0)  # Define a tela_login_guia como a tela ativa

    def abrir_tela_login_admin(self):
        self.QtStack.setCurrentIndex(1)
        
    def abrir_tela_inicial(self):
        self.QtStack.setCurrentIndex(2)
        
    def abrir_tela_conf_com_senha(self):
        self.stack3.show()
        
    def mostrar_mensagem_erro(self, mensagem):
        QMessageBox.critical(self, "...", mensagem)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())