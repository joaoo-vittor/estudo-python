from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def getSaldo(self):
        return self._saldo

    @property
    def getAgencia(self):
        return self._agencia

    @property
    def getConta(self):
        return self._conta

    def detalhes(self):
        print(f'\nAgência: {self.getAgencia}')
        print(f'Conta: {self.getConta}')
        print(f'Saldo: R${self.getSaldo}\n')

    @getSaldo.setter
    def setSaldo(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Voce precisa passar um valor numerico!')
        self._saldo = value

    def depositar(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Voce precisa passar um valor numerico!')
        self._saldo += value
        self.detalhes()

    @abstractmethod
    def sacar(self, valor):
        pass
