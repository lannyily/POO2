import threading
import socket
import mysql.connector as mysql

conexao = mysql.connect(
    host='localhost', database='turismo', user='root', passwd='amor2004')
cursor = conexao.cursor()

class ClienteThread(threading.Thread):
    def __init__(self, clientAddress, clientesocket):
        threading.Thread.__init__(self)
        self.csocket = clientesocket
        self.addr = clientAddress
        print('Nova conexão:', clientAddress)

    def run(self):
        try:
            data = self.csocket.recv(1024).decode()
            operacao, *dados = data.split(';')
            dados = ';'.join(dados)
            print('Operação:', operacao)
            print('Dados:', dados)
            
            if operacao == 'sair':
                print('Cliente solicitou sair. Fechando a conexão...')
                self.csocket.send("Desconectado pelo servidor".encode())
                self.csocket.close()
                print('aqui1')
                return

            elif operacao == 'login':
                if self.verificar_usuario_senha(dados):
                    self.csocket.send("Login bem-sucedido!".encode('utf-8'))
                    print(f'{email} se conectou!')
                        
                    data = self.csocket.recv(1024).decode('utf-8')
                    operacao, *dados = data.split(';')
                    dados = ';'.join(dados)
                    print('Operação:', operacao)
                    print('Dados:', dados)

                    if operacao == 'busca':
                        email_busca = dados.split(';')[0]
                        print(email_busca)
                        print("Realizando busca...")
                        resultado = self.busca(email_busca)
                    else:
                        print('Erro')
                else:
                    self.csocket.send("Usuário ou senha incorretos.".encode())
            elif operacao == 'cadastro':
                nome, cpf, dataN, email, senha = dados.split(';')

                if self.cadastrar_novo_usuario(nome, cpf, dataN, email, senha):
                    self.csocket.send("Conta criada com sucesso!".encode())
                    print(f'{nome} tem uma conta no sistema!')
                else:
                    self.csocket.send("Erro na criação da conta".encode())
            else:
                print(f'Operação não reconhecida: {operacao}')
        except Exception as e:
            print(f"Erro durante a execução da thread: {e}")
        
    def verificar_usuario_senha(self, dados):
        while True:
            email, senha = dados.split(';')
            print('email:', email)
            print('senha:', senha)
            print("1")
     
            try:
                print('2')
                with conexao.cursor() as cursor:
                    print("3")
                    cursor.execute(
                        "SELECT * FROM contas WHERE email = %s AND senha = %s", (email, senha))
                    print('4')                   
                    resultado = cursor.fetchone()
                    print('5')
                    print(resultado)
                if resultado:
                    print(resultado)
                    return True       
                else:
                    return False
            except mysql.Error as err:
                print(f"Erro ao acessar o banco de dados: {err}")
                erro_str = f"Erro ao acessar o banco de dados: {str(err)}"
                self.csocket.send(erro_str.encode('utf-8'))
                return False

    def cadastrar_novo_usuario(self, nome, cpf, dataN, email, senha):
        try:
            cursor.execute("INSERT INTO contas (nome, cpf, dataN, email, senha) VALUES (%s, %s, %s, %s, %s)",
                           (nome, cpf, dataN, email, senha))

            conexao.commit()
            print("Dados inseridos com sucesso!")
            return True
        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return False

    def busca(self, email):
        try:
            sql = "SELECT nome, email FROM contas WHERE email = %s"

            cursor.execute(sql, (email,))
            resultado = cursor.fetchone()
            if resultado:
                nome, email_encontrado = resultado
                print(resultado)
                resposta = f'{nome};{email_encontrado}'
                self.csocket.send(resposta.encode())
            else:
                print("Erro, não foi encontrado")
                self.csocket.send("Não encontrado".encode())
        except Exception as e:
            print(f"Erro durante a busca: {e}")
        finally:
            self.csocket.close()


if __name__ == '__main__':
    localhost = ''
    port = 1600
    addr = (localhost, port)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    print('Servidor iniciado!')
    print('Aguardando nova conexão...')

    while True:
        server.listen(20)
        clientsock, clientAddress = server.accept()
        newthread = ClienteThread(clientAddress, clientsock)
        newthread.start()
