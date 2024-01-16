import sys
import json
import socket
import hashlib
import base64

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import Qt, QUrl, QDate
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QByteArray

from py.tela_cadastro import Ui_tela_cadastro
from py.tela_inicial import Ui_tela_inicial
from py.tela_login import Ui_tela_login
from py.tela_perfil import Ui_tela_perfil
from py.tela_casa_polvora import Ui_tela_casa_polvora
from py.tela_conf_com_senha import Ui_tela_conf_com_senha
from py.tela_reserva_gratis import Ui_reserva_gratis
from py.tela_reserva_paga import Ui_reserva_paga
from py.tela_hoteis import Ui_hoteis
from py.tela_restaurantes import Ui_restaurantes
from py.tela_nota_fical import Ui_tela_nota_fiscal

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
        self.stack8 = QtWidgets.QMainWindow()
        self.stack9 = QtWidgets.QMainWindow()
        self.stack10 = QtWidgets.QMainWindow()
        
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
        
        self.tela_hoteis = Ui_hoteis()
        self.tela_hoteis.setupUi(self.stack8)
        
        self.tela_restaurantes = Ui_restaurantes()
        self.tela_restaurantes.setupUi(self.stack9)
        
        self.tela_nota_fiscal = Ui_tela_nota_fiscal()
        self.tela_nota_fiscal.setupUi(self.stack10)
        
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
    __init__(self, parent=None): Este é o método de inicialização da classe principal. Ele configura a interface do 
    usuário (UI) usando o método setupUi. Além disso, estabelece a conexão com o servidor por meio de um socket TCP, 
    envia o tipo de usuário (cliente) e configura os sinais e slots para os elementos da interface do usuário.

    nota_fiscal(self): Envia uma mensagem ao servidor solicitando uma nota fiscal. Recebe a resposta do servidor, que 
    é um JSON contendo informações sobre a nota fiscal, e exibe essas informações na interface do usuário. Em seguida,
    envia uma mensagem para solicitar o QR code, recebe a imagem em base64 e a exibe.

    ingresso_gratis(self): Envia uma mensagem ao servidor para reservar um ingresso gratuito, com base nas informações 
    fornecidas. Recebe a resposta do servidor e exibe uma mensagem de sucesso ou erro.

    listar_restaurantes(self): Envia uma mensagem ao servidor solicitando a lista de restaurantes. Recebe a resposta em 
    formato JSON e exibe as informações na interface do usuário.

    listar_hoteis(self): Envia uma mensagem ao servidor solicitando a lista de hotéis. Recebe a resposta em formato JSON 
    e exibe as informações na interface do usuário.

    sair_do_sistema(self): Envia uma mensagem ao servidor indicando a intenção de sair. Fecha a conexão com o servidor 
    e retorna à tela de login.

    sair(self): Envia uma mensagem ao servidor indicando a intenção de sair. Fecha a conexão com o servidor e fecha o 
    aplicativo.

   login(self): Solicita informações de login do usuário, envia ao servidor e processa a resposta. Se o login for 
   bem-sucedido, abre a tela inicial.

   cadastro(self): Solicita informações de cadastro do usuário, envia ao servidor e processa a resposta. Exibe mensagens 
   de sucesso ou erro.

   cancelar_cad(self): Cancela o cadastro e retorna à tela de login.

    excluir_conta(self): Solicita senha para excluir a conta, envia ao servidor e processa a resposta. Exibe mensagens 
    de sucesso ou erro.

  Vários métodos para abrir diferentes telas na interface do usuário, como abrir_tela_inicial, abrir_tela_casa_polvora, 
  etc.
        
        
        
    """
    def __init__(self, parent=None):
        """_summary_

        Args:
            parent (_type_, optional): _description_. Defaults to None.
            
        o método __init__ é responsável por preparar o ambiente inicial do programa, estabelecendo a comunicação com o 
        servidor, configurando a interface gráfica e definindo comportamentos associados a eventos do usuário. Essas 
        ações são essenciais para o correto funcionamento do programa, garantindo que ele esteja pronto para interagir 
        com o usuário e responder às suas ações.
        """
        super(Main, self).__init__(parent)
        self.setupUi(self)
        
        self.ip = '192.168.1.15'
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
        self.tela_inicial.pushButton_hotel.clicked.connect(self.listar_hoteis)
        self.tela_inicial.pushButton_restaurante.clicked.connect(self.listar_restaurantes)
        
        self.tela_hoteis.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_hoteis.pushButton_voltat.clicked.connect(self.abrir_tela_inicial)
        self.tela_hoteis.perfilButton.clicked.connect(self.abrir_tela_perfil)
        
        self.tela_restaurantes.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_restaurantes.pushButton_voltat.clicked.connect(self.abrir_tela_inicial)
        self.tela_restaurantes.perfilButton.clicked.connect(self.abrir_tela_perfil)
        
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
        
        self.tela_reserva_gratis.pushButton_sair.clicked.connect(self.sair_do_sistema)
        self.tela_reserva_gratis.pushButton_voltar.clicked.connect(self.voltar_tela_reserva_gratis)
        self.tela_reserva_gratis.pushButton_perfil.clicked.connect(self.abrir_tela_perfil)
        self.tela_reserva_gratis.pushButton_confirmar.clicked.connect(self.ingresso_gratis)
        
        self.tela_nota_fiscal.pushButton.clicked.connect(self.fechar_tela_nota_fiscal)
        
        self.email = ''
        self.monumento = ''
        self.nome = ''
    
    def nota_fiscal(self): 
        """_summary_
        A função nota_fiscal(self) desempenha o papel de solicitar uma nota fiscal ao servidor e exibir as informações 
        orrespondentes na interface gráfica. Aqui está uma descrição passo a passo da função:

      Preparação da mensagem: Cria uma mensagem 'notafiscal' para indicar ao servidor que deseja obter uma nota fiscal. 
      A mensagem é então codificada em bytes e enviada ao servidor através do socket (self.cliente_socket.send(mensagem.encode())).

    Recebimento da resposta do servidor: Aguarda a resposta do servidor, que é esperada ser um objeto JSON contendo informações 
    da nota fiscal. A resposta é decodificada de bytes para uma string (resposta_json = self.cliente_socket.recv(4096).decode('utf-8')).

Processamento da resposta JSON: A resposta JSON é convertida para um dicionário Python usando json.loads. As informações relevantes 
são então extraídas desse dicionário, incluindo idticket, nome_cliente, nome_monumento, data, hora e valor.

Exibição das informações na interface gráfica: Utiliza os valores extraídos do dicionário para preencher os campos relevantes na 
interface gráfica (QLineEdit) da tela de nota fiscal. Isso inclui o nome do cliente, ID do ticket, nome do monumento, data, hora e valor.

Solicitação do QR code: Envia uma nova mensagem 'qrcode' ao servidor para solicitar o QR code correspondente à nota fiscal.

Recebimento e exibição do QR code: Aguarda a resposta do servidor contendo o QR code em formato base64 
(imagem_base64 = self.cliente_socket.recv(16384).decode()). Decodifica a imagem base64 para bytes e, em seguida, 
converte esses bytes em um objeto QPixmap, que é exibido em um QLabel na interface gráfica.
        """
        mensagem = 'notafiscal'
        self.cliente_socket.send(mensagem.encode())
        print(f'Enviada mensagem para o servidor: {mensagem}')

      # Receber a resposta JSON
        resposta_json = self.cliente_socket.recv(4096).decode('utf-8')
        print(f'Recebida resposta do servidor: {resposta_json}')

       # Converte a resposta JSON de volta para um dicionário
        resposta_dict = json.loads(resposta_json)

        # Acessa os valores do dicionário usando as chaves
        idticket = resposta_dict.get('idticket', '')
        nome_cliente = resposta_dict.get('nome_cliente', '')
        nome_monumento = resposta_dict.get('nome_monumento', '')
        data = resposta_dict.get('dia', '')
        hora = resposta_dict.get('horario', '')
        valor = resposta_dict.get('tipo_valor', '')

        print(f'idticket: {idticket}, nome_cliente: {nome_cliente}, nome_monumento: {nome_monumento}, data: {data}, hora: {hora}, valor: {valor}')

        # Abrir a tela de nota fiscal
        self.abrir_tela_nota_fiscal()
        self.tela_nota_fiscal.lineEdit_nome.setText(nome_cliente)
        self.tela_nota_fiscal.lineEdit.setText(str(idticket))
        self.tela_nota_fiscal.lineEdit_tipo.setText(nome_monumento)
        self.tela_nota_fiscal.lineEdit_data.setText(data)
        self.tela_nota_fiscal.lineEdit_horario.setText(hora)
        self.tela_nota_fiscal.lineEdit_valor.setText(valor)

        mensagem = 'qrcode'
        self.cliente_socket.send(mensagem.encode())
        print(f'Enviada mensagem para o servidor: {mensagem}')
    
        imagem_base64 = self.cliente_socket.recv(16384).decode()
        print(f'Recebida resposta do servidor: {imagem_base64}')
        # Decodificar a imagem base64
        imagem_bytes = base64.b64decode(imagem_base64)

        # Converte a imagem para QPixmap e exibe no QLabel
        pixmap = QPixmap()
        pixmap.loadFromData(imagem_bytes)
        self.tela_nota_fiscal.label_qrcode.setPixmap(pixmap)
    
    def ingresso_gratis(self):
        """_summary_
        Busca por Informações do Usuário:

