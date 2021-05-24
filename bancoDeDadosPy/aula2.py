"""
Aula 2

Python sqlite3 

"""
import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        consulta = 'SELECT id, nome, telefone FROM agenda'
        self.cursor.execute(consulta)

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT id, nome, telefone FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

    def criarTabela(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS agenda ('
                            'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                            'nome VARCHAR(30) NOT NULL,'
                            'telefone CHAR(12) NOT NULL'
                            ')')
        self.conn.commit()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    # agenda.criarTabela()
    # agenda.inserir('João Vitor', '99661144')
    # agenda.inserir('Luiz Otavio', '99661321')
    # agenda.inserir('Lucas Otavio', '99661321')
    # agenda.inserir('Jose', '99661321')
    agenda.listar()

    print('\n')

    agenda.buscar('Lu')
