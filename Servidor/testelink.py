import hashlib

senha = '12345678'
senha = hashlib.md5(senha.encode('utf-8')).hexdigest()
print(senha)
