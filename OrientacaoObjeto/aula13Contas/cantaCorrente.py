from aula13Contas.conta import Conta


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def getLimite(self):
        return self._limite

    @getLimite.setter
    def setLimite(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('O valor de ser numerico "int" ou "float"')
        self._limite = value

    def sacar(self, value):
        if value > (self.getLimite + self.getSaldo):
            print('Saldo insuficiente')
            return
        self._saldo -= value
        self.detalhes()
