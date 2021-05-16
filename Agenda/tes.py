from os import curdir
import sqlite3

conexao = sqlite3.connect('db.sqlite3')
cursor = conexao.cursor()

query = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(query.fetchall())

query = cursor.execute("SELECT * FROM sqlite_sequence;")
print(query.fetchall())