Cria uma mensagem contendo o comando 'busca' e o email do usuário para obter informações do servidor.
Envia essa mensagem ao servidor.
Envio de Solicitação de Ingresso:

Obtém o nome do monumento (self.monumento) e a data selecionada no widget de calendário (dia) na interface gráfica.
Cria uma mensagem contendo o comando 'ingresso', o nome do monumento e a data.
Envia essa mensagem ao servidor.
Recebimento da Resposta do Servidor:

Aguarda a resposta do servidor sobre a disponibilidade do ingresso na data selecionada.
A resposta (um string) é recebida e armazenada na variável resposta.
Tratamento da Resposta:

Verifica se a resposta é 'sim', indicando que o ingresso foi reservado com sucesso.
Em caso afirmativo, exibe uma mensagem de sucesso (self.mostrar_mensagem_sucesso).
Obtém novamente a data selecionada para utilizar na função nota_fiscal.
Chama a função nota_fiscal para gerar e exibir a nota fiscal, que inclui um código QR.
Caso contrário, exibe uma mensagem de erro (self.mostrar_mensagem_erro).
Validação da Data:

Antes de enviar a solicitação ao servidor, verifica se uma data foi selecionada na interface gráfica.
Se nenhuma data foi selecionada, exibe uma mensagem de erro indicando que o usuário deve selecionar uma data.
        Returns:
            _type_: _description_
        """
        mensagem = f'busca;{self.email}'
        self.cliente_socket.send(mensagem.encode())
        print(f'Enviada mensagem para o servidor: {mensagem}')
        monumento = self.monumento
        dia = self.tela_reserva_gratis.calendarWidget.selectedDate().toString("dd-MM-yyyy")
        
        if dia:
            mensagem = f'ingresso;{monumento};{dia}'
            self.cliente_socket.send(mensagem.encode())
            print(f'Enviada mensagem para o servidor: {mensagem}')
            
            resposta = self.cliente_socket.recv(1024).decode()
            print(f'Resposta recebida: {resposta}')
        
            if resposta.lower() == 'sim':
                self.mostrar_mensagem_sucesso("Ingresso reservado com sucesso!")
                dia = self.tela_reserva_gratis.calendarWidget.selectedDate().toString("dd-MM-yyyy")
                self.nota_fiscal()
            else:
                self.mostrar_mensagem_erro("Ingresso não reservado!")
                return None
        else:
            self.mostrar_mensagem_erro("Selecione uma data!")
            return None
        
    def listar_restaurantes(self):
        """
        Abertura da Tela de Restaurantes:

Chama a função abrir_tela_restaurantes para exibir a interface gráfica relacionada aos restaurantes.
Envio de Solicitação ao Servidor:

Cria uma mensagem contendo o comando 'listarrestaurantes'.
Envia essa mensagem ao servidor por meio do socket self.cliente_socket.
Exibe uma mensagem indicando o envio da solicitação.
Recebimento e Processamento da Resposta do Servidor:

Aguarda a resposta do servidor após o envio da solicitação.
A resposta é recebida, decodificada e convertida de JSON para um formato adequado para processamento (resposta = json.loads(resposta)).
Exibe a resposta recebida do servidor (print(f'Recebida resposta do servidor: {resposta}')).
Preenchimento da Tabela na Interface Gráfica:

