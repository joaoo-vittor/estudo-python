from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError(
                "'depositar' precisa receber um numero de tipo 'int' ou 'float'")
        self.saldo += value
        self.detalhes()

    def detalhes(self):
        print(f'Agencia: {self.agencia}')
        print(f'Conta: {self.conta}')
        print(f'Saldo: {self.saldo}')

    @abstractmethod
    def sacar(self, value): pass


class ContaPoupanca(Conta):
    def sacar(self, value):
        if self.saldo > value:
            print("Saldo insuficiente!")
            return
        self.saldo -= value
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, value):
        if (self.saldo + self.limite) > value:
            print("Saldo insuficiente!")
            return
        self.saldo -= value
        self.detalhes()
