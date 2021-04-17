class Banco:
    def __init__(self):
        self.agencia = [1111, 2222, 3333]
        self.conta = []
        self.clientes = []

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.clientes.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.conta:
            return False

        if cliente.conta.agencia not in self.agencia:
            return False

        return True