Configura o número de linhas e colunas na tabela de restaurantes na interface gráfica com base na resposta do servidor.
Utiliza um loop para preencher cada célula da tabela com os dados fornecidos pelo servidor.
        """
        self.abrir_tela_restaurantes()
        mensagem = f'listarrestaurantes'
        self.cliente_socket.send(mensagem.encode())
        print(f'Enviada mensagem para o servidor: {mensagem}')
        
        resposta = self.cliente_socket.recv(1024).decode()
        resposta = json.loads(resposta)
        print(f'Recebida resposta do servidor: {resposta}')
        
        self.tela_restaurantes.tableWidget.setRowCount(len(resposta))
        self.tela_restaurantes.tableWidget.setColumnCount(5)
        for i in range(0, len(resposta)):
            for j in range(0, 5):
                self.tela_restaurantes.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(resposta[i][j]))
    
    def listar_hoteis(self):
        """_summary_ 
        Abertura da Tela de Hotéis:

Chama a função abrir_tela_hoteis para exibir a interface gráfica relacionada aos hotéis.
Envio de Solicitação ao Servidor:

Cria uma mensagem contendo o comando 'listarhoteis'.
Envia essa mensagem ao servidor por meio do socket self.cliente_socket.
Exibe uma mensagem indicando o envio da solicitação.
Recebimento e Processamento da Resposta do Servidor:

Aguarda a resposta do servidor após o envio da solicitação.
A resposta é recebida, decodificada e convertida de JSON para um formato adequado para processamento (resposta = json.loads(resposta)).
Exibe a resposta recebida do servidor (print(f'Recebida resposta do servidor: {resposta}')).
Preenchimento da Tabela na Interface Gráfica:

Configura o número de linhas e colunas na tabela de hotéis na interface gráfica com base na resposta do servidor.
Utiliza um loop para preencher cada célula da tabela com os dados fornecidos pelo servidor.
        """
        self.abrir_tela_hoteis()
        mensagem = f'listarhoteis'
        self.cliente_socket.send(mensagem.encode())
        print(f'Enviada mensagem para o servidor: {mensagem}')
        
        resposta = self.cliente_socket.recv(1024).decode()
        resposta = json.loads(resposta)
        print(f'Recebida resposta do servidor: {resposta}')
        
        self.tela_hoteis.tableWidget.setRowCount(len(resposta))
        self.tela_hoteis.tableWidget.setColumnCount(4)
        for i in range(0, len(resposta)):
            for j in range(0, 4):
                self.tela_hoteis.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(resposta[i][j]))
    
    def sair_do_sistema(self):
        """
        Envio de Mensagem de Desconexão:

Cria uma mensagem contendo o comando 'sair'.
Envia essa mensagem ao servidor por meio do socket self.cliente_socket.
Recebimento da Resposta do Servidor:

Aguarda a resposta do servidor após o envio da mensagem de desconexão.
A resposta é recebida, decodificada e armazenada na variável resposta (resposta = self.cliente_socket.recv(1024).decode()).
Exibe a resposta recebida do servidor (print(f'Resposta recebida: {resposta}')).
Verificação da Resposta para Desconexão:

Verifica se a resposta do servidor indica que o cliente foi desconectado pelo servidor (if resposta.lower() == 'desconectado pelo servidor').
Fechamento e Recriação do Socket em Caso de Desconexão:

Se o cliente foi desconectado pelo servidor, fecha o socket atual (self.cliente_socket.close()).
Cria um novo objeto de socket para o cliente (self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)).
Conecta o novo socket ao endereço do servidor (self.cliente_socket.connect(self.addr)).
Chama a função abrir_tela_login() para exibir a tela de login.
        """
        msg = f'sair'
        self.cliente_socket.send(msg.encode())
        resposta = self.cliente_socket.recv(1024).decode()
        print(f'Resposta recebida: {resposta}')
     
        if resposta.lower() == 'desconectado pelo servidor':
            self.cliente_socket.close() 
            self.cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.cliente_socket.connect(self.addr)
            self.abrir_tela_login()
            
    def sair(self):
        """
        Envio de Mensagem de Desconexão:

