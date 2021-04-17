# caminho do Modulo aula13Contas/conta
from aula13Contas.conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, value):
        if value > self._saldo:
            print('Saldo insuficiente.')
            return

        self._saldo -= value
        self.detalhes()
