import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
import mysql.connector as mysql
import socket
import threading

from cadastro import Cadastro
from classes import Conta, Ingresso_gratuito, Ingresso_pago

from tela_cadastro import Ui_tela_cadastro
from tela_inicial import Ui_tela_inicial
from tela_login import Ui_tela_login
from tela_perfil import Ui_tela_perfil
from tela_casa_polvora import Ui_tela_casa_polvora
from tela_casa_pol_reserva import Ui_tela_casa_pol_reserva

print('oi')

class Ui_Main(QtWidgets.QWidget):

    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()
        
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        
        self.tela_login = Ui_tela_login()
        self.tela_login.setupUi(self.stack0)
        
        self.tela_cadastro = Ui_tela_cadastro()
        self.tela_cadastro.setupUi(self.stack1)
        
        self.tela_inicial = Ui_tela_inicial()
        self.tela_inicial.setupUi(self.stack2)
        
        self.tela_casa_polvora = Ui_tela_casa_polvora()
        self.tela_casa_polvora.setupUi(self.stack3)
        
        self.tela_casa_polvora_reserva = Ui_tela_casa_pol_reserva()
        self.tela_casa_polvora_reserva.setupUi(self.stack4)
        
        self.tela_perfil = Ui_tela_perfil()
        self.tela_perfil.setupUi(self.stack5)
        
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        
class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        
        self.ip = '192.168.1.18'
        self.port = 1600
        self.addr = (self.ip, self.port)
        
        self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente_socket.connect(self.addr)

        self.tela_login.commandLinkButton_naoTemConta.clicked.connect(self.abrir_tela_cadastro)
        self.tela_login.pushButton_fechar.clicked.connect(self.sair)
        self.tela_login.pushButton_entrar.clicked.connect(self.login)

        self.tela_cadastro.pushButton_cadastrar.clicked.connect(self.cadastro)
        self.tela_cadastro.pushButton_voltar.clicked.connect(self.abrir_tela_login)
        self.tela_cadastro.pushButton_cancelar.clicked.connect(self.cancelar_cad)
        
        self.tela_inicial.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_inicial.pushButton_casa_pol.clicked.connect(self.abrir_tela_casa_polvora)
        self.tela_inicial.pushButton_perfil.clicked.connect(self.abrir_tela_perfil)
        
        self.tela_perfil.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_perfil.pushButton_voltar.clicked.connect(self.abrir_tela_inicial)
        
        self.tela_casa_polvora.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_casa_polvora.pushButton_voltar.clicked.connect(self.abrir_tela_inicial)
        self.tela_casa_polvora.pushButton.clicked.connect(self.abrir_tela_casa_polvora_reserva)
        
        self.tela_casa_polvora_reserva.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_casa_polvora_reserva.pushButton_voltar.clicked.connect(self.abrir_tela_casa_polvora)
        self.tela_casa_polvora_reserva.calendarWidget.selectionChanged.connect(self.calendario)
        
        self.email = ''

    def sair_do_sistema(self):
        self.abrir_tela_login()
        self.cliente_socket.close()
        print('saindo do sistema....')
    
    def login(self):
        email = self.tela_login.lineEdit_email.text()
        senha = self.tela_login.lineEdit_senha.text()

        if email != '' and senha != '':
            try: 
                mensagem = f"login;{email};{senha}"
                
                self.cliente_socket.send(mensagem.encode())
                print('1 - Mensagem enviada:', mensagem)

                resposta = self.cliente_socket.recv(1024).decode()
                print('2 - Resposta recebida:', resposta)

                if resposta.lower() == 'login bem-sucedido!':
                    self.email = self.tela_login.lineEdit_email.text()
                    self.tela_login.lineEdit_email.setText('')
                    self.tela_login.lineEdit_senha.setText('')
            
                    self.abrir_tela_inicial()
                elif resposta.lower() == 'usuário ou senha incorretos.':
                    self.mostrar_mensagem_erro("Usuário ou senha incorretos")
                else:
                    self.mostrar_mensagem_erro("Erro desconhecido")
            except ConnectionResetError:
                print("Conexão com o servidor foi perdida.")
                self.mostrar_mensagem_erro("Conexão com o servidor foi perdida.")
                self.sair_do_sistema()
            except Exception as e:
                print(f"Erro ao conectar com o servidor: {e}")
                self.mostrar_mensagem_erro("Erro ao conectar com o servidor. Verifique sua conexão.")
        else:
            self.mostrar_mensagem_erro("Preencha todos os campos")

    def cadastro(self):
        nome = self.tela_cadastro.lineEdit_nome.text()
        cpf = self.tela_cadastro.lineEdit_cpf.text()
        dataN = self.tela_cadastro.dateEdit_nasci.date().toString("dd-MM-yyyy")
        email = self.tela_cadastro.lineEdit_email.text()
        senha = self.tela_cadastro.lineEdit_senha.text()

        if not nome == '' or cpf == '' or email == '' or senha == '':
            try:
                msg = f'cadastro;{nome};{cpf};{dataN};{email};{senha}'
                
                self.cliente_socket.send(msg.encode())
                resp = self.cliente_socket.recv(1024).decode()
                print(resp)
                
                if resp.lower() == "conta criada com sucesso!":
                    self.tela_cadastro.lineEdit_nome.setText("")
                    self.tela_cadastro.lineEdit_cpf.setText("")
                    self.tela_cadastro.dateEdit_nasci.setDate(QDate.currentDate())
                    self.tela_cadastro.lineEdit_email.setText("")
                    self.tela_cadastro.lineEdit_senha.setText("")
                    
                    print("Dados inseridos com sucesso!")
                    QMessageBox.information(None, '...', 'Novo usuário inserido com sucesso!')
                    self.abrir_tela_login()
                else:
                    self.mostrar_mensagem_erro("Erro na criação de conta")
            except Exception as e:
                print(f"Erro: {e}")
        else:
            self.mostrar_mensagem_erro("Preencha todos os campos")

    def calendario(self):
        print('Data do calendario aterada')
        data_selecionada = self.tela_casa_polvora_reserva.calendarWidget.selectedDate().toPyDate()
        print("Data selecionada: ", data_selecionada)

    def sair(self):
        QMessageBox.information(None, 'Exit', 'Saindo da Aplicação...')
        sys.exit()
        
    def cancelar_cad(self):
        QMessageBox.information(None, '...', 'Cadastro cancelado!')
        self.QtStack.setCurrentIndex(0)

    def mostrar_mensagem_erro(self, mensagem):
        QMessageBox.critical(self, "...", mensagem)

    def abrir_tela_login(self):
        self.QtStack.setCurrentIndex(0)
        self.email = ''
        
    def abrir_tela_cadastro(self):
        self.QtStack.setCurrentIndex(1)
        
    def abrir_tela_inicial(self):
        self.QtStack.setCurrentIndex(2)
        
    def abrir_tela_casa_polvora(self):
        self.QtStack.setCurrentIndex(3)
        
    def abrir_tela_casa_polvora_reserva(self):
        self.QtStack.setCurrentIndex(4)
        
    def abrir_tela_perfil(self):
        try:
            print('1')
            mensagem = f'busca;{self.email}'            
            self.cliente_socket.send(mensagem.encode())
            print(f'Enviada mensagem para o servidor: {mensagem}')
            resposta = self.cliente_socket.recv(1024).decode()
            print(f'Recebida resposta do servidor: {resposta}')

            if ';' in resposta:
                nome, email = resposta.split(';')
                print(f'Nome: {nome}, Email: {email}')

                self.tela_perfil.lineEdit_nome.setText(nome)
                self.tela_perfil.lineEdit_email.setText(email)

                self.QtStack.setCurrentIndex(5)
            else:
                print("Resposta do servidor em formato inesperado.")
        except Exception as e:
            print(f"Erro ao abrir a tela de perfil: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())