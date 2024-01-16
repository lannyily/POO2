import threading
import socket
import mysql.connector as mysql
import re
import datetime
import json
import random
from io import BytesIO
import base64
import qrcode
from PIL import Image


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
                        
                        #while True:
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
                        elif operacao == 'listarhoteis':
                            self.listar_hoteis()
                            while True:
                                operacao_hoteis = self.csocket.recv(1024).decode('utf-8')
                                operacao_hoteis, *dados_hotel = operacao_hoteis.split(';')
                                dados_hotel = ';'.join(dados_hotel)
                                print('Operação dentro de listar hoteis:', operacao_hoteis)
                                print('Dados:', dados_hotel)
                                    
                                if operacao_hoteis == 'sair':
                                    self.sair()
                                    break
                                    
                                if operacao_hoteis == 'addhotel':
                                    nome, endereco, entacionamento, piscina, link = dados_hotel.split(';')
                                    
                                    sucesso = self.cadastrar_novo_hotel(nome, endereco, entacionamento, piscina, link)
                                    print(sucesso)
                                    if sucesso == True:
                                        print(f'{nome} esta cadastrado no sistema!')
                                        self.csocket.send("sim".encode('utf-8'))
                                        break
                                    elif sucesso == nome:
                                        print('Nome já cadastrado. Não é possível criar a conta')
                                        self.csocket.send("nome".encode('utf-8'))
                                        break
                                    elif sucesso == endereco:
                                        print('Endereco já cadastrado. Não é possível criar a conta')
                                        self.csocket.send("endereco".encode('utf-8'))
                                        break
                                    else:
                                       print('Erro ao adicionar hotel')
                                elif operacao_hoteis == 'buscahotel':
                                    hotel = self.busca_hotel(dados_hotel)
                                    self.csocket.send(hotel[0].encode('utf-8'))
                                    id_hotel = dados_hotel.split(';')[0]
                                while True:
                                    operacao_excluir_hotel = self.csocket.recv(1024).decode('utf-8')
                                    operacao_excluir_hotel, *dados_excluir_hotel = operacao_excluir_hotel.split(';')
                                    dados_excluir_hotel = ';'.join(dados_excluir_hotel)
                                    print('Operação dentro de excluir hotel:', operacao_excluir_hotel)
                                    print('Dados:', dados_excluir_hotel)
                                        
                                    if operacao_excluir_hotel == 'sair':
                                        self.sair()
                                        break
                                            
                                    if operacao_excluir_hotel == 'excluirhotel':
                                        self.excluir_hotel(id_hotel)
                                        self.csocket.send("hotel excluido com sucesso".encode('utf-8'))
                                        break
                                    else:
                                        print('Operação não reconhecida:', operacao_excluir_hotel)
                                else:
                                    print('Operação não reconhecida:', operacao_hoteis)
                         
                        elif operacao == 'listarrestaurantes':
                            self.listar_restaurantes()
                            
                            operacao_restaurantes = self.csocket.recv(1024).decode('utf-8')
                            operacao_restaurantes, *dados_restaurante = operacao_restaurantes.split(';')
                            dados_restaurante = ';'.join(dados_restaurante)
                            print('Operação dentro de listar restaurantes:', operacao_restaurantes)
                            print('Dados:', dados_restaurante)  
                            
                            if operacao_restaurantes == 'sair':
                                self.sair()
                                break
                            
                            if operacao_restaurantes == 'addrestaurante':
                                nome_restaurante, endereco_restaurante, estacionamento, refeicaoLocal, delivery, link_restaurante = dados_restaurante.split(';')
                                sucesso = self.cadastrar_novo_restaurante(nome_restaurante, endereco_restaurante, estacionamento, refeicaoLocal, delivery, link_restaurante)
                                print(sucesso)
                                if sucesso == True:
                                    print(f'{nome_restaurante} esta cadastrado no sistema!')
                                    self.csocket.send("sim".encode('utf-8'))
                                    break
                                elif sucesso == nome_restaurante:
                                    print('Nome já cadastrado. Não é possível criar a conta')
                                    self.csocket.send("nome".encode('utf-8'))
                                    break
                                elif sucesso == endereco_restaurante:
                                    print('Endereco já cadastrado. Não é possível criar a conta')
                                    self.csocket.send("endereco".encode('utf-8'))
                                    break
                                else:
                                    print('Erro ao adicionar restaurante')
                            elif operacao_restaurantes == 'buscarestaurante':
                                restaurante = self.busca_restaurante(dados_restaurante)
                                self.csocket.send(restaurante[0].encode('utf-8'))
                                id_restaurante = dados_restaurante.split(';')[0]
                                
                                operacao_excluir_restaurante = self.csocket.recv(1024).decode('utf-8')
                                operacao_excluir_restaurante, *dados_excluir_restaurante = operacao_excluir_restaurante.split(';')
                                dados_excluir_restaurante = ';'.join(dados_excluir_restaurante)
                                print('Operação dentro de excluir restaurante:', operacao_excluir_restaurante)
                                print('Dados:', dados_excluir_restaurante)
                                
                                if operacao_excluir_restaurante == 'sair':
                                    self.sair()
                                    break
                                
                                if operacao_excluir_restaurante == 'excluirrestaurante':
                                    self.excluir_restaurante(id_restaurante)
                                    self.csocket.send("restaurante excluido com sucesso".encode('utf-8'))
                                    break
                                else:
                                    print('Operação não reconhecida:', operacao_excluir_restaurante)
                            else:
                                print('Operação não reconhecida:', operacao_restaurantes)            
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
                                self.busca(email_busca)
                                
            
                            elif operacao == 'CASA DA POLVORA':
                                local = 'CASA DA POLVORA'
                                operacao_casa_da_polvora = self.csocket.recv(1024).decode('utf-8')
                                operacao_casa_da_polvora, *dados_casa_da_polvora = operacao_casa_da_polvora.split(';')
                                dados_casa_da_polvora = ';'.join(dados_casa_da_polvora)
                                print('Operação dentro de casa da polvora:', operacao_casa_da_polvora)
                                print('Dados:', dados_casa_da_polvora)
                                
                                if operacao_casa_da_polvora == 'sair':
                                    self.sair()
                                    break
                                
                                if operacao_casa_da_polvora == 'buscahorario':
                                    local_busca = dados_casa_da_polvora.split(';')[0]
                                    print(local_busca)
                                    resposta = self.buscar_horario(local_busca)
                                    self.csocket.send(resposta.encode())
                                    print('Horario encontrado')
                                    while True:
                                        casa_da_polvora = self.csocket.recv(1024).decode('utf-8')
                                        casa_da_polvora, *dado_casa_da_polvora = casa_da_polvora.split(';')
                                        dado_casa_da_polvora = ';'.join(dado_casa_da_polvora)
                                        print('Operação dentro de casa da polvora ingresso:', casa_da_polvora)
                                        print('Dados:', dado_casa_da_polvora)
                                        print('1 Reservando ingresso...')
                                    
                                        if casa_da_polvora == 'busca':
                                            email_busca = dado_casa_da_polvora.split(';')[0]
                                            print('Email: ', email_busca)
                                            nome_cliente = self.buscar_nome_por_email(email_busca)
                                            nome_cliente = str(nome_cliente[0])
                                            print('Nome: ', nome_cliente)
                                        
                                    
                                        if casa_da_polvora == 'ingresso':
                                            print('2 Reservando ingresso...')
                                        
                                            nome_monumento, data = dado_casa_da_polvora.split(';')
                                            print('3 Reservando ingresso...')
                                            horario = self.buscar_horario(local)
                                            print('horario:', horario)
                                            print('4 Reservando ingresso...')
                                            idticket = self.codigo()
                                            print('5 Reservando ingresso...')
                                            sucesso = self.criar_ingresso_gratuito(idticket, nome_cliente, nome_monumento, data, horario)
                                            print('6 Reservando ingresso...')
                                            print(sucesso)
                                            if sucesso == True:
                                                print(f'{nome_cliente} reservou um ingresso!')
                                                self.csocket.send("sim".encode('utf-8'))
                                                
                                                nota_fiscal = self.csocket.recv(1024).decode('utf-8')
                                                nota_fiscal, *dados_nota_fiscal = nota_fiscal.split(';')
                                                dados_nota_fiscal = ';'.join(dados_nota_fiscal)
                                                print('Operação dentro de nota fiscal:', nota_fiscal)
                                                print('Dados:', dados_nota_fiscal)
                                                if nota_fiscal == 'notafiscal':
                                                    nota = self.buscar_ticket(idticket)
                                                    self.csocket.send(nota.encode('utf-8'))
                                                    print('Nota fiscal enviada')
                                                    
                                                    qr_code = self.csocket.recv(1024).decode('utf-8')
                                                    qr_code, *dados_qr_code = qr_code.split(';')
                                                    dados_qr_code = ';'.join(dados_qr_code)
                                                    print('Operação dentro de qr code:', qr_code)
                                                    print('Dados:', dados_qr_code)
                                                    
                                                    if qr_code == 'qrcode':
                                                        self.buscar_qrcode(idticket)
                                                        print('QR code enviado')
                                                        break
        
                                                
                                                else:
                                                    print('Operação não reconhecida:', nota_fiscal)
                                                    break
                                            break
                                        else:
                                            print('Erro ao reservar ingresso')
                            elif operacao == 'listarhoteis':
                                self.listar_hoteis_cliente()
                                print('Listando hoteis...')
                                break        
                            elif operacao == 'listarrestaurantes':
                                self.listar_restaurantes_cliente()
                                print('Listando restaurantes...')
                                break
                            else:
                                print('Operação não reconhecida:', operacao)
                                break

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
                    break
        except Exception as e:
            print(f"Erro durante a execução da thread: {e}")
        finally:
            self.csocket.close()
            
    def listar_tickets_user(self, nome):
        try:
            conexao = mysql.connect(
                host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("SELECT idticket, nome_monumento, dia, horario, tipo_valor FROM ticket WHERE nome_cliente = %s", (nome,))
            resultado = cursor.fetchall()
            print(resultado)
            json_resultado = json.dumps(resultado)
            self.csocket.send(json_resultado.encode('utf-8'))
            print(json_resultado)
        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return False
        finally:
            conexao.close()
    
            
    def buscar_qrcode(self, idticket):
        try:
            conexao = mysql.connect(
                host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor(dictionary=True)

            print('Buscar imagem do QR code')
            cursor.execute("SELECT imagem FROM qrcodes WHERE id = %s", (idticket,))
            resultado = cursor.fetchone()

            if resultado:
                imagem_bytes = resultado['imagem']

                print('Converter imagem para base64')
                imagem_base64 = base64.b64encode(imagem_bytes).decode()

                print('Fechar o cursor e a conexão')
                cursor.close()
                conexao.close()
            
                self.csocket.send(imagem_base64.encode())
                print('Imagem enviada')
            else:
                print('QR code não encontrado para o ID fornecido')

        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return None  # Ou qualquer valor que faça sentido no seu contexto
        except Exception as e:
            print(f"Erro durante a execução da thread: {e}")
            return None  # Ou qualquer valor que faça sentido no seu contexto

    def buscar_ticket(self, idticket):
        try:
            conexao = mysql.connect(
                host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor(dictionary=True)

        # Buscar informações do ticket
            cursor.execute("SELECT * FROM ticket WHERE idticket = %s", (idticket,))
            resultado_ticket = cursor.fetchone()
            json_resultado = json.dumps(resultado_ticket)
        # Fechar o cursor e a conexão
            cursor.close()
            conexao.close()

        # Retornar um dicionário contendo as informações do ticket e a imagem em base64
            return json_resultado
        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return False
        except Exception as e:
            print(f"Erro durante a execução da thread: {e}")

    def buscar_horario(self, monumento):
        try:
            conexao = mysql.connect(
                host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("SELECT horario FROM monumentos WHERE nome = %s", (monumento,))
            resultado = cursor.fetchone()

            if resultado:
                horario = resultado[0]  
                return horario
            else:
                print(f"Não foram encontrados horários para o monumento {monumento}")
                self.csocket.send("Nenhum horário encontrado.".encode())

        except mysql.connector.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return False
        except Exception as e:
            print(f"Erro durante a execução da thread: {e}")
        finally:
            cursor.close()
            conexao.close()
    
    def gerar_idticket(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(8)])

    def codigo(self):
        while True:
            codigo = self.gerar_idticket()
            if self.codigo_nao_repetido(codigo):
                return codigo

    def codigo_nao_repetido(self, codigo):
        try:
            conexao = mysql.connect(
                host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            query = "SELECT COUNT(*) FROM ticket WHERE idticket = %s"
            cursor.execute(query, (codigo,))
            resultado = cursor.fetchone()
            return resultado[0] == 0
        except mysql.connector.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return False
        except Exception as e:
            print(f"Erro durante a execução da thread: {e}")
        finally:
            cursor.close()
            conexao.close()  
    
    def criar_ingresso_pago(self, idticket, nome_cliente, nome_monumento, data, horario, valor):
        try:
            conexao = mysql.connect(
              host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO ingressos (idticket, nome_cliente, nome_monumento, data, horario, tipo_valor) VALUES (%s, %s, %s, %s, %s, %s)",
                    (idticket, nome_cliente, nome_monumento, data, horario, valor))
            conexao.commit()
            return True
        except mysql.Error as err:
            mensagem_erro = f"Erro ao acessar o banco de dados: {err}"
            print(mensagem_erro)
            return False
        except Exception as e:
            mensagem_erro = f"Erro durante o cadastro: {e}"
            print(mensagem_erro)
            return False
    
    def criar_ingresso_gratuito(self, idticket, nome_cliente, nome_monumento, data, horario):
        try:
            valor = 'Gratuito'
            conexao = mysql.connect(
                host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()

        # Inserir dados na tabela ticket
            cursor.execute("INSERT INTO ticket (idticket, nome_cliente, nome_monumento, dia, horario, tipo_valor) VALUES (%s, %s, %s, %s, %s, %s)",
                           (idticket, nome_cliente, nome_monumento, data, horario, valor))
            conexao.commit()

        # Criar dados do QR code
            dados_qrcode = f'{idticket};{nome_cliente};{nome_monumento};{data};{horario};{valor}'

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(dados_qrcode)
            qr.make(fit=True)

        # Criar imagem do QR code
            img = qr.make_image(fill_color="black", back_color="white")

        # Converter a imagem para bytes
            buffer = BytesIO()
            img.save(buffer)
            imagem_bytes = buffer.getvalue()

        # Inserir dados na tabela qrcodes
            cursor.execute("INSERT INTO qrcodes (id, imagem) VALUES (%s, %s)", (idticket, imagem_bytes,))
            conexao.commit()

        # Fechar o cursor e a conexão
            cursor.close()
            conexao.close()

            return True
        except mysql.connector.Error as err:
            mensagem_erro = f"Erro ao acessar o banco de dados: {err}"
            print(mensagem_erro)
            return False
        except Exception as e:
            mensagem_erro = f"Erro durante o cadastro: {e}"
            print(mensagem_erro)
            return False
    
    def listar_restaurantes_cliente(self):
        try:
            conexao = mysql.connect(
                  host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("SELECT nome, endereco, estacionamento, refeiçãoLocal, delivery FROM restaurantes")
            resultado = cursor.fetchall()
            
            json_resultado = json.dumps(resultado)
            self.csocket.send(json_resultado.encode('utf-8'))
        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return False   
    
    def listar_hoteis_cliente(self):
        try:
            conexao = mysql.connect(
                host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("SELECT nome, endereco, entacionamento, piscina FROM hoteis")
            resultado = cursor.fetchall()
            
            json_resultado = json.dumps(resultado)
            self.csocket.send(json_resultado.encode('utf-8'))
        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return False
    
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
            return False, "Erro na criação da conta."
        except Exception as e:
            mensagem_erro = f"Erro durante o cadastro: {e}"
            print(mensagem_erro)
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
            
    def listar_hoteis(self):
        try:
            conexao = mysql.connect(
                host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM hoteis")
            resultado = cursor.fetchall()

            json_resultado = json.dumps(resultado)
            self.csocket.send(json_resultado.encode('utf-8'))
        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return False
        finally:
            conexao.close()
    
    def listar_restaurantes(self):
        try:
            conexao = mysql.connect(
                host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM restaurantes")
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
    
    def cadastrar_novo_hotel(self, nome, endereco, estacionamento, piscina, link):
        try:
            conexao = mysql.connect(
              host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM hoteis WHERE nome = %s OR endereco = %s", (nome, endereco))
            existing_hotel = cursor.fetchone()
            if existing_hotel:
                nome_db, endereco_db = existing_hotel[1], existing_hotel[2]
                if nome_db == nome:
                    print('Encontrou o nome no banco de dados')
                    print(nome_db)
                    return nome_db
                elif endereco_db == endereco:
                    print('Encontrou o endereco no banco de dados')
                    print(endereco_db)
                    return endereco_db
            else:
                cursor.execute("INSERT INTO hoteis (nome, endereco, estacionamento, piscina, linkInstagram) VALUES (%s, %s, %s, %s, %s)",
                        (nome, endereco, estacionamento, piscina, link))

                conexao.commit()
                return True
        except mysql.Error as err:
            mensagem_erro = f"Erro ao acessar o banco de dados: {err}"
            print(mensagem_erro)
            return False
        except Exception as e:
            mensagem_erro = f"Erro durante o cadastro: {e}"
            print(mensagem_erro)
            return False
    
    def cadastrar_novo_restaurante(self, nome, endereco, estacionamento, refeicaoLocal, delivery, link):
        try:
            conexao = mysql.connect(
              host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM restaurantes WHERE nome = %s OR endereco = %s", (nome, endereco))
            existing_restaurante = cursor.fetchone()
            if existing_restaurante:
                nome_db, endereco_db = existing_restaurante[1], existing_restaurante[2]
                if nome_db == nome:
                    print('Encontrou o nome no banco de dados')
                    print(nome_db)
                    return nome_db
                elif endereco_db == endereco:
                    print('Encontrou o endereco no banco de dados')
                    print(endereco_db)
                    return endereco_db
            else:
                cursor.execute("INSERT INTO restaurantes (nome, endereco, estacionamento, refeiçãoLocal, delivery, linkInstagram) VALUES (%s, %s, %s, %s, %s, %s)",
                        (nome, endereco, estacionamento, refeicaoLocal, delivery, link))

                conexao.commit()
                return True
        except mysql.Error as err:
            mensagem_erro = f"Erro ao acessar o banco de dados: {err}"
            print(mensagem_erro)
            return False
        except Exception as e:
            mensagem_erro = f"Erro durante o cadastro: {e}"
            print(mensagem_erro)
            return False
        
    def busca_hotel(self, dado):
        try:
            id = dado.split(';')[0]
            conexao = mysql.connect(
                host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("SELECT nome FROM hoteis WHERE id = %s", (id,))
            resultado = cursor.fetchone()
            return resultado
        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return False
        finally:
            conexao.close()
    
    def busca_restaurante(self, dado):
        try:
            id = dado.split(';')[0]
            conexao = mysql.connect(
                host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("SELECT nome FROM restaurantes WHERE id = %s", (id,))
            resultado = cursor.fetchone()
            return resultado
        except mysql.Error as err:
            print(f"Erro ao acessar o banco de dados: {err}")
            return False
        finally:
            conexao.close()
    
    def excluir_hotel(self, id):
        try:
            conexao = mysql.connect(
              host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM hoteis WHERE id = %s", (id,))
            conexao.commit()
        except Exception as e:
            print(f"Erro durante a exclusão do hotel: {e}")
        
    def excluir_restaurante(self, id):
        try:
            conexao = mysql.connect(
              host='localhost', database='turismo', user='root', passwd='amor2004')
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM restaurantes WHERE id = %s", (id,))
            conexao.commit()
        except Exception as e:
            print(f"Erro durante a exclusão do restaurante: {e}")
        
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
