import sqlite3

conexao = sqlite3.connect(r'd:\github\projetos-python\6-python-base_de_dados\aula01-sqlite\bancodedadosbrowser.db')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#    'nome TEXT,'
#    'peso REAL'
#    ')')

""" # cada vez que é executado ele insere no BD
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
# ou
cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
    {'nome': 'Joãozinho', 'peso': 25}
    )
# ou
cursor.execute(
    'INSERT INTO clientes VALUES (:id, :nome, :peso)',
    {'id': None, 'nome': 'Daniel', 'peso': 113}
    )
conexao.commit()

# mudar o nome
cursor.execute(
    'UPDATE clientes SET nome=:nome WHERE id=:id',
    {'nome': 'Joana', 'id': 2}
    )

# deletar o nome !!!!CUIDADO!!!
cursor.execute(
    'DELETE FROM clientes WHERE id=:id',
    {'id': 2}
)

conexao.commit()
"""
#cursor.execute(
#    'SELECT nome, peso FROM clientes WHERE peso > :peso',
#    {'peso': 50}
#    )

cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    identificador, nome, peso = linha

    print(identificador, nome, peso)


cursor.close()
conexao.close()