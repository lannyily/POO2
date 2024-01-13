import mysql.connector

# Conecta ao banco de dados MySQL
conexao = mysql.connector.connect(
    host='localhost',
    database='seu_banco_de_dados',
    user='seu_usuario',
    password='sua_senha'
)
cursor = conexao.cursor()

# Inserção de dados
try:
    # Substitua 'sua_tabela' pelo nome real da sua tabela
    cursor.execute("INSERT INTO sua_tabela (campo1, campo2) VALUES (%s, %s)", ('valor1', 'valor2'))
    conexao.commit()
    print("Dados inseridos com sucesso!")
except Exception as e:
    print(f"Erro ao inserir dados: {e}")

# Busca de dados
try:
    cursor.execute("SELECT * FROM sua_tabela WHERE campo1 = %s", ('valor1',))
    dados = cursor.fetchall()
    for linha in dados:
        print(f"Dados encontrados: {linha}")
except Exception as e:
    print(f"Erro ao buscar dados: {e}")

# Modificação de dados
try:
    # Substitua 'seu_novo_valor' pelo novo valor que você deseja atribuir ao campo
    cursor.execute("UPDATE sua_tabela SET campo2 = %s WHERE campo1 = %s", ('seu_novo_valor', 'valor1'))
    conexao.commit()
    print("Dados modificados com sucesso!")
except Exception as e:
    print(f"Erro ao modificar dados: {e}")

# Fecha a conexão com o banco de dados
conexao.close()
