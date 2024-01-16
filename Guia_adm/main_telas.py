import sys
import socket
import hashlib
import json

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import Qt, QUrl, QDate

from py.tela_login_adm import Ui_tela_login_adm
from py.tela_inicial_adm import Ui_tela_inicial_adm
from py.tela_login import Ui_tela_login_guia
from py.tela_conf_com_senha import Ui_tela_conf_com_senha
from py.tela_atualizar_senha import Ui_tela_atualizar_senha
from py.tela_usuarios import Ui_tela_usuarios
from py.tela_excluir_conta import Ui_tela_excluir_conta
from py.tela_hoteis import Ui_tela_hoteis
from py.tela_restaurante import Ui_tela_restaurante
from py.tela_novo_hotel import Ui_tela_novo_hotel
from py.tela_excluir_hotel import Ui_tela_excluir_hotel
from py.tela_novo_restaurante import Ui_tela_novo_restaurante
from py.tela_excluir_restaurante import Ui_tela_excluir_restaurante

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
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()
        self.stack10 = QtWidgets.QMainWindow()
        self.stack11 = QtWidgets.QMainWindow()
        self.stack12 = QtWidgets.QMainWindow()
        
        self.tela_login_guia = Ui_tela_login_guia()
        self.tela_login_guia.setupUi(self.stack0)
        
        self.tela_login_admin = Ui_tela_login_adm()
        self.tela_login_admin.setupUi(self.stack1)
        
        self.tela_inicial_admin = Ui_tela_inicial_adm()
        self.tela_inicial_admin.setupUi(self.stack2)
        
        self.tela_conf_com_senha = Ui_tela_conf_com_senha()
        self.tela_conf_com_senha.setupUi(self.stack3)
        
        self.tela_atualizar_senha = Ui_tela_atualizar_senha()
        self.tela_atualizar_senha.setupUi(self.stack4)
        
        self.tela_usuarios = Ui_tela_usuarios()
        self.tela_usuarios.setupUi(self.stack5)
        
        self.tela_excluir_conta = Ui_tela_excluir_conta()
        self.tela_excluir_conta.setupUi(self.stack6)
        
        self.tela_hoteis = Ui_tela_hoteis()
        self.tela_hoteis.setupUi(self.stack7)
        
        self.tela_restaurante = Ui_tela_restaurante()
        self.tela_restaurante.setupUi(self.stack8)
        
        self.tela_novo_hotel = Ui_tela_novo_hotel()
        self.tela_novo_hotel.setupUi(self.stack9)
        
        self.tela_excluir_hotel = Ui_tela_excluir_hotel()
        self.tela_excluir_hotel.setupUi(self.stack10)
        
        self.tela_novo_restaurante = Ui_tela_novo_restaurante()
        self.tela_novo_restaurante.setupUi(self.stack11)
        
        self.tela_excluir_restaurante = Ui_tela_excluir_restaurante()
        self.tela_excluir_restaurante.setupUi(self.stack12)
        
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)
        self.QtStack.addWidget(self.stack10)
        self.QtStack.addWidget(self.stack11)
        self.QtStack.addWidget(self.stack12)
        
class Main(Ui_Main, QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        
        self.ip = '192.168.1.15'
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
        self.tela_inicial_admin.pushButton_usuarios.clicked.connect(self.listar_usuarios)
        self.tela_inicial_admin.pushButton_hoteis_2.clicked.connect(self.listar_hoteis)
        self.tela_inicial_admin.pushButton_restaurantes.clicked.connect(self.listar_restaurantes)
        
        self.tela_restaurante.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_restaurante.pushButton_voltar.clicked.connect(self.abrir_tela_inicial_admin)
        self.tela_restaurante.pushButton_add_hotel.clicked.connect(self.abrir_tela_novo_restaurante)
        self.tela_restaurante.pushButton_excluir_hotel.clicked.connect(self.abrir_tela_excluir_restaurante)
        
        self.tela_novo_restaurante.pushButton_voltar_2.clicked.connect(self.abrir_tela_restaurante)
        self.tela_novo_restaurante.pushButton_sair_2.clicked.connect(self.sair_do_sistema)
        self.tela_novo_restaurante.pushButton_add_restaurante.clicked.connect(self.add_restaurante)
        
        self.tela_excluir_restaurante.pushButton_voltar.clicked.connect(self.abrir_tela_restaurante)
        self.tela_excluir_restaurante.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_excluir_restaurante.pushButton_buscar.clicked.connect(self.excluir_restaurante_busca)
        self.tela_excluir_restaurante.pushButton_excluir.clicked.connect(self.excluir_restaurante)
        
        self.tela_hoteis.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_hoteis.pushButton_voltar.clicked.connect(self.abrir_tela_inicial_admin)
        self.tela_hoteis.pushButton_add_hotel.clicked.connect(self.abrir_tela_novo_hotel)
        self.tela_hoteis.pushButton_excluir_hotel.clicked.connect(self.abrir_tela_excluir_hotel)
        
        self.tela_novo_hotel.pushButton_voltar_2.clicked.connect(self.abrir_tela_hoteis)
        self.tela_novo_hotel.pushButton_sair_2.clicked.connect(self.sair_do_sistema)
        self.tela_novo_hotel.pushButton_add_hotel.clicked.connect(self.add_hotel)
        
        self.tela_excluir_hotel.pushButton_voltar.clicked.connect(self.abrir_tela_hoteis)
        self.tela_excluir_hotel.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_excluir_hotel.pushButton_buscar.clicked.connect(self.excluir_hotel_busca)
        self.tela_excluir_hotel.pushButton_excluir.clicked.connect(self.excluir_hotel)
        
        self.tela_usuarios.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_usuarios.pushButton_voltar.clicked.connect(self.abrir_tela_inicial_admin)
        self.tela_usuarios.pushButton_buscar.clicked.connect(self.buscar_usuarios)
        self.tela_usuarios.pushButton_buscar_2.clicked.connect(self.mostrar_conta)
        
        self.tela_excluir_conta.pushButton_voltar.clicked.connect(self.abrir_tela_usuarios)
        self.tela_excluir_conta.pushButton_redefinir_senha.clicked.connect(self.excluir_conta)
        
        self.tela_conf_com_senha.pushButton_sair_2.clicked.connect(self.abrir_tela_inicial_admin)
        self.tela_conf_com_senha.pushButton.clicked.connect(self.autenticar_senha)
        
        self.tela_atualizar_senha.pushButton.clicked.connect(self.nova_senha)
        self.tela_atualizar_senha.pushButton_2.clicked.connect(self.abrir_tela_inicial_admin)
        
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
            self.abrir_tela_login_admin()
        
    def entrar_no_sistema_admin(self):
        while True:
            print('Entrando no sistema...')
            senha = self.tela_login_admin.lineEdit_senha.text()
            
            if senha:
                try:
                    print(f'Senha digitada: {senha}')
                    senha_md5 = hashlib.md5(senha.encode()).hexdigest()
                    mensagem = f'loginadmin;{senha_md5}'
                    
                    self.cliente_socket.send(mensagem.encode())
                    print(f'Senha enviada para o servidor: {senha_md5}')
                    
                    resposta = self.cliente_socket.recv(1024).decode()
                    print(f'Resposta do servidor: {resposta}')
                    
                    if resposta.lower() == 'login efetuado com sucesso':
                        self.tela_login_admin.lineEdit_senha.setText('')
                        self.abrir_tela_inicial_admin()
                        break
                    elif resposta.lower() == 'senha incorreta':
                        self.mostrar_mensagem_erro('Senha incorreta')
                        self.tela_login_admin.lineEdit_senha.setText('')
                        break
                    else:
                        self.mostrar_mensagem_erro('Erro ao efetuar login')
                        self.tela_login_admin.lineEdit_senha.setText('')
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
    
    def autenticar_senha(self):
        while True:
            senha = self.tela_conf_com_senha.lineEdit.text()
            if senha:
                try:
                    print(f'Senha digitada: {senha}')
                    senha_md5 = hashlib.md5(senha.encode()).hexdigest()
                    mensagem = f'autenticar;{senha_md5}'
                    
                    self.cliente_socket.send(mensagem.encode())
                    print(f'Senha enviada para o servidor: {senha_md5}')
                    
                    resposta = self.cliente_socket.recv(1024).decode()
                    print(f'Resposta do servidor: {resposta}')
                    
                    if resposta.lower() == 'login efetuado com sucesso':
                        self.tela_conf_com_senha.lineEdit.setText('')
                        self.abrir_tela_atualizar_senha()
                        break
                    elif resposta.lower() == 'senha incorreta':
                        self.mostrar_mensagem_erro('Senha incorreta')
                        self.tela_conf_com_senha.lineEdit.setText('')
                        break
                    else:
                        self.mostrar_mensagem_erro('Erro ao efetuar login')
                        self.tela_conf_com_senha.lineEdit.setText('')
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
    
    def nova_senha(self):
        while True:
            senha = self.tela_atualizar_senha.lineEdit.text()
            senha_confirmada = self.tela_atualizar_senha.lineEdit_2.text()
            if senha and senha_confirmada:
                try:
                    if senha == senha_confirmada:
                        senha_md5 = hashlib.md5(senha.encode()).hexdigest()
                        mensagem = f'atualizar;{senha_md5}'
                        
                        self.cliente_socket.send(mensagem.encode())
                        print(f'Senha enviada para o servidor: {senha_md5}')
                        
                        resposta = self.cliente_socket.recv(1024).decode()
                        print(f'Resposta do servidor: {resposta}')
                        
                        if resposta.lower() == 'senha atualizada com sucesso!':
                            self.tela_atualizar_senha.lineEdit.setText('')
                            self.tela_atualizar_senha.lineEdit_2.setText('')
                            self.mostrar_mensagem_aviso('Senha atualizada com sucesso!')
                            self.abrir_tela_inicial_admin()
                            break
                        elif resposta.lower() == 'erro ao atualizar senha':
                            self.mostrar_mensagem_erro('Erro ao atualizar senha')
                            self.tela_atualizar_senha.lineEdit.setText('')
                            self.tela_atualizar_senha.lineEdit_2.setText('')
                            break
                except ConnectionResetError:
                    print("Conexão com o servidor foi perdida.")
                    self.mostrar_mensagem_erro("Conexão com o servidor foi perdida.")
                    self.sair()
                except Exception as e:
                    print(f"Erro ao conectar com o servidor: {e}")
                    self.mostrar_mensagem_erro("Erro ao conectar com o servidor. Verifique sua conexão.")
            else:
                if not senha:
                    self.mostrar_mensagem_erro('Senha não informada')
                    break
                elif not senha_confirmada:
                    self.mostrar_mensagem_erro('Confirmação de senha não informada')
                    break
    
    def listar_usuarios(self):
        self.abrir_tela_usuarios()
        mensagem = 'listarusuarios'
        self.cliente_socket.send(mensagem.encode())
        print(f'Mensagem enviada para o servidor: {mensagem}')
        
        resposta = self.cliente_socket.recv(1024).decode()
        resposta = json.loads(resposta)
        print(f'Resposta do servidor: {resposta}')
        
        self.tela_usuarios.tableWidget.setRowCount(len(resposta))
        self.tela_usuarios.tableWidget.setColumnCount(6) 
        for i in range(0, len(resposta)):
            for j in range(0, 6):
                self.tela_usuarios.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(resposta[i][j])))
           
    def buscar_usuarios(self):
        while True:
            email = self.tela_usuarios.lineEdit.text()
            
            if email:
                try:
                    mensagem = f'busca;{email}'
                    self.cliente_socket.send(mensagem.encode())
                    print(f'Mensagem enviada para o servidor: {mensagem}')
                    
                    resposta = self.cliente_socket.recv(1024).decode()
                    print(f'Resposta do servidor: {resposta}')
                    
                    if resposta.lower() == 'nome nao encontrado':
                        self.mostrar_mensagem_aviso('Nome não encontrado')
                        self.tela_usuarios.lineEdit.setText('')
                        break
                    else:
                        self.tela_usuarios.lineEdit_2.setText(resposta)
                        break
                except ConnectionResetError:
                    print("Conexão com o servidor foi perdida.")
                    self.mostrar_mensagem_erro("Conexão com o servidor foi perdida.")
                    self.sair()
                except Exception as e:
                    print(f"Erro ao conectar com o servidor: {e}")
                    self.mostrar_mensagem_erro("Erro ao conectar com o servidor. Verifique sua conexão.")
            else:
                self.mostrar_mensagem_erro('Nome não informado')
                break

    def mostrar_conta(self):
        self.abrir_tela_excluir_conta()
        mensagem = 'mostarconta'
        self.cliente_socket.send(mensagem.encode())
        print(f'Mensagem enviada para o servidor: {mensagem}')
        
        resposta = self.cliente_socket.recv(1024).decode()
        
        resposta = json.loads(resposta)
        print(f'Resposta do servidor: {resposta}')
        
        self.tela_excluir_conta.tableWidget.setRowCount(1)
        self.tela_excluir_conta.tableWidget.setColumnCount(6)
                
        print('antes do for')
        for j in range(0, 6):
            self.tela_excluir_conta.tableWidget.setItem(0, j, QtWidgets.QTableWidgetItem(str(resposta[j])))
        print('depois do for')
      
    def excluir_conta(self):
        menagem = 'excluir'
        self.cliente_socket.send(menagem.encode())
        
        resposta = self.cliente_socket.recv(1024).decode()
        print(f'Resposta do servidor: {resposta}')
        
        if resposta.lower() == 'conta excluida com sucesso':
            self.mostrar_mensagem_aviso('Conta excluída com sucesso')
            self.abrir_tela_usuarios()
        else:
            self.mostrar_mensagem_erro('Erro ao excluir conta')
            self.abrir_tela_usuarios()
    
    def listar_hoteis(self):
        self.abrir_tela_hoteis()
        mensagem = 'listarhoteis'
        self.cliente_socket.send(mensagem.encode())
        print(f'Mensagem enviada para o servidor: {mensagem}')
        
        resposta = self.cliente_socket.recv(1024).decode()
        resposta = json.loads(resposta)
        print(f'Resposta do servidor: {resposta}')
        
        self.tela_hoteis.tableWidget.setRowCount(len(resposta))
        self.tela_hoteis.tableWidget.setColumnCount(6)
        for i in range(0, len(resposta)):
            for j in range(0, 6):
                self.tela_hoteis.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(resposta[i][j])))
    
    def listar_restaurantes(self):
        self.abrir_tela_restaurante()
        mensagem = 'listarrestaurantes'
        self.cliente_socket.send(mensagem.encode())
        print(f'Mensagem enviada para o servidor: {mensagem}')
        
        resposta = self.cliente_socket.recv(1024).decode()
        resposta = json.loads(resposta)
        print(f'Resposta do servidor: {resposta}')
        
        self.tela_restaurante.tableWidget.setRowCount(len(resposta))
        self.tela_restaurante.tableWidget.setColumnCount(6)
        for i in range(0, len(resposta)):
            for j in range(0, 6):
                self.tela_restaurante.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(resposta[i][j])))
             
    def add_hotel(self):
        while True:
            nome = self.tela_novo_hotel.lineEdit_nome.text()
            endereco = self.tela_novo_hotel.lineEdit_endereco.text()
            if self.tela_novo_hotel.radioButton_esta_sim.isChecked():
                estacionamento = 'SIM'
            elif self.tela_novo_hotel.radioButton_esta_nao.isChecked():
                estacionamento = 'NAO'
            if self.tela_novo_hotel.radioButton_piscina_sim.isChecked():
                piscina = 'SIM'
            elif self.tela_novo_hotel.radioButton_piscina_nao.isChecked():
                piscina = 'NAO'
            link = self.tela_novo_hotel.lineEdit_endereco_2.text()
            
            if nome and endereco and estacionamento and piscina and link:
                try:
                    mensagem = f'addhotel;{nome};{endereco};{estacionamento};{piscina};{link}'
                    self.cliente_socket.send(mensagem.encode())
                    print(f'Mensagem enviada para o servidor: {mensagem}')
                    
                    resposta = self.cliente_socket.recv(1024).decode()
                    print(f'Resposta do servidor: {resposta}')
                    
                    if resposta.lower() == 'sim':
                        self.mostrar_mensagem_aviso('Hotel adicionado com sucesso')
                        self.tela_novo_hotel.lineEdit_nome.setText('')
                        self.tela_novo_hotel.lineEdit_endereco.setText('')
                        self.tela_novo_hotel.lineEdit_endereco_2.setText('')
                        estacionamento = ''
                        piscina = ''
                        self.abrir_tela_hoteis()
                        break
                    elif resposta.lower() == 'nome':
                        self.mostrar_mensagem_aviso('Nome já cadastrado. Não é possível criar a conta')
                        self.tela_novo_hotel.lineEdit_nome.setText('')
                    elif resposta.lower() == 'endereco':
                        self.mostrar_mensagem_aviso('Endereço já cadastrado. Não é possível criar a conta')
                        self.tela_novo_hotel.lineEdit_endereco.setText('')
                    else:
                        self.mostrar_mensagem_erro('Erro ao adicionar hotel')
                        self.tela_novo_hotel.lineEdit_nome.setText('')
                        self.tela_novo_hotel.lineEdit_endereco.setText('')
                        self.tela_novo_hotel.lineEdit_endereco_2.setText('')
                        estacionamento = ''
                        piscina = ''
                        self.abrir_tela_hoteis()
                        break
                except ConnectionResetError:
                    print("Conexão com o servidor foi perdida.")
                    self.mostrar_mensagem_erro("Conexão com o servidor foi perdida.")
                    self.sair()
                except Exception as e:
                    print(f"Erro ao conectar com o servidor: {e}")
                    self.mostrar_mensagem_erro("Erro ao conectar com o servidor. Verifique sua conexão.")
     
    def add_restaurante(self):
        while True:
            nome = self.tela_novo_restaurante.lineEdit_nome.text()
            endereco = self.tela_novo_restaurante.lineEdit_endereco.text()
            if self.tela_novo_restaurante.radioButton_esta_sim.isChecked():
                estacionamento = 'SIM'
            elif self.tela_novo_restaurante.radioButton_esta_nao.isChecked():
                estacionamento = 'NAO'
            if self.tela_novo_restaurante.radioButton_refe_sim.isChecked():
                refeicaoLocal = 'SIM'
            elif self.tela_novo_restaurante.radioButton_refe_nao.isChecked():
                refeicaoLocal = 'NAO'
            if self.tela_novo_restaurante.radioButton_delivery_sim.isChecked():
                delivery = 'SIM'
            elif self.tela_novo_restaurante.radioButton_delivery_nao.isChecked():
                delivery = 'NAO'
            link = self.tela_novo_restaurante.lineEdit_endereco_2.text()
            
            if nome and endereco and estacionamento and refeicaoLocal and delivery and link:
                try:
                    mensagem = f'addrestaurante;{nome};{endereco};{estacionamento};{refeicaoLocal};{delivery};{link}'
                    self.cliente_socket.send(mensagem.encode())
                    print(f'Mensagem enviada para o servidor: {mensagem}')
                    
                    resposta = self.cliente_socket.recv(1024).decode()
                    print(f'Resposta do servidor: {resposta}')
                    
                    if resposta.lower() == 'sim':
                        self.mostrar_mensagem_aviso('Restaurante adicionado com sucesso')
                        self.tela_novo_restaurante.lineEdit_nome.setText('')
                        self.tela_novo_restaurante.lineEdit_endereco.setText('')
                        self.tela_novo_restaurante.lineEdit_endereco_2.setText('')
                        estacionamento = ''
                        refeicaoLocal = ''
                        delivery = ''
                        self.abrir_tela_restaurante()
                        break
                    elif resposta.lower() == 'nome':
                        self.mostrar_mensagem_aviso('Nome já cadastrado. Não é possível criar a conta')
                        self.tela_novo_restaurante.lineEdit_nome.setText('')
                    elif resposta.lower() == 'endereco':
                        self.mostrar_mensagem_aviso('Endereço já cadastrado. Não é possível criar a conta')
                        self.tela_novo_restaurante.lineEdit_endereco.setText('')
                    else:
                        self.mostrar_mensagem_erro('Erro ao adicionar restaurante')
                        self.tela_novo_restaurante.lineEdit_nome.setText('')
                        self.tela_novo_restaurante.lineEdit_endereco.setText('')
                        self.tela_novo_restaurante.lineEdit_endereco_2.setText('')
                        estacionamento = ''
                        refeicaoLocal = ''
                        delivery = ''
                        self.abrir_tela_restaurante()
                        break    
                except ConnectionResetError:
                    print("Conexão com o servidor foi perdida.")
                    self.mostrar_mensagem_erro("Conexão com o servidor foi perdida.")
                    self.sair()
                except Exception as e:
                    print(f"Erro ao conectar com o servidor: {e}")
                    self.mostrar_mensagem_erro("Erro ao conectar com o servidor. Verifique sua conexão.")
                                    
    def excluir_hotel_busca(self):
            while True:
                id_hotel = self.tela_excluir_hotel.lineEdit.text()
                if id_hotel:
                    try:
                        mensagem = f'buscahotel;{id_hotel}'
                        self.cliente_socket.send(mensagem.encode())
                        print(f'Mensagem enviada para o servidor: {mensagem}')
                        
                        resposta = self.cliente_socket.recv(1024).decode()
                        print(f'Resposta do servidor: {resposta}')
                        
                        if resposta.lower() == 'hotel nao encontrado':
                            self.mostrar_mensagem_aviso('Hotel não encontrado')
                            self.tela_excluir_hotel.lineEdit_2.setText('')
                            break
                        else:
                            self.tela_excluir_hotel.lineEdit_2.setText(resposta)
                            break
                    except ConnectionResetError:
                        print("Conexão com o servidor foi perdida.")
                        self.mostrar_mensagem_erro("Conexão com o servidor foi perdida.")
                        self.sair()
                    except Exception as e:
                        print(f"Erro ao conectar com o servidor: {e}")
                        self.mostrar_mensagem_erro("Erro ao conectar com o servidor. Verifique sua conexão.")
                else:
                    self.mostrar_mensagem_erro('ID do hotel não informado')
                    break
    
    def excluir_restaurante_busca(self):
        while True:
            id_restaurante = self.tela_excluir_restaurante.lineEdit_id.text()
            if id_restaurante:
                try:
                    mensagem = f'buscarestaurante;{id_restaurante}'
                    self.cliente_socket.send(mensagem.encode())
                    print(f'Mensagem enviada para o servidor: {mensagem}')
                    
                    resposta = self.cliente_socket.recv(1024).decode()
                    print(f'Resposta do servidor: {resposta}')
                    
                    if resposta.lower() == 'restaurante nao encontrado':
                        self.mostrar_mensagem_aviso('Restaurante não encontrado')
                        self.tela_excluir_restaurante.lineEdit_resultado.setText('')
                        break
                    else:
                        self.tela_excluir_restaurante.lineEdit_resultado.setText(resposta)
                        break
                except ConnectionResetError:
                    print("Conexão com o servidor foi perdida.")
                    self.mostrar_mensagem_erro("Conexão com o servidor foi perdida.")
                    self.sair()
                except Exception as e:
                    print(f"Erro ao conectar com o servidor: {e}")
                    self.mostrar_mensagem_erro("Erro ao conectar com o servidor. Verifique sua conexão.")
            else:
                self.mostrar_mensagem_erro('ID do restaurante não informado')
                break
    
    def excluir_hotel(self):
        mensagem = 'excluirhotel'
        self.cliente_socket.send(mensagem.encode())
        
        resposta = self.cliente_socket.recv(1024).decode()
        print(f'Resposta do servidor: {resposta}')
        
        if resposta.lower() == 'hotel excluido com sucesso':
            self.mostrar_mensagem_aviso('Hotel excluído com sucesso')
            self.abrir_tela_hoteis()
        else:
            self.mostrar_mensagem_erro('Erro ao excluir hotel')
            self.abrir_tela_hoteis()
    
    def excluir_restaurante(self):
        mensagem = 'excluirrestaurante'
        self.cliente_socket.send(mensagem.encode())
        
        resposta = self.cliente_socket.recv(1024).decode()
        print(f'Resposta do servidor: {resposta}')
        
        if resposta.lower() == 'restaurante excluido com sucesso':
            self.mostrar_mensagem_aviso('Restaurante excluído com sucesso')
            self.abrir_tela_restaurante()
        else:
            self.mostrar_mensagem_erro('Erro ao excluir restaurante')
            self.abrir_tela_restaurante()
                  
    def abrir_tela_login_guia(self):
        self.QtStack.setCurrentIndex(0)  
        
    def abrir_tela_login_admin(self):
        tipo_usuario = 'funcionario'
        self.cliente_socket.send(tipo_usuario.encode())
        print(f'Tipo de usuário enviado para o sevidor: {tipo_usuario}')
        self.QtStack.setCurrentIndex(1)
        
    def abrir_tela_inicial_admin(self):
        self.QtStack.setCurrentIndex(2)
        
    def abrir_tela_conf_com_senha(self):
        self.stack3.show()
        
    def abrir_tela_atualizar_senha(self):
        self.stack3.close()
        self.QtStack.setCurrentIndex(4)
        
    def abrir_tela_usuarios(self):
        self.stack3.close()
        self.stack6.close()
        self.QtStack.setCurrentIndex(5)
        
    def mostrar_mensagem_erro(self, mensagem):
        QMessageBox.critical(self, "Contos da Vila", mensagem)
        
    def mostrar_mensagem_aviso(self, mensagem):
        QMessageBox.warning(self, "Contos da Vila", mensagem)
        
    def abrir_tela_excluir_conta(self):
        self.stack6.show()
        
    def abrir_tela_hoteis(self):
        self.stack10.close()
        self.QtStack.setCurrentIndex(7)
        
    def abrir_tela_restaurante(self):
        self.stack12.close()
        self.QtStack.setCurrentIndex(8)
        
    def abrir_tela_novo_hotel(self):
        self.QtStack.setCurrentIndex(9)
        
    def abrir_tela_excluir_hotel(self):
        self.stack10.show()
        
    def abrir_tela_novo_restaurante(self):
        self.QtStack.setCurrentIndex(11)
        
    def abrir_tela_excluir_restaurante(self):
        self.stack12.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())