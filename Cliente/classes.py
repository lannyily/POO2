class Conta():
    def __init__(self, nome, cpf, dataN, email, senha):
        self._nome = nome
        self._cpf = cpf
        self._dataN = dataN
        self._email = email
        self._senha = senha
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def email(self):
        return self._email
    
    @property
    def dataN(self):
        return self._dataN
    
    @property
    def senha(self):
        return self._senha
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
        
    @email.setter
    def email(self, email):
        self._email = email
        
    @dataN.setter
    def dataN(self, dataN):
        self._dataN = dataN
        
    @senha.setter
    def senha(self, senha):
        self._senha = senha
      
class Ingresso_gratuito(Conta):
    def __init__(self, nome, email, data, guia, horario, codigo, valor, tipo, status):
        super().__init__(nome, email)
        self._data = data
        self._guia = guia
        self._horario = horario
        self._codigo = codigo
        self._valor = valor
        self._tipo = tipo 
        self._status = status
        
    @property
    def data(self):
        return self._data
    
    @property
    def guia(self):
        return self._guia
    
    @property
    def horario(self):
        return self._horario
    
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def status(self):
        return self._status
    
    @property
    def tipo(self):
        return self._tipo
    
    @data.setter
    def data(self, data):
        self._data = data
        
    @guia.setter
    def guia(self, guia):
        self._guia = guia
        
    @horario.setter
    def horario(self, horario):
        self._horario = horario
        
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo
        
    @status.setter
    def status(self, status):
        self._status = status
        
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo 
        
class Ingresso_pago(Conta):
    def __init__(self, nome, email, data, guia, horario, codigo, valor, tipo, status):
        super().__init__(nome, email)
        self._data = data
        self._guia = guia
        self._horario = horario
        self._codigo = codigo
        self._valor = valor
        self._tipo = tipo
        self._status = status
        
    @property
    def data(self):
        return self._data
    
    @property
    def guia(self):
        return self._guia
    
    @property
    def horario(self):
        return self._horario
    
    @property
    def codigo(self):
        return self._codigo
    
    @property
    def valor(self):
        return self._valor 
    
    @property
    def status(self):
        return self._status
    
    @property
    def tipo(self):
        return self._tipo
    
    @data.setter
    def data(self, data):
        self._data = data
        
    @guia.setter
    def guia(self, guia):
        self._guia = guia
        
    @horario.setter
    def horario(self, horario):
        self._horario = horario
        
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo
        
    @valor.setter
    def valor(self, valor):
        self._valor = valor
        
    @status.setter
    def status(self, status):
        self._status = status
        
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo 