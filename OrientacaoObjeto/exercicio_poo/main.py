"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""

from conta import ContaPoupanca, ContaCorrente
from cliente import Cliente
from banco import Banco

banco = Banco()

cliente1 = Cliente('joao', 22)
cliente2 = Cliente('vitor', 26)

conta1 = ContaPoupanca(1111, 2222, 0)
conta2 = ContaCorrente(2222, 3333, 0)

cliente1.inserir_cliente(conta1)
cliente2.inserir_cliente(conta2)

print(cliente1.getNome)
cliente1.conta.detalhes()
print(cliente2.getNome)
cliente2.conta.detalhes()

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)