Cria uma mensagem contendo o comando 'sair'.
Envia essa mensagem ao servidor por meio do socket self.cliente_socket (self.cliente_socket.send(msg.encode())).
Recebimento da Resposta do Servidor:

Aguarda a resposta do servidor após o envio da mensagem de desconexão.
A resposta é recebida, decodificada e armazenada na variável resposta (resposta = self.cliente_socket.recv(1024).decode()).
Verificação da Resposta para Desconexão:

Verifica se a resposta do servidor indica que o cliente foi desconectado pelo servidor (if resposta.lower() == 'Desconectado pelo servidor').
Fechamento do Socket e da Interface Gráfica:

Se o cliente foi desconectado pelo servidor, fecha o socket atual (self.cliente_socket.close()).
Fecha a interface gráfica do programa (self.close()).
Exibição de Mensagem no Console:

Imprime no console a mensagem indicando que o cliente saiu do sistema (print('Saiu do sistema')).
        """
        msg = 'sair'
        self.cliente_socket.send(msg.encode())
        
        resposta = self.cliente_socket.recv(1024).decode()
        if resposta.lower() == 'Desconectado pelo servidor':
            self.cliente_socket.close()     
        self.close()
        print('Saiu do sistema')  
        
    def login(self):
        """
        Obtenção de Credenciais:

Obtém as credenciais do usuário (e-mail e senha) a partir dos campos de entrada na tela de login 
(email = self.tela_login.lineEdit_email.text() e senha = self.tela_login.lineEdit_senha.text()).
Verificação das Credenciais:

Verifica se tanto o e-mail quanto a senha foram fornecidos (if email and senha:).
Calcula o hash MD5 da senha fornecida (senha_md5 = hashlib.md5(senha.encode()).hexdigest()).
Envio da Mensagem de Login ao Servidor:

Cria uma mensagem contendo o comando 'login', o e-mail e a senha hash MD5.
Envia essa mensagem ao servidor por meio do socket self.cliente_socket (self.cliente_socket.send(mensagem.encode('utf-8'))).
Recebimento da Resposta do Servidor:

Aguarda a resposta do servidor após o envio da mensagem de login.
A resposta é recebida, decodificada e armazenada na variável resposta (resposta = self.cliente_socket.recv(1024).decode('utf-8')).
Verificação da Resposta para Tomar Ações:

Verifica se a resposta do servidor indica um "login bem-sucedido".
Se sim, armazena o e-mail do usuário, limpa os campos de entrada da tela de login, abre a tela inicial e encerra o loop (break).
Se não, exibe mensagens de erro apropriadas e continua aguardando novas tentativas.
Tratamento de Exceções:

Captura exceções como ConnectionResetError e outras exceções genéricas durante o processo de comunicação com o servidor.
Exibe mensagens de erro apropriadas para problemas de conexão ou outros erros desconhecidos.
Validação de Campos Vazios:

Verifica se os campos de e-mail e senha estão vazios e exibe mensagens de erro correspondentes.
        """
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
        """Obtenção de Dados do Formulário:

Obtém os dados do formulário de cadastro, como nome, CPF, data de nascimento, e-mail e senha.
Verificação dos Campos Obrigatórios:

Verifica se nenhum dos campos obrigatórios (nome, CPF, e-mail, senha) está vazio.
Hash da Senha:

Calcula o hash MD5 da senha fornecida (senha_md5 = hashlib.md5(senha.encode()).hexdigest()).
Envio da Mensagem de Cadastro ao Servidor:

Cria uma mensagem contendo o comando 'cadastro' e os dados do usuário.
Envia essa mensagem ao servidor por meio do socket self.cliente_socket (self.cliente_socket.send(msg.encode())).
Recebimento e Tratamento da Resposta do Servidor:

Aguarda a resposta do servidor após o envio da mensagem de cadastro.
A resposta é recebida, decodificada e armazenada na variável resp.
Baseado na resposta, toma diversas ações:
Limpa os campos de entrada e exibe uma mensagem informativa se o cadastro for bem-sucedido.
Exibe mensagens de erro específicas para casos como CPF ou e-mail já cadastrados, e-mails inválidos, senhas 
curtas, CPF inválido, menores de idade, ou outros erros desconhecidos.
Tratamento de Exceções:

