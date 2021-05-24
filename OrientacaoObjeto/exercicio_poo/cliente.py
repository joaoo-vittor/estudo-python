from conta import Conta


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def getNome(self):
        return self._nome

    @getNome.setter
    def setNome(self, value):
        if not isinstance(value, str):
            raise ValueError("'nome' deve ser uma string.")
        self._nome = value

    @property
    def getIdade(self):
        return self._idade

    @getIdade.setter
    def setIdade(self, value):
        if not isinstance(value, int):
            raise ValueError("'idade' deve ser um numero inteiro.")
        self._idade = value


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def inserir_cliente(self, conta):
        self.conta = conta
