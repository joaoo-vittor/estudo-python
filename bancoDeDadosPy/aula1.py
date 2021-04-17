"""
Aula 1

SQLite: usando o módulo sqlite3

"""

import sqlite3

conexao = sqlite3.connect('basededados.db')

cursor = conexao.cursor()

"""
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')'
               )

cursor.execute('INSERT INTO clientes (nome, peso) VALUES ("João Vitor", 99.5)')


cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Otavio', 86.4))

cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
    {'nome': 'Maria', 'peso': 15})

cursor.execute(
    'INSERT INTO clientes VALUES (:id, :nome, :peso)',
    {'id': None, 'nome': 'Maria', 'peso': 15})

conexao.commit()
"""

"""
alterar = cursor.execute(
    'SELECT id, nome, peso FROM clientes WHERE id = 3').fetchall()

print(alterar)

cursor.execute('UPDATE clientes SET peso=:peso WHERE id=:id',
               {'id': 3, 'peso': 53})

cursor.execute('UPDATE clientes SET peso=:peso WHERE id=:id',
               {'id': 4, 'peso': 75})

cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',
               {'id': 4, 'nome': 'Simone'})

conexao.commit()

print('\n')
"""

# cursor.execute('DELETE FROM clientes WHERE id=:id', {'id': 3})
# conexao.commit()

cursor.execute('SELECT * FROM clientes')

for linha in cursor.fetchall():
    identificador, nome, peso = linha
    print(identificador, nome, peso)

print('\n')


cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 80')

for linha in cursor.fetchall():
    nome, peso = linha
    print(nome, peso)

cursor.close()
conexao.close()
