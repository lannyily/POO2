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

from classes import Conta, Ingresso_gratuito, Ingresso_pago

from py.tela_cadastro import Ui_tela_cadastro
from py.tela_inicial import Ui_tela_inicial
from py.tela_login import Ui_tela_login
from py.tela_perfil import Ui_tela_perfil
from py.tela_casa_polvora import Ui_tela_casa_polvora
from py.tela_conf_com_senha import Ui_tela_conf_com_senha
from py.tela_reserva_gratis import Ui_reserva_gratis
from py.tela_reserva_paga import Ui_reserva_paga

class TelaConfComSenha(QDialog, Ui_tela_conf_com_senha):
    def __init__(self, parent=None):
        super(TelaConfComSenha, self).__init__(parent)
        self.tela_conf_com_senha.setupUi(self)

class Ui_Main(QtWidgets.QWidget):
    """
    A class é usada para abrir as telas
    
    ...

    Methods
    -------
    setupUi(Main)
        Configura a Janela Principal
        Configura o QStackedLayout
        Cria janelas secundárias
        Configura as telas de interface
        Adiciona telas ao QStackedLayout
    """
    def setupUi(self, Main):
        """
        Parameters
        ----------
        Main : None
        
        """
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()
        
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        
        self.tela_login = Ui_tela_login()
        self.tela_login.setupUi(self.stack0)
        
        self.tela_cadastro = Ui_tela_cadastro()
        self.tela_cadastro.setupUi(self.stack1)
        
        self.tela_inicial = Ui_tela_inicial()
        self.tela_inicial.setupUi(self.stack2)
        
        self.tela_casa_polvora = Ui_tela_casa_polvora()
        self.tela_casa_polvora.setupUi(self.stack3)
        
        self.tela_reserva_gratis = Ui_reserva_gratis()
        self.tela_reserva_gratis.setupUi(self.stack4)
        
        self.tela_perfil = Ui_tela_perfil()
        self.tela_perfil.setupUi(self.stack5)
        
        self.tela_conf_com_senha = Ui_tela_conf_com_senha()
        self.tela_conf_com_senha.setupUi(self.stack6)
        
        self.tela_reserva_paga = Ui_reserva_paga()
        self.tela_reserva_paga.setupUi(self.stack7)
        
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        
class Main(Ui_Main, QMainWindow):
    """
    A classe é usada para tudas as funcionalidades do sistema, desde os botões, calendarias, selação das escolhas, as funções que executam as funcionalidades e a conexão com o banco de dados
    
    ...
    
    Args
    ----
        QMainWindow (None): _description_
        Ui_Main (None): _description_
        
    Attibutes
    ---------
    parent : None
        ...
    
    Methods
    -------
    sair_do_sistema()
        Quando o usuário deseja sair do sistema, ele sai e da inicio a uma nova conexão
    
    login()
        Ele recebe o email e senha do usúario para efetuar o login, se tiver na base de dados
        ele entra na pagina inicial da conta da pessoa, se não, ele fala que login e senha estão 
        incorretos.
    
    cadastro()
        Recebe todos os dados do novo usuário para ser registrado no banco de dados, se ele não
        preecher todos os campos o código dara um aviso.
    
    calendario()
        Para no sistema a data que está no momento
    
    sair()
        Sair do sistema na tela de login
    
    cancelar_cad()
        É para cancelar o cadastro durante o processo
    
    mostrar_mensagem_erro(mensagem)
        Responsavel por colocar todas as mensagens de erro na caixa de erro
    
    abrir_tela_login()
        Abre a tela de login
    
    abrir_tela_inicial()
        Abre a tela inicial
    
    abrir_tela_casa_polvora()
        Abre a tela casa da polvora
    
    abrir_tela_casa_polvora_reserva()
        Abre a tela casa da polvora para fazer a reserva
        
    abrir_tela_perfil()
        Abre a tela de perfil e mostrar o usuário que esta logado no momento
        
        
        
    """
    def __init__(self, parent=None):
        """_summary_

        Args:
            parent (_type_, optional): _description_. Defaults to None.
        """
        super(Main, self).__init__(parent)
        self.setupUi(self)
        
        self.ip = '192.168.18.105'
        self.port = 1600
        self.addr = (self.ip, self.port)
        
        self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente_socket.connect(self.addr)
        
        tipo_usuario = 'cliente'
        self.cliente_socket.send(tipo_usuario.encode())
        print(f'Tipo de usuário enviado para o sevidor: {tipo_usuario}')

        self.tela_login.commandLinkButton_naoTemConta.clicked.connect(self.abrir_tela_cadastro)
        self.tela_login.pushButton_fechar.clicked.connect(self.sair)
        self.tela_login.pushButton_entrar.clicked.connect(self.login)

        self.tela_cadastro.pushButton_cadastrar.clicked.connect(self.cadastro)
        self.tela_cadastro.pushButton_voltar.clicked.connect(self.abrir_tela_login)
        self.tela_cadastro.pushButton_cancelar.clicked.connect(self.cancelar_cad)
        
        self.tela_inicial.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_inicial.pushButton_casa_pol.clicked.connect(self.abrir_tela_casa_polvora)
        self.tela_inicial.perfilButton.clicked.connect(self.abrir_tela_perfil)
        
        self.tela_perfil.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_perfil.pushButton_voltar.clicked.connect(self.abrir_tela_inicial)
        self.tela_perfil.pushButton_excluir_conta.clicked.connect(self.abrir_tela_conf_com_senha)
        
        self.tela_conf_com_senha.pushButton_voltar.clicked.connect(self.abrir_tela_perfil)
        self.tela_conf_com_senha.pushButton_exckuir.clicked.connect(self.excluir_conta)
        
        self.tela_casa_polvora.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_casa_polvora.pushButton_voltar.clicked.connect(self.abrir_tela_inicial)
        self.tela_casa_polvora.pushButton_perfil.clicked.connect(self.abrir_tela_perfil)
        self.tela_casa_polvora.pushButton_2.clicked.connect(self.abrir_link_youtube_casa_polvora)
        self.tela_casa_polvora.pushButton_3.clicked.connect(self.abrir_link_google_maps_casa_polvora)
        self.tela_casa_polvora.pushButton.clicked.connect(self.abrir_tela_reserva_gratis)
        
        self.tela_casa_polvora_reserva.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_casa_polvora_reserva.pushButton_voltar.clicked.connect(self.abrir_tela_casa_polvora)
        self.tela_casa_polvora_reserva.calendarWidget.selectionChanged.connect(self.calendario)
        
        self.email = ''

    def sair_do_sistema(self):
        print("1 saindo do sistema....")
        msg = f'sair'
        self.cliente_socket.send(msg.encode())
        print('2 saindo do sistema....')
        resposta = self.cliente_socket.recv(1024).decode()
        print(f'Resposta recebida: {resposta}')
        print('3 saindo do sistema....')
     
        if resposta.lower() == 'desconectado pelo servidor':
            print('3 saindo do sistema....')
            self.cliente_socket.close() 
            print('4 saindo do sistema....')
            self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print('5 saindo do sistema....')
            self.cliente_socket.connect(self.addr)
            print('6 saindo do sistema....')
            self.abrir_tela_login()
            print('7 saindo do sistema....')
            
        print('Foi')

    def sair(self):
        msg = 'sair'
        self.cliente_socket.send(msg.encode())
        
        resposta = self.cliente_socket.recv(1024).decode()
        if resposta.lower() == 'Desconectado pelo servidor':
            self.cliente_socket.close()     
        self.close()
        print('Saiu do sistema')  
        
    def login(self):
        while True:
            email = self.tela_login.lineEdit_email.text()
            senha = self.tela_login.lineEdit_senha.text()

            if email and senha:
                try:
                    senha_md5 = hashlib.md5(senha.encode()).hexdigest()
                    
                    mensagem = f"login;{email};{senha_md5}"

                    self.cliente_socket.send(mensagem.encode('utf-8'))
                    print('1 - Mensagem enviada:', mensagem)

                    resposta = self.cliente_socket.recv(1024).decode('utf-8')

                    print('2 - Resposta recebida:', resposta)

                    if resposta.lower() == 'login bem-sucedido!':
                        self.email = email
                        self.tela_login.lineEdit_email.setText('')
                        self.tela_login.lineEdit_senha.setText('')
                        self.abrir_tela_inicial()
                        break  
                    elif resposta.lower() == 'usuário ou senha incorretos.':
                        self.mostrar_mensagem_erro("Usuário ou senha incorretos. Tente novamente.")
                        self.tela_login.lineEdit_email.setText('')  
                        self.tela_login.lineEdit_senha.setText('')  
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
                if not email:
                    self.mostrar_mensagem_erro("Campo de e-mail vazio. Preencha todos os campos.")
                elif not senha:
                    self.mostrar_mensagem_erro("Campo de senha vazio. Preencha todos os campos.")
                break  

    def cadastro(self):
        print('Cadastro')
        nome = self.tela_cadastro.lineEdit_nome.text()
        cpf = self.tela_cadastro.lineEdit_cpf.text()
        dataN = self.tela_cadastro.dateEdit_nasci.date().toString("dd-MM-yyyy")
        email = self.tela_cadastro.lineEdit_email.text()
        senha = self.tela_cadastro.lineEdit_senha.text()

        if not nome == '' or cpf == '' or email == '' or senha == '':
            try:
                senha_md5 = hashlib.md5(senha.encode()).hexdigest()
                
                msg = f'cadastro;{nome};{cpf};{dataN};{email};{senha_md5}'
                print(f'Mensagem enviada: {msg}')
                self.cliente_socket.send(msg.encode())
                
                resp = self.cliente_socket.recv(1024).decode()
                print(f'Resposta recebida: {resp}')
                
                if resp.lower() == "dados inseridos com sucesso!":
                    self.tela_cadastro.lineEdit_nome.setText("")
                    self.tela_cadastro.lineEdit_cpf.setText("")
                    self.tela_cadastro.dateEdit_nasci.setDate(QDate.currentDate())
                    self.tela_cadastro.lineEdit_email.setText("")
                    self.tela_cadastro.lineEdit_senha.setText("")
                    
                    print("Dados inseridos com sucesso!")
                    QMessageBox.information(None, '...', 'Novo usuário inserido com sucesso!')
                    self.abrir_tela_login()
                    
                elif resp.lower() == "cpf ja cadastrado. nao e possivel criar a conta":
                    self.mostrar_mensagem_erro("CPF já cadastrado. Tente novamente.")
                    self.tela_cadastro.lineEdit_cpf.setText("")
                elif resp.lower() == "email ja cadastrado. nao e possivel criar a conta":
                    self.mostrar_mensagem_erro("E-mail já cadastrado. Tente novamente.")
                    self.tela_cadastro.lineEdit_email.setText("") 
                elif resp.lower() == "email invalido":
                    self.mostrar_mensagem_erro("E-mail inválido. Digite um e-mail valido.")
                    self.tela_cadastro.lineEdit_email.setText("")
                elif resp.lower() == "senha muito curta":
                    self.mostrar_mensagem_erro("Senha muito curta. Digite uma senha com no mínimo 8 caracteres.")
                    self.tela_cadastro.lineEdit_senha.setText("")
                elif resp.lower() == "cpf invalido":
                    self.mostrar_mensagem_erro("CPF inválido. Digite um CPF válido.")
                    self.tela_cadastro.lineEdit_cpf.setText("")
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
        
    def cancelar_cad(self):
        QMessageBox.information(None, '...', 'Cadastro cancelado!')
        self.QtStack.setCurrentIndex(0)

    def excluir_conta(self):
        senha = self.tela_conf_com_senha.lineEdit_senha.text()
        if senha:
            try:
                senha_md5 = hashlib.md5(senha.encode()).hexdigest()
                
                msg = f'excluir;{self.email};{senha_md5}'
                print(f'Mensagem enviada: {msg}')
                self.cliente_socket.send(msg.encode())
                
                resp = self.cliente_socket.recv(1024).decode()
                print(f'Resposta recebida: {resp}')
                
                if resp.lower() == "conta excluida com sucesso!":
                    self.tela_conf_com_senha.lineEdit_senha.setText("")
                    print("Conta excluida com sucesso!")
                    QMessageBox.information(None, '...', 'Conta excluida com sucesso!')
                    self.abrir_tela_login()
                    
                elif resp.lower() == "senha incorreta":
                    self.mostrar_mensagem_erro("Senha incorreta. Tente novamente.")
                    self.tela_conf_com_senha.lineEdit_senha.setText("")
                else:
                    self.mostrar_mensagem_erro("Erro ao excluir conta")
                    
            except Exception as e:
                print(f"Erro: {e}")
        else:
            self.mostrar_mensagem_erro("Preencha todos os campos")

    def abrir_link_youtube_casa_polvora(self):
        QDesktopServices.openUrl(QUrl("https://www.youtube.com/watch?v=2RI0kLBV9Mw"))
    
    def abrir_link_google_maps_casa_polvora(self):
        QDesktopServices.openUrl(QUrl("https://www.google.com/maps/place/Casa+da+Pólvora/@-7.0224187,-42.1316923,17z/data=!3m1!4b1!4m6!3m5!1s0x79c91375b1794b7:0xd075cbbe61f291b2!8m2!3d-7.022424!4d-42.129112!16s%2Fg%2F11txrpwcrh?hl=pt-BR&entry=ttu"))
    
    def mostrar_mensagem_erro(self, mensagem):
        QMessageBox.critical(self, "...", mensagem)

    def abrir_tela_login(self):
        self.QtStack.setCurrentIndex(0)
        self.email = ''
        self.tela_login.lineEdit_email.setText("")
        self.tela_login.lineEdit_senha.setText("")
        
    def abrir_tela_cadastro(self):
        self.QtStack.setCurrentIndex(1)
        self.tela_cadastro.lineEdit_nome.setText("")
        self.tela_cadastro.lineEdit_cpf.setText("")
        self.tela_cadastro.dateEdit_nasci.setDate(QDate.currentDate())
        self.tela_cadastro.lineEdit_email.setText("")
        self.tela_cadastro.lineEdit_senha.setText("")
        
    def abrir_tela_inicial(self):
        self.QtStack.setCurrentIndex(2)
        
    def abrir_tela_casa_polvora(self):
        self.QtStack.setCurrentIndex(3)
        
    def abrir_tela_reserva_gratis(self):
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
    
    def abrir_tela_conf_com_senha(self):
        self.QtStack.setCurrentIndex(6)
    
    def abrir_tela_reserva_paga(self):
        self.QtStack.setCurrentIndex(7)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
    
    