Captura exceções genéricas durante o processo de comunicação com o servidor.
Exibe mensagens de erro apropriadas para problemas de conexão ou outros erros desconhecidos.
Validação dos Campos Preenchidos:

Verifica se todos os campos foram preenchidos e exibe uma mensagem de erro caso contrário.
        """
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
                elif resp.lower() == "menor de idade":
                    self.mostrar_mensagem_erro("Menores de idade não podem criar conta.")
                    self.tela_cadastro.dateEdit_nasci.setDate(QDate.currentDate())
                else:
                    self.mostrar_mensagem_erro("Erro na criação de conta")
                    
            except Exception as e:
                print(f"Erro: {e}")
        else:
            self.mostrar_mensagem_erro("Preencha todos os campos")
        
    def cancelar_cad(self):
        QMessageBox.information(None, '...', 'Cadastro cancelado!')
        self.QtStack.setCurrentIndex(0)

    def excluir_conta(self):
        senha = self.tela_conf_com_senha.lineEdit.text()
        if senha:
            try:
                senha_md5 = hashlib.md5(senha.encode()).hexdigest()
                
                msg = f'excluir;{self.email};{senha_md5}'
                print(f'Mensagem enviada: {msg}')
                self.cliente_socket.send(msg.encode())
                
                resp = self.cliente_socket.recv(1024).decode()
                print(f'Resposta recebida: {resp}')
                
                if resp.lower() == "conta excluida com sucesso!":
                    self.tela_conf_com_senha.lineEdit.setText("")
                    print("Conta excluida com sucesso!")
                    QMessageBox.information(None, '...', 'Conta excluida com sucesso!')
                    self.abrir_tela_login()
                    
                elif resp.lower() == "senha incorreta":
                    self.mostrar_mensagem_erro("Senha incorreta. Tente novamente.")
                    self.tela_conf_com_senha.lineEdit.setText("")
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
        
    def mostrar_mensagem_sucesso(self, mensagem):
        QMessageBox.information(self, "...", mensagem)

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
        self.monumento = 'CASA DA POLVORA'
        print(self.monumento)
        mensagem = 'CASA DA POLVORA'
        self.cliente_socket.send(mensagem.encode())
        self.QtStack.setCurrentIndex(3)
        
    def abrir_tela_reserva_gratis(self):
        try:
            mensagem = f'buscahorario;{self.monumento}'
            self.cliente_socket.send(mensagem.encode())
            print(f'Enviada mensagem para o servidor: {mensagem}')
            resposta = self.cliente_socket.recv(1024).decode() 
            print(f'Recebida resposta do servidor: {resposta}')
            
            self.tela_reserva_gratis.lineEdit_2.setText(resposta)
            self.tela_reserva_gratis.lineEdit_3.setText(self.monumento)
            self.QtStack.setCurrentIndex(4)
            
        except Exception as e:
            print(f"Erro ao abrir a tela de reserva: {e}")
        
    def busca_nome(self):
        try:
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
                resposta = self.cliente_socket.recv(1024).decode()
                
                self.QtStack.setCurrentIndex(5)        
                
            else:
                print("Resposta do servidor em formato inesperado.")
        except Exception as e:
            print(f"Erro ao abrir a tela de perfil: {e}")
    
    def abrir_tela_perfil(self):
        self.QtStack.setCurrentIndex(5)
        self.busca_nome()
    
    def abrir_tela_conf_com_senha(self):
        self.stack6.show()
    
    def abrir_tela_reserva_paga(self):
        self.QtStack.setCurrentIndex(7)
        
    def abrir_tela_hoteis(self):
        self.QtStack.setCurrentIndex(8)
        
    def abrir_tela_restaurantes(self):
        self.QtStack.setCurrentIndex(9)
        
    def abrir_tela_nota_fiscal(self):
        self.QtStack.setCurrentIndex(10)
        
    def fechar_tela_nota_fiscal(self):
        self.stack10.close()
        self.abrir_tela_inicial()
        
    def voltar_tela_reserva_gratis(self):
        if self.monumento == 'CASA DA POLVORA':
            self.stack4.close()
            self.QtStack.setCurrentIndex(3)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
    
    