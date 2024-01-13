import threading
import socket
import mysql.connector as mysql
import re
import datetime
import json

conexao = mysql.connect(
    host='localhost', database='turismo', user='root', passwd='amor2004')
cursor = conexao.cursor()

class ClienteThread(threading.Thread):
    def __init__(self, clientAddress, clientesocket):
        threading.Thread.__init__(self)
        self.csocket = clientesocket
        self.addr = clientAddress
        self.tipo_usuario = ''
        print('Nova conexão:', clientAddress)
        
    def run(self):
        data = self.csocket.recv(1024).decode()
        tipo_usuario = data.split(';')[0]
        print('Tipo de usuário:', tipo_usuario)
        
        self.tipo_usuario = tipo_usuario
        
        if tipo_usuario == 'cliente':
            self.run_cliente()
        elif tipo_usuario == 'funcionario':
            self.run_funcionario()
        elif tipo_usuario == 'sair':
            print('O Usuário solicitou sair. Fechando a conexão...')
            self.csocket.send("Desconectado pelo servidor".encode('utf-8'))
            self.csocket.close()
        else:
            print(f'Tipo de usuário não reconhecido: {tipo_usuario}')
            self.csocket.close()
    
    def run_funcionario(self):
        try:
            while True:
                data = self.csocket.recv(1024).decode()
                print('Aguardando operação...')
                operacao, *dados = data.split(';')
                print('Aguardando operação...')
                dados = ';'.join(dados)
                print('Operação externa:', operacao)
                print('Dados:', dados)
                
                if operacao == 'sair':
                    self.sair()
                    break
                
                elif operacao == 'loginadmin':
                    print('Verificando senha...')
                    if self.verificar_senha_admin(dados):
                        self.csocket.send("Login efetuado com sucesso".encode('utf-8'))
                        print('O administrador se conectou!')
                        
                        while True:
                            data_operacao = self.csocket.recv(1024).decode('utf-8')
                            operacao, *dados_operacao = data_operacao.split(';')
                            dados_operacao = ';'.join(dados_operacao)
                            print('Operação dentro do login:', operacao)
                            print('Dados:', dados_operacao)
                            
                            if operacao == 'sair':
                                self.sair()
                                break
                            
                            if operacao == 'autenticar':
                                if self.verificar_senha_admin(dados_operacao):
                                    senha_antiga = dados_operacao.split(';')[0]
                                    self.csocket.send("Login efetuado com sucesso".encode('utf-8'))
                                    print('Agora o administrador pode mudar a senha!')
                                    
                                    data_operacao = self.csocket.recv(1024).decode('utf-8')
                                    operacao, *dado = data_operacao.split(';')
                                    dado = ';'.join(dado)
                                    print('Operação dentro do atualizar senha:', operacao)
                                    print('Dados:', dado)
                                    
                                    if operacao == 'atualizar':
                                        print(f'Senha antiga: {senha_antiga}')
                                        print(f'Senha nova: {dado}')
                                        if self.atualizar_senha_admin(dado, senha_antiga):
                                            self.csocket.send("Senha atualizada com sucesso!".encode('utf-8'))
                                        else:
                                            self.csocket.send("Erro ao atualizar a senha".encode('utf-8'))
                                    else:
                                        print('Operação não reconhecida:', operacao)
                                else:
                                    self.csocket.send("Senha incorreta".encode('utf-8'))
                                    print('Senha incorreta. Tente novamente.')
                            elif operacao == 'listarusuarios':
                                self.listar_usuarios()
                                print('Listando usuários...')
                                while True:
                                    operacao_data = self.csocket.recv(1024).decode('utf-8')
                                    operacao_data, *dados = operacao_data.split(';')
                                    dados = ';'.join(dados)
                                    print('Operação dentro de listar:', operacao_data)
                                    print('Dados:', dados)
                                
                                    if operacao_data == 'sair':
                                        self.sair()
                                        break
                                
                                    if operacao_data == 'busca':
                                        print('Buscando usuário...')
                                        resultado = self.buscar_nome_por_email(dados)
                                        email = dados.split(';')[0]
                                        if resultado:
                                            self.csocket.send(resultado[0].encode('utf-8'))
                                            
                                            while True:
                                                operacao_usuario = self.csocket.recv(1024).decode('utf-8')
                                                operacao_usuario, *dado = operacao_usuario.split(';')
                                                dado = ';'.join(dado)
                                                print('Operação dentro do usuario:', operacao_usuario)
                                                print('Dados:', dado)
                                                
                                                if operacao_usuario == 'mostarconta':
                                                    self.mostrar_usuario(email)
                                                    
                                                    while True:
                                                        operacao_user = self.csocket.recv(1024).decode('utf-8')
                                                        operacao_user, *dad = operacao_user.split(';')
                                                        dad = ';'.join(dad)
                                                        print('Operação dentro do user:', operacao_user)
                                                        print('Dados:', dad)
                                                        
                                                        if operacao_user == 'excluir':
                                                                print('Senha correta. Excluindo conta...')
                                                                self.excluir_conta(email)
                                                                self.csocket.send("conta excluida com sucesso".encode('utf-8'))
                                                                break
                                                        else:
                                                            print('Operação não reconhecida:', operacao_user)
                                                else:
                                                    print('Operação não reconhecida:', operacao_usuario)
                                        else:
                                            print('Erro ao realizar busca')
                                    else:
                                        print('Operação não reconhecida:', operacao_data)
                    else:
                        self.csocket.send("Senha incorreta".encode('utf-8'))
                        print('Senha incorreta. Tente novamente.')
                else:
                    print('Operação não reconhecida:', operacao)
        except Exception as e:
            print(f"Erro durante a execução da thread: {e}")
        finally:
            self.csocket.close()
    
    def run_cliente(self):
        try:
            while True:
                data = self.csocket.recv(1024).decode()
                operacao, *dados = data.split(';')
                dados = ';'.join(dados)
                print('Operação externa:', operacao)
                print('Dados:', dados)

                if operacao == 'sair':
                    self.sair()
                    break

                elif operacao == 'login':
                    if self.verificar_usuario_senha(dados):
                        self.csocket.send("Login bem-sucedido!".encode('utf-8'))
                        print(f'{dados} se conectou!')

                        while True:
                            data_operacao = self.csocket.recv(1024).decode('utf-8')
                            operacao, *dados_operacao = data_operacao.split(';')
                            dados_operacao = ';'.join(dados_operacao)
                            print('Operação dentro do login:', operacao)
                            print('Dados:', dados_operacao)
                            
                            if operacao == 'sair':
                                self.sair()
                                break
                            
                            if operacao == 'busca':
                                email_busca = dados_operacao.split(';')[0]
                                print(email_busca)
                                print("Realizando busca...")
                                resultado = self.busca(email_busca)
                                
                                if resultado:
                                    data_operacao = self.csocket.recv(1024).decode('utf-8')
                                    operacao, *dados_operacao = data_operacao.split(';')
                                    dados_operacao = ';'.join(dados_operacao)
                                    print('Operação dentro do perfil:', operacao)
                                    print('Dados:', dados_operacao)
                                    
                                    if operacao == 'excluir':
                                        print('Excluindo conta...')
                                        if self.verificar_usuario_senha(dados_operacao):
                                            self.excluir_conta(email_busca)
                                            break
                                        else:
                                            self.csocket.send("Senha incorreta".encode('utf-8'))
                                    else:
                                        print('Operação não reconhecida:', operacao)
                                else:
                                    print('Erro ao realizar busca')
                            else:
                                print('Operação não reconhecida:', operacao)

                    else:
                        self.csocket.send("Usuário ou senha incorretos.".encode('utf-8'))
                        print('Usuário ou senha incorretos. Tente novamente.')
                        
                elif operacao == 'cadastro':
                    nome, cpf, dataN, email, senha = dados.split(';')
                    
                    if not self.validar_email(email):
                        print('Email inválido')
                        self.csocket.send("Email invalido".encode('utf-8'))
                        return False
                    
                    if len(senha) < 8:
                        print('Senha muito curta')
                        self.csocket.send("Senha muito curta".encode('utf-8'))
                        return False
                    
                    if not self.validar_cpf(cpf):
                        print('CPF inválido')
                        self.csocket.send("CPF invalido".encode('utf-8'))
                        return False
                    
                    if not self.verificar_maioridade(dataN):
                        print('Menor de idade')
                        self.csocket.send("Menor de idade".encode('utf-8'))
                        return False
                    
                    sucesso = self.cadastrar_novo_usuario(nome, cpf, dataN, email, senha)
                    print(sucesso)
                    if sucesso == True:
                        print(f'{nome} tem uma conta no sistema!')
                        return
                    elif sucesso == cpf:
                        print('CPF já cadastrado. Não é possível criar a conta')
                        self.csocket.send("CPF ja cadastrado. Nao e possivel criar a conta".encode('utf-8'))
                    elif sucesso == email:
                        print('Email já cadastrado. Não é possível criar a conta')
                        self.csocket.send("Email ja cadastrado. Nao e possivel criar a conta".encode('utf-8'))
                    else:
                        print('Erro ao criar conta')
                else:
                    print(f'Operação não reconhecida: {operacao}')

        except Exception as e:
            print(f"Erro durante a execução da thread: {e}")
        finally:
            self.csocket.close()
    
    def excluir_conta(self, email):
        try:
            with conexao.cursor() as cursor:
                cursor.execute("DELETE FROM contas WHERE email = %s", (email,))
                conexao.commit()
                self.csocket.send("Conta excluida com sucesso!".encode('utf-8'))
        except Exception as e:
            print(f"Erro durante a exclusão da conta: {e}")
    
    def verificar_usuario_senha(self, dados):
        while True:
            email, senha = dados.split(';')
            print('email:', email)
            print('senha:', senha)
     
            try:
                with conexao.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM contas WHERE email = %s AND senha = %s", (email, senha))                   
                    resultado = cursor.fetchone()
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
            cursor.execute("SELECT * FROM contas WHERE cpf = %s OR email = %s", (cpf, email))
            existing_user = cursor.fetchone()
            if existing_user:
                cpf_db, email_db = existing_user[2], existing_user[4]
                if cpf_db == cpf:
                    print('Encontrou o cpf no banco de dados')
                    print(cpf_db)
                    return cpf_db
                elif email_db == email:
                    print('Encontrou o email no banco de dados')
                    print(email_db)
                    return email_db
            else:
                cursor.execute("INSERT INTO contas (nome, cpf, dataN, email, senha) VALUES (%s, %s, %s, %s, %s)",
                        (nome, cpf, dataN, email, senha))

                conexao.commit()
                self.csocket.send("Dados inseridos com sucesso!".encode('utf-8'))
                return True
        except mysql.Error as err:
            mensagem_erro = f"Erro ao acessar o banco de dados: {err}"
            print(mensagem_erro)
            self.csocket.send(mensagem_erro.encode('utf-8'))
            return False, "Erro na criação da conta."
        except Exception as e:
            mensagem_erro = f"Erro durante o cadastro: {e}"
            print(mensagem_erro)
            self.csocket.send(mensagem_erro.encode('utf-8'))
            return False, "Erro na criação da conta."

    def validar_email(self, email):
        padrao = r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(padrao, email))

    def validar_cpf(self, cpf):
        cpf_numerico = re.sub(r'\D', '', cpf)
        
        if len(cpf_numerico) != 11:
            return False

        soma = 0
        for i in range(9):
            soma += int(cpf_numerico[i]) * (10 - i)
        resto = soma % 11
        digito1 = 11 - resto if resto >= 2 else 0

        if digito1 != int(cpf_numerico[9]):
            return False

        soma = 0
        for i in range(10):
            soma += int(cpf_numerico[i]) * (11 - i)
        resto = soma % 11
        digito2 = 11 - resto if resto >= 2 else 0

        if digito2 != int(cpf_numerico[10]):
            return False

        return True

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

    def verificar_maioridade(data_nascimento):
        data_nascimento = datetime.strptime(data_nascimento, '%d-%m-%Y')
        data_atual = datetime.now()
        idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))

        if idade >= 18:
            return True
        else:
            return False
        
    def verificar_senha_admin(self, dados):
        while True:
            senha = dados.split(';')[0]
            try:
                conexao = mysql.connect(
                host='localhost', database='turismo', user='root', passwd='amor2004')
                cursor = conexao.cursor()
                cursor.execute(
                    "SELECT * FROM senha_admin WHERE senha = %s", (senha,))
                resultado = cursor.fetchone()
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

    def atualizar_senha_admin(self, dados, senha_antiga):
        try:
            senha = dados.split(';')[0]

            with conexao.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM senha_admin WHERE senha = %s", (senha_antiga,))
                achei = cursor.fetchone()

                if achei:
                    cursor.execute(
                        "UPDATE senha_admin SET senha = %s WHERE senha = %s", (senha, senha_antiga))
                    conexao.commit()
                    
                    self.csocket.send("Senha atualizada com sucesso.".encode('utf-8'))
                    return True
                else:
                    self.csocket.send("Senha antiga incorreta.".encode('utf-8'))
                    return False

        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            erro_str = f"Erro ao acessar o banco de dados: {str(err)}"
            self.csocket.send(erro_str.encode('utf-8'))
            return False

        finally:
            conexao.close()

    def listar_usuarios(self):
        try:
            with conexao.cursor() as cursor:
                cursor.execute("SELECT * FROM contas")
                resultado = cursor.fetchall()

                json_resultado = json.dumps(resultado)
                self.csocket.send(json_resultado.encode('utf-8'))
        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return False
        finally:
            conexao.close()
            
    def mostrar_usuario(self, dado):
        try:
            conexao = mysql.connect(
                host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()   
            cursor.execute("SELECT * FROM contas WHERE email = %s", (dado,))
            resultado = cursor.fetchone()
            json_resultado = json.dumps(resultado)
            self.csocket.send(json_resultado.encode('utf-8'))
        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return False
        finally:
            conexao.close()

    def buscar_nome_por_email(self, dados):
        try:
            email = dados.split(';')[0]
            conexao = mysql.connect(
                host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("SELECT nome FROM contas WHERE email = %s", (email,))
            resultado = cursor.fetchone()
            return resultado
        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return False
        finally:
            conexao.close()   
        
    def excluir_conta(self, email):
        try:
            conexao = mysql.connect(
              host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM contas WHERE email = %s", (email,))
            conexao.commit()
        except Exception as e:
            print(f"Erro durante a exclusão da conta: {e}")
        
    def sair(self):
        print('Cliente solicitou sair. Fechando a conexão...')
        self.csocket.send("Desconectado pelo servidor".encode('utf-8'))
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
