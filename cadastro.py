import re
import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication

import mysql.connector as mysql

conexao = mysql.connect(host='localhost', database='turismo', user='root', passwd='amor2004')
cursor = conexao.cursor()

'''
sql = """CREATE TABLE `turismo`.`contas` (
  `idconta` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `cpf` VARCHAR(45) NOT NULL,
  `dataN` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idconta`));"""
  
cursor.execute(sql)
'''
class Cadastro:
    def __init__(self):
        self.conexao = mysql.connect(host='localhost', database='turismo', user='root', passwd='amor2004')
        self.cursor = self.conexao.cursor()

    def fechar_conexao(self):
        self.conexao.close()

    def cadastrar(self, pessoa):
        
        self.cursor.execute("INSERT INTO contas (nome, cpf, dataN, email, senha) VALUES (%s, %s, %s, %s, %s)",
                               (pessoa.nome, pessoa.cpf, pessoa.dataN, pessoa.email, pessoa.senha))
        self.conexao.commit()
        self.cursor.close()
        self.conexao.close()
        print("Dados inseridos com sucesso!")
        return True
    
        '''
        if self.verificar_email(pessoa.email) and self.verificar_cpf(pessoa.cpf):
            self.cursor.execute("INSERT INTO contas (nome, cpf, dataN, email, senha) VALUES (%s, %s, %s, %s, %s)",
                               (pessoa.nome, pessoa.cpf, pessoa.dataN, pessoa.email, pessoa.senha))
            self.conexao.commit()
            self.cursor.close()
            self.conexao.close()
            #print("Dados inseridos com sucesso!")
            return True
        return False, 'erro'
        '''
    '''if self.verificar_email(pessoa.email) and self.verificar_cpf(pessoa.cpf):
            if not self.buscar_cpf(pessoa.cpf) and not self.buscar_email(pessoa.email):
                # Inserir dados no banco de dados
                sql = "INSERT INTO contas (email, nome, senha, cpf, nascimento) VALUES (%s, %s, %s, %s, %s)"
                valores = (pessoa.email, pessoa.nome, pessoa.senha, pessoa.cpf, pessoa.nascimento)
                self.cursor.execute(sql, valores)
                self.conexao.commit()
                return True
            else:
                return False
        return False'''
        
    def busca(self, email):
        sql = "SELECT nome, email FROM contas WHERE email = %s"
        self.cursor.execute(sql, (email,))
        resultado = self.cursor.fetchone()
        if resultado:
            nome, email = resultado
            return nome, email
        else:
            return None


    def verificar_email(self, email):
        formato_email = r'^[\w\.-]+@[\w\.-]+\.\w+'
        if re.match(formato_email, email):
            return True, None
        return False, QMessageBox.information(None, '...', 'E-mail invalido, por favor insira um e-mail válido')

    def verificar_cpf(self, cpf):
        cpf = ''.join(filter(str.isdigit, cpf))
    
        if len(cpf) != 11:
            return False, 'CPF deve conter 11 dígitos'
    
        total = 0
        for i in range(9):
            total += int(cpf[i]) * (10 - i)
    
        resto = total % 11
        digito1 = 0 if resto < 2 else 11 - resto
        total = 0
    
        for i in range(10):
            total += int(cpf[i]) * (11 - i)
    
        resto = total % 11
        digito2 = 0 if resto < 2 else 11 - resto
    
        if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
            return True, None
    
        return False, QMessageBox.information(None, '...', 'CPF invalido, por favor insira um CPF válido'), 'erro'

    def buscar_email(self, email):
        sql = "SELECT email FROM contas WHERE email = %s"
        self.cursor.execute(sql, (email,))
        resultado = self.cursor.fetchone()
        if resultado:
            return resultado[0], QMessageBox.information(None, '...', 'Esse e-mail já esta sendo usado')
        return None

    def buscar_cpf(self, cpf):
        sql = "SELECT cpf FROM contas WHERE cpf = %s"
        self.cursor.execute(sql, (cpf,))
        resultado = self.cursor.fetchone()
        if resultado:
            return resultado[0], QMessageBox.information(None, '...', 'Esse CPF já esta sendo usado')
        return None