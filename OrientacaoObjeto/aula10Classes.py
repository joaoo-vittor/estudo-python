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


# Aluno(filha de Pessoa) está herdando de Pessoa
class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeClasse} está estudando...')
