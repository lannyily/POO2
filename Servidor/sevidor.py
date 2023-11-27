import threading
import socket
import mysql.connector as mysql
# conexao com mysql
conexao = mysql.connect(
    host='localhost', database='turismo', user='root', passwd='amor2004')
cursor = conexao.cursor()

# bloqueio
lock = threading.Lock()


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

            if operacao == 'login':
                email, senha = dados.split(';')
                print('email:', email)
                print('senha:', senha)

                with lock:
                    if self.verificar_usuario_senha(email, senha):
                        self.csocket.send("Login bem-sucedido!".encode())
                        print(f'{email} se conectou!')

                        while True:
                            try:
                                data = self.csocket.recv(1024).decode()
                                if not data:
                                    print(f'Conexão encerrada por {self.addr}')
                                    break

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
                            except ConnectionResetError:
                                print(f'Conexão encerrada por {self.addr}')
                                break
                    else:
                        self.csocket.send(
                            "Usuário ou senha incorretos.".encode())
            elif operacao == 'cadastro':
                nome, cpf, dataN, email, senha = dados.split(';')

                with lock:
                    if self.cadastrar_novo_usuario(nome, cpf, dataN, email, senha):
                        self.csocket.send("Conta criada com sucesso!".encode())
                        print(f'{nome} tem uma conta no sistema!')
                    else:
                        self.csocket.send("Erro na criação da conta".encode())
            else:
                print(f'Operação não reconhecida: {operacao}')
        except Exception as e:
            print(f"Erro durante a execução da thread: {e}")
        finally:
            self.csocket.close()

    def verificar_usuario_senha(self, email, senha):
        try:
            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM contas WHERE email = %s AND senha = %s", (email, senha))
                resultado = cursor.fetchone()

            if resultado:
                print(resultado)
                return resultado
            else:
                print("Usuário/senha não encontrados.")
                return None
        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
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
