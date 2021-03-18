class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeClasse} está falando....')


# Cliente(filha de Pessoa) está herdando de Pessoa
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeClasse} está comprando...')

    def falar(self):
        print('Estou em CLIENTE.')


# ClienteVIP(filha de Cliente) está herdando de Cliente
class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        # super().__init__(nome, idade)
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')

    # def falar(self):
    #     # Chamando o método 'falar' da superClasse Pessoa
    #     super().falar()
    #     Cliente.falar(self)
    #     print('-'*10)
    #     # Ou chamando diretamente a superClasse Pessoa
    #     Pessoa.falar(self)
    #     print('-'*10)
    #     print('Estou sobreescrevendo método "falar" de pessoa.')
